import base64
import json
import platform
import re
import sys
from tempfile import TemporaryFile
from unittest import IsolatedAsyncioTestCase

import aiohttp
from aioresponses import CallbackResult, aioresponses
from callee import Attrs
from mock import ANY, MagicMock

from auth0.v3.asyncify import asyncify
from auth0.v3.management import Clients, Guardian, Jobs

clients = re.compile(r"^https://example\.com/api/v2/clients.*")
factors = re.compile(r"^https://example\.com/api/v2/guardian/factors.*")
users_imports = re.compile(r"^https://example\.com/api/v2/jobs/users-imports.*")
payload = {"foo": "bar"}

telemetry = base64.b64encode(
    json.dumps(
        {
            "name": "auth0-python",
            "version": sys.modules["auth0"].__version__,
            "env": {
                "python": platform.python_version(),
            },
        }
    ).encode("utf-8")
).decode()

headers = {
    "User-Agent": "Python/{}".format(platform.python_version()),
    "Authorization": "Bearer jwt",
    "Content-Type": "application/json",
    "Auth0-Client": telemetry,
}


def get_callback(status=200, response=None):
    mock = MagicMock(
        return_value=CallbackResult(status=status, payload=response or payload)
    )

    def callback(url, **kwargs):
        return mock(url, **kwargs)

    return callback, mock


class TestAsyncify(IsolatedAsyncioTestCase):
    @aioresponses()
    async def test_get(self, mocked):
        callback, mock = get_callback()
        mocked.get(clients, callback=callback)
        c = asyncify(Clients)(domain="example.com", token="jwt")
        self.assertEqual(await c.all_async(), payload)
        mock.assert_called_with(
            Attrs(path="/api/v2/clients"),
            allow_redirects=True,
            params={"include_fields": "true"},
            headers=headers,
            timeout=ANY,
        )

    @aioresponses()
    async def test_post(self, mocked):
        callback, mock = get_callback()
        mocked.post(clients, callback=callback)
        c = asyncify(Clients)(domain="example.com", token="jwt")
        data = {"client": 1}
        self.assertEqual(await c.create_async(data), payload)
        mock.assert_called_with(
            Attrs(path="/api/v2/clients"),
            allow_redirects=True,
            json=data,
            headers=headers,
            timeout=ANY,
        )

    @aioresponses()
    async def test_file_post(self, mocked):
        callback, mock = get_callback()
        mocked.post(users_imports, callback=callback)
        j = asyncify(Jobs)(domain="example.com", token="jwt")
        users = TemporaryFile()
        self.assertEqual(await j.import_users_async("connection-1", users), payload)
        file_port_headers = headers.copy()
        file_port_headers.pop("Content-Type")
        mock.assert_called_with(
            Attrs(path="/api/v2/jobs/users-imports"),
            allow_redirects=True,
            data={
                "connection_id": "connection-1",
                "upsert": "false",
                "send_completion_email": "true",
                "external_id": None,
                "users": users,
            },
            headers=file_port_headers,
            timeout=ANY,
        )
        users.close()

    @aioresponses()
    async def test_patch(self, mocked):
        callback, mock = get_callback()
        mocked.patch(clients, callback=callback)
        c = asyncify(Clients)(domain="example.com", token="jwt")
        data = {"client": 1}
        self.assertEqual(await c.update_async("client-1", data), payload)
        mock.assert_called_with(
            Attrs(path="/api/v2/clients/client-1"),
            allow_redirects=True,
            json=data,
            headers=headers,
            timeout=ANY,
        )

    @aioresponses()
    async def test_put(self, mocked):
        callback, mock = get_callback()
        mocked.put(factors, callback=callback)
        g = asyncify(Guardian)(domain="example.com", token="jwt")
        data = {"factor": 1}
        self.assertEqual(await g.update_factor_async("factor-1", data), payload)
        mock.assert_called_with(
            Attrs(path="/api/v2/guardian/factors/factor-1"),
            allow_redirects=True,
            json=data,
            headers=headers,
            timeout=ANY,
        )

    @aioresponses()
    async def test_delete(self, mocked):
        callback, mock = get_callback()
        mocked.delete(clients, callback=callback)
        c = asyncify(Clients)(domain="example.com", token="jwt")
        self.assertEqual(await c.delete_async("client-1"), payload)
        mock.assert_called_with(
            Attrs(path="/api/v2/clients/client-1"),
            allow_redirects=True,
            params={},
            json=None,
            headers=headers,
            timeout=ANY,
        )

    @aioresponses()
    async def test_shared_session(self, mocked):
        callback, mock = get_callback()
        mocked.get(clients, callback=callback)
        async with asyncify(Clients)(domain="example.com", token="jwt") as c:
            self.assertEqual(await c.all_async(), payload)
        mock.assert_called_with(
            Attrs(path="/api/v2/clients"),
            allow_redirects=True,
            params={"include_fields": "true"},
            headers=headers,
            timeout=ANY,
        )

    @aioresponses()
    async def test_rate_limit(self, mocked):
        callback, mock = get_callback(status=429)
        mocked.get(clients, callback=callback)
        mocked.get(clients, callback=callback)
        mocked.get(clients, callback=callback)
        mocked.get(clients, payload=payload)
        c = asyncify(Clients)(domain="example.com", token="jwt")
        rest_client = c._async_client.client
        rest_client._skip_sleep = True
        self.assertEqual(await c.all_async(), payload)
        self.assertEqual(3, mock.call_count)
        (a, b, c) = rest_client._metrics["backoff"]
        self.assertTrue(100 <= a < b < c <= 1000)

    @aioresponses()
    async def test_timeout(self, mocked):
        callback, mock = get_callback()
        mocked.get(clients, callback=callback)
        c = asyncify(Clients)(domain="example.com", token="jwt", timeout=(8.8, 9.9))
        self.assertEqual(await c.all_async(), payload)
        mock.assert_called_with(
            ANY,
            allow_redirects=ANY,
            params=ANY,
            headers=ANY,
            timeout=aiohttp.ClientTimeout(sock_connect=8.8, sock_read=9.9),
        )
