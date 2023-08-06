import decimal
import logging
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Type, Union

import orjson
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.files.uploadedfile import UploadedFile as DJUploadedFile
from django.db import connection, transaction
from django.http import Http404, HttpRequest, HttpResponse, QueryDict
from django.http.multipartparser import MultiPartParserError, parse_header
from django.utils.datastructures import MultiValueDict
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from pydantic import BaseModel
from pydantic.error_wrappers import ValidationError

logger = logging.getLogger("djanticapi")

DEFAULT_JSON_OPTIONS = orjson.OPT_UTC_Z | orjson.OPT_PASSTHROUGH_DATACLASS | orjson.OPT_PASSTHROUGH_DATETIME | orjson.OPT_PASSTHROUGH_SUBCLASS | orjson.OPT_SERIALIZE_DATACLASS | orjson.OPT_SERIALIZE_NUMPY | orjson.OPT_SERIALIZE_UUID


def default(obj):
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


class JsonResponse(HttpResponse):
    def __init__(self, data, encoder: Callable[[Any], Any] = default, option: int = DEFAULT_JSON_OPTIONS, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        if option is None:
            option = DEFAULT_JSON_OPTIONS
        data = orjson.dumps(data, default=encoder, option=option)
        super().__init__(content=data, **kwargs)


def valuedict_to_json(valuedict: MultiValueDict) -> Dict[str, Any]:
    full_data = {}
    for k in valuedict:
        v = valuedict.getlist(k, [None])
        if len(v) == 1:
            v = v[-1]
        full_data[k] = v
    return full_data


class UploadedFile(DJUploadedFile):
    @classmethod
    def __get_validators__(cls: Type["UploadedFile"]) -> Iterable[Callable[..., Any]]:
        yield cls.validate

    @classmethod
    def validate(cls: Type["UploadedFile"], v: Any) -> Any:
        if not isinstance(v, DJUploadedFile):
            raise ValueError(f"Expected UploadFile, received: {type(v)}")
        return v


class BaseParser:
    content_type = ''

    def parse(self,  request: HttpRequest) -> Tuple[Union[MultiValueDict, Dict], Optional[MultiValueDict]]:
        "returns a tuple of ``(MultiValueDict(Request Data), MultiValueDict(FILES))`"
        raise NotImplementedError(".parse() must be overridden.")


class JSONParser(BaseParser):
    content_type = 'application/json'

    def parse(self, request: HttpRequest) -> Tuple[Union[MultiValueDict, Dict], Optional[MultiValueDict]]:
        try:
            return orjson.loads(request.body), None
        except ValueError as exc:
            raise FormParseException('JSON parse error - %s' % exc)


class FormParser(BaseParser):
    content_type = 'application/x-www-form-urlencoded'

    def parse(self, request: HttpRequest) -> Tuple[Union[MultiValueDict, Dict], Optional[MultiValueDict]]:
        try:
            return QueryDict(request.body), None
        except ValueError as exc:
            raise FormParseException('Form parse error - %s' % exc)


class MultiPartParser(BaseParser):
    content_type = 'multipart/form-data'

    def parse(self, request: HttpRequest) -> Tuple[Union[MultiValueDict, Dict], Optional[MultiValueDict]]:
        try:
            post_data = request.POST
            files_data = request.FILES
            return post_data, files_data
        except MultiPartParserError as exc:
            raise FormParseException('Multipart form parse error - %s' % exc)


class ParserManager:
    def __init__(self) -> None:
        self._parsers: List["BaseParser"] = []

    def register(self, parser: 'BaseParser') -> bool:
        self._parsers.append(parser)
        return True

    def get(self, content_type: str) -> 'BaseParser':
        for p in self._parsers:
            if p.content_type in content_type:
                return p
        raise UnsupportedMediaTypeException('Unsupported media type "%s" in request.' % content_type)


parsers = ParserManager()
parsers.register(JSONParser())
parsers.register(FormParser())
parsers.register(MultiPartParser())


class BaseFormModel(BaseModel):
    @classmethod
    def from_request(cls, request: HttpRequest) -> 'BaseModel':
        if request.method.upper() == "GET":
            query_params = valuedict_to_json(request.GET)
            return cls(**query_params)

        meta = request.META
        try:
            content_length = int(meta.get('CONTENT_LENGTH', meta.get('HTTP_CONTENT_LENGTH', 0)))
        except (ValueError, TypeError):
            content_length = 0

        if content_length == 0:
            return cls()

        content_type = meta.get('CONTENT_TYPE', meta.get('HTTP_CONTENT_TYPE', ''))
        base_content_type, _ = parse_header(content_type.encode(settings.DEFAULT_CHARSET))
        if not base_content_type:
            return cls()
        parser = parsers.get(content_type=base_content_type)
        request_data, files = parser.parse(request)
        if isinstance(request_data, MultiValueDict):
            _full_data = valuedict_to_json(request_data)
        else:
            _full_data = request_data

        if files is not None:
            if isinstance(files, MultiValueDict):
                _full_data.update(valuedict_to_json(files))
            else:
                _full_data.update(files)

        return cls(**_full_data)


class BaseAPIView(View):

    @classmethod
    def as_view(cls: Any, **initkwargs: Any) -> Callable[..., HttpResponse]:
        view = super().as_view(**initkwargs)
        return csrf_exempt(view)

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        try:
            result = super().dispatch(request, *args, **kwargs)
            response = self.finalize_response(result)
        except ValidationError as exc:
            logger.warning("API handler `%s` request data validation failed, reason is %s.", request.path, exc)
            exc = FormParameterValidationException()
            response = self.handle_exception(exc)
        except Exception as exc:
            if not isinstance(exc, BaseAPIException):
                logger.exception("API handler failed, reason is %s", exc)
            response = self.handle_exception(exc)

        return response

    def http_method_not_allowed(self, request, *args, **kwargs):
        logger.warning('Method Not Allowed (%s): %s', request.method, request.path, extra={'status_code': 405, 'request': request})
        exc = HttpResponseNotAllowedException(err_detail='Method not allowed (%s)' % request.method)
        exc.headers = {'Allow': ', '.join(getattr(self, "_allowed_methods")())}
        raise exc

    def finalize_response(self, data: Any) -> HttpResponse:
        if isinstance(data, (JsonResponse, HttpResponse)):
            return data

        return JsonResponse(data=dict(data=data, err_msg="", err_code="Ok"))

    def handle_exception(self, exc: Exception) -> HttpResponse:
        if isinstance(exc, Http404):
            exc = NotFoundException()
        elif isinstance(exc, PermissionDenied):
            exc = PermissionDeniedException()

        if isinstance(exc, BaseAPIException):
            result = {'err_msg': exc.err_detail, 'err_code': exc.err_code}
            http_status_code = exc.http_status_code
        else:
            result = {'err_msg': exc.__doc__, 'err_code': 'UnknownError'}
            http_status_code = 500
        # django orm transaction rollback
        self._set_django_db_rollback()
        response = JsonResponse(data=result, status=http_status_code)
        if hasattr(exc, "headers"):
            for k, v in getattr(exc, "headers", {}).items():
                response[k] = v
        return response

    @staticmethod
    def _set_django_db_rollback():
        atomic_requests = connection.settings_dict.get('ATOMIC_REQUESTS', False)
        if atomic_requests and connection.in_atomic_block:
            transaction.set_rollback(True)


class BaseAPIException(Exception):
    http_status_code = 500
    default_err_detail = "A server error occurred."
    default_err_code = "UnknownError"
    _headers = {}

    def __init__(self, err_detail: str = None, err_code: str = None) -> None:
        self.err_detail = err_detail if err_detail is not None else self.default_err_detail
        self.err_code = err_code if err_code is not None else self.default_err_code

    @property
    def headers(self) -> Dict[str, Any]:
        return self._headers

    @headers.setter
    def headers(self, headers: Dict[str, Any]):
        self._headers = headers


class NotFoundException(BaseAPIException):
    http_status_code = 404
    default_err_detail = "Not found."
    default_err_code = "NotFound"


class PermissionDeniedException(BaseAPIException):
    http_status_code = 403
    default_err_detail = 'You do not have permission to perform this action.'
    default_err_code = 'PermissionDenied'


class FormParameterValidationException(BaseAPIException):
    http_status_code = 400
    default_err_detail = 'Illegal parameter in request parameter.'
    default_err_code = 'IllegalParameter'


class FormParseException(BaseAPIException):
    http_status_code = 400
    default_err_detail = 'Malformed request.'
    default_err_code = 'ParseError'


class UnsupportedMediaTypeException(BaseAPIException):
    http_status_code = 415
    default_err_detail = 'Unsupported media type in request.'
    default_err_code = 'UnsupportedMediaType'


class HttpResponseNotAllowedException(BaseAPIException):
    http_status_code = 405
    default_err_detail = 'Http response not allowed.'
    default_err_code = 'HttpResponseNotAllowed'
