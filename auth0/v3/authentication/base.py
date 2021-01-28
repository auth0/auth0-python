import base64
import json
import sys
import platform
import requests
from ..exceptions import Auth0Error, RateLimitError

UNKNOWN_ERROR = 'a0.sdk.internal.unknown'


class AuthenticationBase(object):
    """Base authentication object providing simple REST methods.

    Args:
        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)
    """

    def __init__(self, domain, telemetry=True, timeout=5.0, protocol="https"):
        self.domain = domain
        self.timeout = timeout
        self.protocol = protocol
        self.base_headers = {'Content-Type': 'application/json'}

        if telemetry:
            py_version = platform.python_version()
            version = sys.modules['auth0'].__version__

            auth0_client = json.dumps({
                'name': 'auth0-python',
                'version': version,
                'env': {
                    'python': py_version,
                }
            }).encode('utf-8')

            self.base_headers.update({
                'User-Agent': 'Python/{}'.format(py_version),
                'Auth0-Client': base64.b64encode(auth0_client),
            })

    def post(self, url, data=None, headers=None):
        request_headers = self.base_headers.copy()
        request_headers.update(headers or {})
        response = requests.post(url=url, json=data, headers=request_headers, timeout=self.timeout)
        return self._process_response(response)

    def get(self, url, params=None, headers=None):
        request_headers = self.base_headers.copy()
        request_headers.update(headers or {})
        response = requests.get(url=url, params=params, headers=request_headers, timeout=self.timeout)
        return self._process_response(response)

    def _process_response(self, response):
        return self._parse(response).content()

    def _parse(self, response):
        if not response.text:
            return EmptyResponse(response.status_code)
        try:
            return JsonResponse(response)
        except ValueError:
            return PlainResponse(response)


class Response(object):
    def __init__(self, status_code, content, headers):
        self._status_code = status_code
        self._content = content
        self._headers = headers

    def content(self):
        if self._is_error():
            if self._status_code == 429:
                reset_at = int(self._headers.get('x-ratelimit-reset', '-1'))
                raise RateLimitError(error_code=self._error_code(),
                                     message=self._error_message(),
                                     reset_at=reset_at)

            raise Auth0Error(status_code=self._status_code,
                             error_code=self._error_code(),
                             message=self._error_message())
        else:
            return self._content

    def _is_error(self):
        return self._status_code is None or self._status_code >= 400

    # Adding these methods to force implementation in subclasses because they are references in this parent class
    def _error_code(self):
        raise NotImplementedError

    def _error_message(self):
        raise NotImplementedError


class JsonResponse(Response):
    def __init__(self, response):
        content = json.loads(response.text)
        super(JsonResponse, self).__init__(response.status_code, content, response.headers)

    def _error_code(self):
        if 'error' in self._content:
            return self._content.get('error')
        elif 'code' in self._content:
            return self._content.get('code')
        else:
            return UNKNOWN_ERROR

    def _error_message(self):
        return self._content.get('error_description', '')


class PlainResponse(Response):
    def __init__(self, response):
        super(PlainResponse, self).__init__(response.status_code, response.text, response.headers)

    def _error_code(self):
        return UNKNOWN_ERROR

    def _error_message(self):
        return self._content


class EmptyResponse(Response):
    def __init__(self, status_code):
        super(EmptyResponse, self).__init__(status_code, '', {})

    def _error_code(self):
        return UNKNOWN_ERROR

    def _error_message(self):
        return ''
