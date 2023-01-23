import asyncio

import aiohttp

from auth0.exceptions import RateLimitError

from .rest import EmptyResponse, JsonResponse, PlainResponse, RestClient


def _clean_params(params):
    if params is None:
        return params
    return {k: v for k, v in params.items() if v is not None}


class AsyncRestClient(RestClient):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._session = None
        sock_connect, sock_read = (
            self.timeout
            if isinstance(self.timeout, tuple)
            else (self.timeout, self.timeout)
        )
        self.timeout = aiohttp.ClientTimeout(
            sock_connect=sock_connect, sock_read=sock_read
        )

    def set_session(self, session):
        """Set Client Session to improve performance by reusing session.
        Session should be closed manually or within context manager.
        """
        self._session = session

    async def _request(self, *args, **kwargs):
        kwargs["headers"] = kwargs.get("headers", self.base_headers)
        kwargs["timeout"] = self.timeout
        if self._session is not None:
            # Request with re-usable session
            async with self._session.request(*args, **kwargs) as response:
                return await self._process_response(response)
        else:
            # Request without re-usable session
            async with aiohttp.ClientSession() as session:
                async with session.request(*args, **kwargs) as response:
                    return await self._process_response(response)

    async def get(self, url, params=None, headers=None):
        request_headers = self.base_headers.copy()
        request_headers.update(headers or {})
        # Track the API request attempt number
        attempt = 0

        # Reset the metrics tracker
        self._metrics = {"retries": 0, "backoff": []}

        params = _clean_params(params)
        while True:
            # Increment attempt number
            attempt += 1

            try:
                response = await self._request(
                    "get", url, params=params, headers=request_headers
                )
                return response
            except RateLimitError as e:
                # If the attempt number is greater than the configured retries, raise RateLimitError
                if attempt > self._retries:
                    raise e

            wait = self._calculate_wait(attempt)

            # Skip calling sleep() when running unit tests
            if self._skip_sleep is False:
                # sleep() functions in seconds, so convert the milliseconds formula above accordingly
                await asyncio.sleep(wait / 1000)

    async def post(self, url, data=None, headers=None):
        request_headers = self.base_headers.copy()
        request_headers.update(headers or {})
        return await self._request("post", url, json=data, headers=request_headers)

    async def file_post(self, url, data=None, files=None):
        headers = self.base_headers.copy()
        headers.pop("Content-Type", None)
        return await self._request("post", url, data={**data, **files}, headers=headers)

    async def patch(self, url, data=None):
        return await self._request("patch", url, json=data)

    async def put(self, url, data=None):
        return await self._request("put", url, json=data)

    async def delete(self, url, params=None, data=None):
        return await self._request(
            "delete", url, json=data, params=_clean_params(params) or {}
        )

    async def _process_response(self, response):
        parsed_response = await self._parse(response)
        return parsed_response.content()

    async def _parse(self, response):
        text = await response.text()
        requests_response = RequestsResponse(response, text)
        if not text:
            return EmptyResponse(response.status)
        try:
            return JsonResponse(requests_response)
        except ValueError:
            return PlainResponse(requests_response)


class RequestsResponse:
    def __init__(self, response, text):
        self.status_code = response.status
        self.headers = response.headers
        self.text = text
