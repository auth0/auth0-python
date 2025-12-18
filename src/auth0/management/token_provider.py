import asyncio
import threading
import time
from typing import Optional

import httpx

LEEWAY_SECONDS = 10


class TokenProvider:
    """
    Sync token provider with caching and automatic refresh.

    Fetches tokens via OAuth 2.0 client credentials grant and caches them
    until they expire (with a 10-second leeway for safety).

    Thread-safe: uses a lock to prevent concurrent token fetches.
    """

    def __init__(
        self,
        *,
        domain: str,
        client_id: str,
        client_secret: str,
        audience: Optional[str] = None,
    ):
        self._domain = domain
        self._client_id = client_id
        self._client_secret = client_secret
        self._audience = audience or f"https://{domain}/api/v2/"

        self._access_token: Optional[str] = None
        self._expires_at: float = 0
        self._lock = threading.Lock()

    def get_token(self) -> str:
        """
        Get a valid access token, fetching a new one if expired.

        Returns
        -------
        str
            A valid access token.
        """
        # Fast path: return cached token if still valid
        if self._access_token and time.time() < (self._expires_at - LEEWAY_SECONDS):
            return self._access_token

        with self._lock:
            # Double-check after acquiring lock
            if self._access_token and time.time() < (self._expires_at - LEEWAY_SECONDS):
                return self._access_token
            self._fetch_token()

        return self._access_token  # type: ignore[return-value]

    def _fetch_token(self) -> None:
        """Fetch a new token via client credentials grant."""
        url = f"https://{self._domain}/oauth/token"
        payload = {
            "grant_type": "client_credentials",
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "audience": self._audience,
        }

        with httpx.Client() as client:
            response = client.post(url, data=payload)
            response.raise_for_status()
            data = response.json()

        self._access_token = data["access_token"]
        self._expires_at = time.time() + data["expires_in"]


class AsyncTokenProvider:
    """
    Async token provider with caching and automatic refresh.

    Fetches tokens via OAuth 2.0 client credentials grant and caches them
    until they expire (with a 10-second leeway for safety).

    Coroutine-safe: uses an async lock to prevent concurrent token fetches.
    """

    def __init__(
        self,
        *,
        domain: str,
        client_id: str,
        client_secret: str,
        audience: Optional[str] = None,
    ):
        self._domain = domain
        self._client_id = client_id
        self._client_secret = client_secret
        self._audience = audience or f"https://{domain}/api/v2/"

        self._access_token: Optional[str] = None
        self._expires_at: float = 0
        self._lock = asyncio.Lock()

    async def get_token(self) -> str:
        """
        Get a valid access token, fetching a new one if expired.

        Returns
        -------
        str
            A valid access token.
        """
        # Fast path: return cached token if still valid
        if self._access_token and time.time() < (self._expires_at - LEEWAY_SECONDS):
            return self._access_token

        async with self._lock:
            # Double-check after acquiring lock
            if self._access_token and time.time() < (self._expires_at - LEEWAY_SECONDS):
                return self._access_token
            await self._fetch_token()

        return self._access_token  # type: ignore[return-value]

    async def _fetch_token(self) -> None:
        """Fetch a new token via client credentials grant."""
        url = f"https://{self._domain}/oauth/token"
        payload = {
            "grant_type": "client_credentials",
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "audience": self._audience,
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, data=payload)
            response.raise_for_status()
            data = response.json()

        self._access_token = data["access_token"]
        self._expires_at = time.time() + data["expires_in"]
