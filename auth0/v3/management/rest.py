import base64
import json
import platform
import sys
import requests

from ..exceptions import Auth0Error, RateLimitError
from time import sleep
from random import randint

UNKNOWN_ERROR = 'a0.sdk.internal.unknown'

class RestClientOptions(object):
    """Configuration object for RestClient. Used for configuring
            additional RestClient options, such as rate-limit
            retries.

    Args:
        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)
        retries (integer): In the event an API request returns a
            429 response header (indicating rate-limit has been
            hit), the RestClient will retry the request this many
            times using an exponential backoff strategy, before
            raising a RateLimitError exception. 10 retries max.
            (defaults to 3)
    """
    def __init__(self, telemetry=None, timeout=None, retries=None):
        self.telemetry = True
        self.timeout = 5.0
        self.retries = 3

        if telemetry is not None:
            self.telemetry = telemetry

        if timeout is not None:
            self.timeout = timeout

        if retries is not None:
            self.retries = retries

class RestClient(object):
    """Provides simple methods for handling all RESTful api endpoints.

    Args:
        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)
        options (RestClientOptions): Pass an instance of
            RestClientOptions to configure additional RestClient
            options, such as rate-limit retries. Overrides matching
            options passed to the constructor.
            (defaults to 3)
    """

    def __init__(self, jwt, telemetry=True, timeout=5.0, options=None):
        if options is None:
            options = RestClientOptions(telemetry=telemetry, timeout=timeout)

        self.options = options
        self.jwt = jwt

        self._metrics = {'retries': 0, 'backoff': []}
        self._skip_sleep = False

        self.base_headers = {
            'Authorization': 'Bearer {}'.format(self.jwt),
            'Content-Type': 'application/json',
        }

        if options.telemetry:
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

        # For backwards compatibility reasons only
        # TODO: Deprecate in the next major so we can prune these arguments. Guidance should be to use RestClient.options.*
        self.telemetry = options.telemetry
        self.timeout = options.timeout

    # Returns a hard cap for the maximum number of retries allowed (10)
    def MAX_REQUEST_RETRIES(self):
        return 10

    # Returns the maximum amount of jitter to introduce in milliseconds (100ms)
    def MAX_REQUEST_RETRY_JITTER(self):
        return 100

    # Returns the maximum delay window allowed (1000ms)
    def MAX_REQUEST_RETRY_DELAY(self):
        return 1000

    # Returns the minimum delay window allowed (100ms)
    def MIN_REQUEST_RETRY_DELAY(self):
        return 100

    def get(self, url, params=None):
        headers = self.base_headers.copy()

        # Track the API request attempt number
        attempt = 0

        # Reset the metrics tracker
        self._metrics = {'retries': 0, 'backoff': []}

        # Cap the maximum number of retries to 10 or fewer. Floor the retries at 0.
        retries = min(self.MAX_REQUEST_RETRIES(), max(0, self.options.retries))

        while True:
            # Increment attempt number
            attempt += 1

            # Issue the request
            response = requests.get(url, params=params, headers=headers, timeout=self.options.timeout);

            # If the response did not have a 429 header, or the retries were configured at 0, or the attempt number is equal to or greater than the configured retries, break
            if response.status_code != 429 or retries <= 0 or attempt > retries:
                break

            # Retry the request. Apply a exponential backoff for subsequent attempts, using this formula:
            # max(MIN_REQUEST_RETRY_DELAY, min(MAX_REQUEST_RETRY_DELAY, (100ms * (2 ** attempt - 1)) + random_between(1, MAX_REQUEST_RETRY_JITTER)))

            # Increases base delay by (100ms * (2 ** attempt - 1))
            wait = 100 * 2 ** (attempt - 1)

            # Introduces jitter to the base delay; increases delay between 1ms to MAX_REQUEST_RETRY_JITTER (100ms)
            wait += randint(1, self.MAX_REQUEST_RETRY_JITTER())

            # Is never more than MAX_REQUEST_RETRY_DELAY (1s)
            wait = min(self.MAX_REQUEST_RETRY_DELAY(), wait)

            # Is never less than MIN_REQUEST_RETRY_DELAY (100ms)
            wait = max(self.MIN_REQUEST_RETRY_DELAY(), wait)

            self._metrics['retries'] = attempt
            self._metrics['backoff'].append(wait)

            # Skip calling sleep() when running unit tests
            if self._skip_sleep is False:
                # sleep() functions in seconds, so convert the milliseconds formula above accordingly
                sleep(wait / 1000)

        # Return the final Response
        return self._process_response(response)

    def post(self, url, data=None):
        headers = self.base_headers.copy()

        response = requests.post(url, json=data, headers=headers, timeout=self.options.timeout)
        return self._process_response(response)

    def file_post(self, url, data=None, files=None):
        headers = self.base_headers.copy()
        headers.pop('Content-Type', None)

        response = requests.post(url, data=data, files=files, headers=headers, timeout=self.options.timeout)
        return self._process_response(response)

    def patch(self, url, data=None):
        headers = self.base_headers.copy()

        response = requests.patch(url, json=data, headers=headers, timeout=self.options.timeout)
        return self._process_response(response)

    def put(self, url, data=None):
        headers = self.base_headers.copy()

        response = requests.put(url, json=data, headers=headers, timeout=self.options.timeout)
        return self._process_response(response)

    def delete(self, url, params=None, data=None):
        headers = self.base_headers.copy()

        response = requests.delete(url, headers=headers, params=params or {}, json=data, timeout=self.options.timeout)
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
