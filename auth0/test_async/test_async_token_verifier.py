import time
import unittest
from unittest.mock import ANY

import jwt
import pytest
from aioresponses import aioresponses
from cryptography.hazmat.primitives import serialization
from yarl import URL

from .. import TokenValidationError
from ..authentication.async_token_verifier import (
    AsyncAsymmetricSignatureVerifier,
    AsyncJwksFetcher,
    AsyncTokenVerifier,
)
from ..test.authentication.test_token_verifier import (
    JWKS_RESPONSE_MULTIPLE_KEYS,
    JWKS_RESPONSE_SINGLE_KEY,
    RSA_PUB_KEY_1_JWK,
    RSA_PUB_KEY_1_PEM,
    RSA_PUB_KEY_2_PEM,
)
from .test_asyncify import get_callback

JWKS_URI = "https://example.auth0.com/.well-known/jwks.json"

PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDfytWVSk/4Z6rNu8UZ7C4tnU9x0vj5FCaj4awKZlxVgOR1Kcen
QqDOxJdrXXanTBJbZwh8pk+HpWvqDVgVmKhnt+OkgF//hIXZoJMhDOFVzX504kiZ
cu3bu7kFs+PUfKw5s59tmETFPseA/fIrad9YXHisMkNmPWhuKYJ3WfZAaQIDAQAB
AoGADPSfHL9qlcTanIJsTK3hln5u5PYDt9e0zPP5k7iNS93kW+wJROOUj6PN6EdG
4TSEM4ppcV3naMDo2GnhWY624P6LUB+CbDFzjQKq805vrxJuFnq50blscwVK/ffP
kODBm/gwk+FaliRpQTDAAPWkKbkRfkmPx4JMEmTDBQ45diECQQDxw3qp2+wa5WP5
9w7AYrDPq4Fd6gIFcmxracROUcdhhMmVHKA9DzTWY46cSoWZoChYhQhhyj8dlP8q
El8aevN9AkEA7PhxcNyff8aehqEQ/Z38bm3P+GgB9EkRinjesba2CqhEI5okzvb7
OIYdszgQUBqGKlST0a7s9KuTpd7moyy8XQJAY8hjk0HCxCMTTXMLspnJEh1eKo3P
wcHFP9wKeqzEFtrAfHuxIyJok2fJz3XuiEaTAF3/5KSdwi7h1dJ5UCuY3QJAM9rF
0CGnEWngJKu4MRdSNsP232+7Bb67hOagLJlDyp85keTYKyXmoV7PvvkEsNKtCzRI
yHiTx5KIE6LsK0bNzQJBAMV+1KyI8ua1XmqLDaOexvBPM86HnuP+8u5CthgrXyGm
nh9gurwbs/lBRYV/d4XBLj+dzHb2zC0Jo7u96wrOObw=
-----END RSA PRIVATE KEY-----"""

PUBLIC_KEY = {
    "kty": "RSA",
    "e": "AQAB",
    "kid": "kid-1",
    "n": "38rVlUpP-GeqzbvFGewuLZ1PcdL4-RQmo-GsCmZcVYDkdSnHp0KgzsSXa112p0wSW2cIfKZPh6Vr6g1YFZioZ7fjpIBf_4SF2aCTIQzhVc1-dOJImXLt27u5BbPj1HysObOfbZhExT7HgP3yK2nfWFx4rDJDZj1obimCd1n2QGk",
}


def get_pem_bytes(rsa_public_key):
    return rsa_public_key.public_bytes(
        serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo
    )


class TestAsyncAsymmetricSignatureVerifier(unittest.TestCase):
    @pytest.mark.asyncio
    @aioresponses()
    async def test_async_asymmetric_verifier_fetches_key(self, mocked):
        callback, mock = get_callback(200, JWKS_RESPONSE_SINGLE_KEY)
        await mocked.get(JWKS_URI, callback=callback)

        verifier = AsyncAsymmetricSignatureVerifier(JWKS_URI)

        key = await verifier._fetch_key("test-key-1")

        self.assertEqual(get_pem_bytes(key), RSA_PUB_KEY_1_PEM)


class TestAsyncJwksFetcher(unittest.TestCase):
    @pytest.mark.asyncio
    @aioresponses()
    @unittest.mock.patch(
        "auth0.authentication.token_verifier.time.time", return_value=0
    )
    async def test_async_get_jwks_json_twice_on_cache_expired(
        self, mocked, mocked_time
    ):
        fetcher = AsyncJwksFetcher(JWKS_URI, cache_ttl=100)

        callback, mock = get_callback(200, JWKS_RESPONSE_SINGLE_KEY)
        await mocked.get(JWKS_URI, callback=callback)
        await mocked.get(JWKS_URI, callback=callback)

        key_1 = await fetcher.get_key("test-key-1")
        expected_key_1_pem = get_pem_bytes(key_1)
        self.assertEqual(expected_key_1_pem, RSA_PUB_KEY_1_PEM)

        mock.assert_called_with(
            URL("https://example.auth0.com/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(mock.call_count, 1)

        mocked_time.return_value = 200

        # 2 seconds has passed, cache should be expired
        key_1 = await fetcher.get_key("test-key-1")
        expected_key_1_pem = get_pem_bytes(key_1)
        self.assertEqual(expected_key_1_pem, RSA_PUB_KEY_1_PEM)

        mock.assert_called_with(
            URL("https://example.auth0.com/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(mock.call_count, 2)

    @pytest.mark.asyncio
    @aioresponses()
    async def test_async_get_jwks_json_once_on_cache_hit(self, mocked):
        fetcher = AsyncJwksFetcher(JWKS_URI, cache_ttl=1)

        callback, mock = get_callback(200, JWKS_RESPONSE_MULTIPLE_KEYS)
        await mocked.get(JWKS_URI, callback=callback)
        await mocked.get(JWKS_URI, callback=callback)

        key_1 = await fetcher.get_key("test-key-1")
        key_2 = await fetcher.get_key("test-key-2")
        expected_key_1_pem = get_pem_bytes(key_1)
        expected_key_2_pem = get_pem_bytes(key_2)
        self.assertEqual(expected_key_1_pem, RSA_PUB_KEY_1_PEM)
        self.assertEqual(expected_key_2_pem, RSA_PUB_KEY_2_PEM)

        mock.assert_called_with(
            URL("https://example.auth0.com/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(mock.call_count, 1)

    @pytest.mark.asyncio
    @aioresponses()
    async def test_async_fetches_jwks_json_forced_on_cache_miss(self, mocked):
        fetcher = AsyncJwksFetcher(JWKS_URI, cache_ttl=1)

        callback, mock = get_callback(200, {"keys": [RSA_PUB_KEY_1_JWK]})
        await mocked.get(JWKS_URI, callback=callback)

        # Triggers the first call
        key_1 = await fetcher.get_key("test-key-1")
        expected_key_1_pem = get_pem_bytes(key_1)
        self.assertEqual(expected_key_1_pem, RSA_PUB_KEY_1_PEM)

        mock.assert_called_with(
            URL("https://example.auth0.com/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(mock.call_count, 1)

        callback, mock = get_callback(200, JWKS_RESPONSE_MULTIPLE_KEYS)
        await mocked.get(JWKS_URI, callback=callback)

        # Triggers the second call
        key_2 = await fetcher.get_key("test-key-2")
        expected_key_2_pem = get_pem_bytes(key_2)
        self.assertEqual(expected_key_2_pem, RSA_PUB_KEY_2_PEM)

        mock.assert_called_with(
            URL("https://example.auth0.com/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(mock.call_count, 1)

    @pytest.mark.asyncio
    @aioresponses()
    async def test_async_fetches_jwks_json_once_on_cache_miss(self, mocked):
        fetcher = AsyncJwksFetcher(JWKS_URI, cache_ttl=1)

        callback, mock = get_callback(200, JWKS_RESPONSE_SINGLE_KEY)
        await mocked.get(JWKS_URI, callback=callback)

        with self.assertRaises(Exception) as err:
            await fetcher.get_key("missing-key")

        mock.assert_called_with(
            URL("https://example.auth0.com/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(
            str(err.exception), 'RSA Public Key with ID "missing-key" was not found.'
        )
        self.assertEqual(mock.call_count, 1)

    @pytest.mark.asyncio
    @aioresponses()
    async def test_async_fails_to_fetch_jwks_json_after_retrying_twice(self, mocked):
        fetcher = AsyncJwksFetcher(JWKS_URI, cache_ttl=1)

        callback, mock = get_callback(500, {})
        await mocked.get(JWKS_URI, callback=callback)
        await mocked.get(JWKS_URI, callback=callback)

        with self.assertRaises(Exception) as err:
            await fetcher.get_key("id1")

        mock.assert_called_with(
            URL("https://example.auth0.com/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(
            str(err.exception), 'RSA Public Key with ID "id1" was not found.'
        )
        self.assertEqual(mock.call_count, 2)


class TestAsyncTokenVerifier(unittest.TestCase):
    @pytest.mark.asyncio
    @aioresponses()
    async def test_RS256_token_signature_passes(self, mocked):
        callback, mock = get_callback(200, {"keys": [PUBLIC_KEY]})
        await mocked.get(JWKS_URI, callback=callback)

        issuer = "https://tokens-test.auth0.com/"
        audience = "tokens-test-123"
        token = jwt.encode(
            {
                "iss": issuer,
                "sub": "auth0|123456789",
                "aud": audience,
                "exp": int(time.time()) + 86400,
                "iat": int(time.time()),
            },
            PRIVATE_KEY,
            algorithm="RS256",
            headers={"kid": "kid-1"},
        )

        tv = AsyncTokenVerifier(
            signature_verifier=AsyncAsymmetricSignatureVerifier(JWKS_URI),
            issuer=issuer,
            audience=audience,
        )
        payload = await tv.verify(token)
        self.assertEqual(payload["sub"], "auth0|123456789")

    @pytest.mark.asyncio
    @aioresponses()
    async def test_RS256_token_signature_fails(self, mocked):
        callback, mock = get_callback(
            200, {"keys": [RSA_PUB_KEY_1_JWK]}
        )  # different pub key
        await mocked.get(JWKS_URI, callback=callback)

        issuer = "https://tokens-test.auth0.com/"
        audience = "tokens-test-123"
        token = jwt.encode(
            {
                "iss": issuer,
                "sub": "auth0|123456789",
                "aud": audience,
                "exp": int(time.time()) + 86400,
                "iat": int(time.time()),
            },
            PRIVATE_KEY,
            algorithm="RS256",
            headers={"kid": "test-key-1"},
        )

        tv = AsyncTokenVerifier(
            signature_verifier=AsyncAsymmetricSignatureVerifier(JWKS_URI),
            issuer=issuer,
            audience=audience,
        )

        with self.assertRaises(TokenValidationError) as err:
            await tv.verify(token)
        self.assertEqual(str(err.exception), "Invalid token signature.")
