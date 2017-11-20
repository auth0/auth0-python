import base64
import json
import sys
import time

import requests

from ..exceptions import Auth0Error


UNKNOWN_ERROR = 'a0.sdk.internal.unknown'


class NopRateLimiter(object):
    def update(self, headers):
        pass

    def ensure_limit(self):
        pass


class RateLimiter(object):
    def __init__(self):
        self.ratelimit_reset = int(time.time()) - 1
        self.ratelimit_remaining = 1

    def update(self, headers):
        if 'x-ratelimit-remaining' in headers:
            self.ratelimit_remaining = int(headers['x-ratelimit-remaining'])

        if 'x-ratelimit-reset' in headers:
            self.ratelimit_reset = int(headers['x-ratelimit-reset'])

    def ensure_limit(self):
        self.ratelimit_remaining -= 1

        if self.ratelimit_remaining < 0:
            sleep_time = self.ratelimit_reset - int(time.time())
            if sleep_time > 0:
                time.sleep(sleep_time)


def extract_content(func):
    def _decorator(self, *args, **kwargs):
        response = func(self, *args, **kwargs)

        text = json.loads(response.text) if response.text else {}

        if isinstance(text, dict) and 'errorCode' in text:
            raise Auth0Error(status_code=text['statusCode'],
                             error_code=text['errorCode'],
                             message=text['message'])
        return text

    return _decorator


rate_limit_max_retries = 5


def rate_limited(func):
    def _decorator(self, *args, **kwargs):
        self.rate_limiter.ensure_limit()

        for _ in range(0, rate_limit_max_retries):
            response = func(self, *args, **kwargs)

            self.rate_limiter.update(response.headers)

            if response.status_code != 429:
                return response

        return response

    return _decorator


def client_method(func):
    return extract_content(rate_limited(func))


class RestClient(object):
    """Provides simple methods for handling all RESTful api endpoints. """

    def __init__(self, jwt, telemetry=True, rate_limiter=NopRateLimiter()):
        self.jwt = jwt
        self.rate_limiter = rate_limiter

        if telemetry:
            py_version = '%i.%i.%i' % (sys.version_info.major,
                                       sys.version_info.minor,
                                       sys.version_info.micro)

            # FIXME: is there a nicer way to do this?
            from ... import __version__ as version

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

            self.base_headers = {
                'User-Agent': 'Python/%s' % py_version,
                'Auth0-Client': base64.b64encode(auth0_client),
                'Content-Type': 'application/json'
            }
        else:
            self.base_headers = {}

    @client_method
    def get(self, url, params={}):
        headers = self.base_headers.copy()
        headers.update({
            'Authorization': 'Bearer %s' % self.jwt,
        })

        return requests.get(url, params=params, headers=headers)

    @client_method
    def post(self, url, data={}):
        headers = self.base_headers.copy()
        headers.update({
            'Authorization': 'Bearer %s' % self.jwt,
            'Content-Type': 'application/json'
        })

        return requests.post(url, data=json.dumps(data), headers=headers)

    @client_method
    def file_post(self, url, data={}, files={}):
        headers = self.base_headers.copy()
        headers.pop('Content-Type', None)
        headers.update({
            'Authorization': 'Bearer %s' % self.jwt,
        })

        return requests.post(url, data=data, files=files, headers=headers)

    @client_method
    def patch(self, url, data={}):
        headers = self.base_headers.copy()
        headers.update({
            'Authorization': 'Bearer %s' % self.jwt,
            'Content-Type': 'application/json'
        })

        return requests.patch(url, data=json.dumps(data), headers=headers)

    @client_method
    def put(self, url, data={}):
        headers = self.base_headers.copy()
        headers.update({
            'Authorization': 'Bearer %s' % self.jwt,
            'Content-Type': 'application/json'
        })

        return requests.put(url, data=json.dumps(data), headers=headers)

    @client_method
    def delete(self, url, params={}):
        headers = self.base_headers.copy()
        headers.update({
            'Authorization': 'Bearer %s' % self.jwt,
        })

        response = requests.delete(url, headers=headers, params=params)
        return self._process_response(response)

    def _process_response(self, response):
        self.rate_limiter.update(response.headers)

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
        return self._content.get('error', self._content.get('message', ''))

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
        return requests.delete(url, headers=headers, params=params)
