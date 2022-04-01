import asyncio
import json

import aiohttp

from .rest import EmptyResponse, JsonResponse, PlainResponse
from .rest import Response as _Response
from .rest import RestClient


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
        super(AsyncRestClient, self).__init__(*args, **kwargs)
        self._session = None

    def set_session(self, session):
        """Set Client Session to improve performance by reusing session.
        Session should be closed manually or within context manager.
        """
        self._session = session

    async def _request(self, *args, **kwargs):
        # FIXME add support for timeouts
        kwargs["headers"] = kwargs.get("headers", self.base_headers)
        if self._session is not None:
            # Request with re-usable session
            async with self._session.request(*args, **kwargs) as response:
                return await self._process_response(response)
        else:
            # Request without re-usable session
            async with aiohttp.ClientSession() as session:
                async with session.request(*args, **kwargs) as response:
                    return await self._process_response(response)

    async def get(self, url, params=None):
        return await self._request("get", url, params=_clean_params(params))

    async def post(self, url, data=None):
        return await self._request("post", url, json=data)

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


class RequestsResponse(object):
    def __init__(self, response, text):
        self.status_code = response.status
        self.headers = response.headers
        self.text = text
