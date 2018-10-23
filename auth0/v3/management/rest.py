import sys
import platform
import json
import base64
import requests
from ..exceptions import Auth0Error


UNKNOWN_ERROR = 'a0.sdk.internal.unknown'


class RestClient(object):

    """Provides simple methods for handling all RESTful api endpoints. """

    def __init__(self, jwt, telemetry=True):
        self.jwt = jwt

        self.base_headers = {
            'Authorization': 'Bearer {}'.format(self.jwt),
            'Content-Type': 'application/json',
        }
        if telemetry:
            py_version = platform.python_version()
            version = sys.modules['auth0'].__version__

            auth0_client = json.dumps({
                'name': 'auth0-python', 'version': version,
                'dependencies': [
                    {
                        'name': 'requests',
                        'version': requests.__version__,
                    }
                ],
                'environment': [
                    {
                        'name': 'python',
                        'version': py_version,
                    }
                ]
            }).encode('utf-8')

            self.base_headers.update({
                'User-Agent': 'Python/{}'.format(py_version),
                'Auth0-Client': base64.b64encode(auth0_client),
            })

    def get(self, url, params=None):
        headers = self.base_headers.copy()

        response = requests.get(url, params=params, headers=headers)
        return self._process_response(response)

    def post(self, url, data=None):
        headers = self.base_headers.copy()

        response = requests.post(url, data=json.dumps(data or {}), headers=headers)
        return self._process_response(response)

    def file_post(self, url, data=None, files=None):
        headers = self.base_headers.copy()
        headers.pop('Content-Type', None)

        response = requests.post(url, data=data, files=files, headers=headers)
        return self._process_response(response)

    def patch(self, url, data=None):
        headers = self.base_headers.copy()

        response = requests.patch(url, data=json.dumps(data or {}), headers=headers)
        return self._process_response(response)

    def put(self, url, data=None):
        headers = self.base_headers.copy()

        response = requests.put(url, data=json.dumps(data or {}), headers=headers)
        return self._process_response(response)

    def delete(self, url, params=None):
        headers = self.base_headers.copy()

        response = requests.delete(url, headers=headers, params=params or {})
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
    def __init__(self, status_code, content):
        self._status_code = status_code
        self._content = content

    def content(self):
        if self._is_error():
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
        super(JsonResponse, self).__init__(response.status_code, content)

    def _error_code(self):
        if 'errorCode' in self._content:
            return self._content.get('errorCode')
        elif 'error' in self._content:
            return self._content.get('error')
        else:
            return UNKNOWN_ERROR

    def _error_message(self):
        message = self._content.get('message', '')
        if message is not None and message != '':
            return message
        return self._content.get('error', '')


class PlainResponse(Response):
    def __init__(self, response):
        super(PlainResponse, self).__init__(response.status_code, response.text)

    def _error_code(self):
        return UNKNOWN_ERROR

    def _error_message(self):
        return self._content


class EmptyResponse(Response):
    def __init__(self, status_code):
        super(EmptyResponse, self).__init__(status_code, '')

    def _error_code(self):
        return UNKNOWN_ERROR

    def _error_message(self):
        return ''
