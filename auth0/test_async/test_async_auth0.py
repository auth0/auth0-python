import re
import unittest
from unittest.mock import ANY, MagicMock

import pytest
from aioresponses import CallbackResult, aioresponses
from yarl import URL

from auth0.management.async_auth0 import AsyncAuth0 as Auth0

clients = re.compile(r"^https://example\.com/api/v2/clients.*")
factors = re.compile(r"^https://example\.com/api/v2/guardian/factors.*")
payload = {"foo": "bar"}


def get_callback(status=200):
    mock = MagicMock(return_value=CallbackResult(status=status, payload=payload))

    def callback(url, **kwargs):
        return mock(url, **kwargs)

    return callback, mock


class TestAuth0(unittest.IsolatedAsyncioTestCase):
    @pytest.mark.asyncio
    @aioresponses()
    async def test_get(self, mocked):
        callback, mock = get_callback()

        mocked.get(clients, callback=callback)

        auth0 = Auth0(domain="example.com", token="jwt")

        self.assertEqual(await auth0.clients.all_async(), payload)

        mock.assert_called_with(
            URL("https://example.com/api/v2/clients?include_fields=true"),
            allow_redirects=True,
            params={"include_fields": "true"},
            headers=ANY,
            timeout=ANY,
        )

    @pytest.mark.asyncio
    @aioresponses()
    async def test_shared_session(self, mocked):
        callback, mock = get_callback()
        callback2, mock2 = get_callback()

        mocked.get(clients, callback=callback)
        mocked.put(factors, callback=callback2)

        async with Auth0(domain="example.com", token="jwt") as auth0:
            self.assertEqual(await auth0.clients.all_async(), payload)
            self.assertEqual(
                await auth0.guardian.update_factor_async("factor-1", {"factor": 1}),
                payload,
            )

        mock.assert_called_with(
            URL("https://example.com/api/v2/clients?include_fields=true"),
            allow_redirects=True,
            params={"include_fields": "true"},
            headers=ANY,
            timeout=ANY,
        )

        mock2.assert_called_with(
            URL("https://example.com/api/v2/guardian/factors/factor-1"),
            allow_redirects=True,
            json={"factor": 1},
            headers=ANY,
            timeout=ANY,
        )
