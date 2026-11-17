import asyncio
import unittest
from unittest.mock import AsyncMock

from auth0.authentication.async_token_verifier import AsyncJwksFetcher
from auth0.authentication.exceptions import TokenValidationError


class TestAsyncJwksFetcher(unittest.IsolatedAsyncioTestCase):
    async def test_cancellation_propagates_without_retry(self):
        fetcher = AsyncJwksFetcher("https://example.invalid/jwks")
        started = asyncio.Event()

        async def get_jwks(url):
            started.set()
            await asyncio.Future()

        fetcher._async_client.get = AsyncMock(side_effect=get_jwks)
        task = asyncio.create_task(fetcher.get_key("test-key"))
        try:
            await asyncio.wait_for(started.wait(), timeout=1)
            task.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await asyncio.wait_for(task, timeout=1)
            self.assertTrue(task.cancelled())
            fetcher._async_client.get.assert_awaited_once()
        finally:
            task.cancel()
            await asyncio.gather(task, return_exceptions=True)

    async def test_request_error_still_reports_missing_key(self):
        fetcher = AsyncJwksFetcher("https://example.invalid/jwks")
        fetcher._async_client.get = AsyncMock(side_effect=RuntimeError("request failed"))

        with self.assertRaisesRegex(TokenValidationError, "RSA Public Key"):
            await fetcher.get_key("test-key")
