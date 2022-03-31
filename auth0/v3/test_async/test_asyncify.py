import asyncio
import unittest

import mock
from aioresponses import aioresponses

from auth0.v3.management.asyncify import asyncify
from auth0.v3.management.clients import Clients

payload = {"foo": "bar"}


class TestAsyncify(unittest.IsolatedAsyncioTestCase):
    @aioresponses()
    async def test_all(self, mocked):
        mocked.get(
            "https://example.com/api/v2/clients?include_fields=true",
            status=200,
            payload=payload,
        )
        c = asyncify(Clients)(
            domain="example.com",
            token="jwt",
        )
        self.assertEqual(await c.all_async(), payload)

    @aioresponses()
    async def test_all_shared_session(self, mocked):
        mocked.get(
            "https://example.com/api/v2/clients?include_fields=true",
            status=200,
            payload=payload,
        )
        async with asyncify(Clients)(
            domain="example.com",
            token="jwt",
        ) as c:
            self.assertEqual(await c.all_async(), payload)
