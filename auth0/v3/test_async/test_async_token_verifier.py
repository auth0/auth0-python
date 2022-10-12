import time
import unittest

from aioresponses import aioresponses
from callee import Attrs
from mock import ANY

from ..authentication.async_token_verifier import (
    AsyncAsymmetricSignatureVerifier as AsymmetricSignatureVerifier,
)
from ..authentication.async_token_verifier import AsyncJwksFetcher as JwksFetcher
from ..test.authentication.test_token_verifier import (
    JWKS_RESPONSE_MULTIPLE_KEYS,
    JWKS_RESPONSE_SINGLE_KEY,
    RSA_PUB_KEY_1_JWK,
    RSA_PUB_KEY_1_PEM,
    RSA_PUB_KEY_2_PEM,
)
from .test_asyncify import get_callback

JWKS_URI = "https://example.auth0.com/.well-known/jwks.json"


class TestAsyncAsymmetricSignatureVerifier(unittest.TestCase):
    @aioresponses()
    async def test_async_asymmetric_verifier_fetches_key(self, mocked):
        callback, mock = get_callback(200, JWKS_RESPONSE_SINGLE_KEY)
        mocked.get(JWKS_URI, callback=callback)

        verifier = AsymmetricSignatureVerifier(JWKS_URI)

        key = await verifier._fetch_key_async("test-key")

        self.assertEqual(key, RSA_PUB_KEY_1_JWK)


class TestAsyncJwksFetcher(unittest.IsolatedAsyncioTestCase):
    @staticmethod
    def _get_pem_bytes(rsa_public_key):
        # noinspection PyPackageRequirements
        # requirement already includes cryptography -> pyjwt[crypto]
        from cryptography.hazmat.primitives import serialization

        return rsa_public_key.public_bytes(
            serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo
        )

    @aioresponses()
    async def test_async_get_jwks_json_twice_on_cache_expired(self, mocked):
        fetcher = JwksFetcher(JWKS_URI, cache_ttl=1)

        callback, mock = get_callback(200, JWKS_RESPONSE_SINGLE_KEY)
        mocked.get(JWKS_URI, callback=callback)
        mocked.get(JWKS_URI, callback=callback)

        key_1 = await fetcher.get_key_async("test-key-1")
        expected_key_1_pem = self._get_pem_bytes(key_1)
        self.assertEqual(expected_key_1_pem, RSA_PUB_KEY_1_PEM)

        mock.assert_called_with(
            Attrs(path="/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(mock.call_count, 1)

        time.sleep(2)

        # 2 seconds has passed, cache should be expired
        key_1 = await fetcher.get_key_async("test-key-1")
        expected_key_1_pem = self._get_pem_bytes(key_1)
        self.assertEqual(expected_key_1_pem, RSA_PUB_KEY_1_PEM)

        mock.assert_called_with(
            Attrs(path="/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(mock.call_count, 2)

    @aioresponses()
    async def test_async_get_jwks_json_once_on_cache_hit(self, mocked):
        fetcher = JwksFetcher(JWKS_URI, cache_ttl=1)

        callback, mock = get_callback(200, JWKS_RESPONSE_MULTIPLE_KEYS)
        mocked.get(JWKS_URI, callback=callback)
        mocked.get(JWKS_URI, callback=callback)

        key_1 = await fetcher.get_key_async("test-key-1")
        key_2 = await fetcher.get_key_async("test-key-2")
        expected_key_1_pem = self._get_pem_bytes(key_1)
        expected_key_2_pem = self._get_pem_bytes(key_2)
        self.assertEqual(expected_key_1_pem, RSA_PUB_KEY_1_PEM)
        self.assertEqual(expected_key_2_pem, RSA_PUB_KEY_2_PEM)

        mock.assert_called_with(
            Attrs(path="/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(mock.call_count, 1)

    @aioresponses()
    async def test_async_fetches_jwks_json_forced_on_cache_miss(self, mocked):
        fetcher = JwksFetcher(JWKS_URI, cache_ttl=1)

        callback, mock = get_callback(200, {"keys": [RSA_PUB_KEY_1_JWK]})
        mocked.get(JWKS_URI, callback=callback)

        # Triggers the first call
        key_1 = await fetcher.get_key_async("test-key-1")
        expected_key_1_pem = self._get_pem_bytes(key_1)
        self.assertEqual(expected_key_1_pem, RSA_PUB_KEY_1_PEM)

        mock.assert_called_with(
            Attrs(path="/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(mock.call_count, 1)

        callback, mock = get_callback(200, JWKS_RESPONSE_MULTIPLE_KEYS)
        mocked.get(JWKS_URI, callback=callback)

        # Triggers the second call
        key_2 = await fetcher.get_key_async("test-key-2")
        expected_key_2_pem = self._get_pem_bytes(key_2)
        self.assertEqual(expected_key_2_pem, RSA_PUB_KEY_2_PEM)

        mock.assert_called_with(
            Attrs(path="/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(mock.call_count, 1)

    @aioresponses()
    async def test_async_fetches_jwks_json_once_on_cache_miss(self, mocked):
        fetcher = JwksFetcher(JWKS_URI, cache_ttl=1)

        callback, mock = get_callback(200, JWKS_RESPONSE_SINGLE_KEY)
        mocked.get(JWKS_URI, callback=callback)

        with self.assertRaises(Exception) as err:
            await fetcher.get_key_async("missing-key")

        mock.assert_called_with(
            Attrs(path="/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(
            str(err.exception), 'RSA Public Key with ID "missing-key" was not found.'
        )
        self.assertEqual(mock.call_count, 1)

    @aioresponses()
    async def test_async_fails_to_fetch_jwks_json_after_retrying_twice(self, mocked):
        fetcher = JwksFetcher(JWKS_URI, cache_ttl=1)

        callback, mock = get_callback(500, {})
        mocked.get(JWKS_URI, callback=callback)
        mocked.get(JWKS_URI, callback=callback)

        with self.assertRaises(Exception) as err:
            await fetcher.get_key_async("id1")

        mock.assert_called_with(
            Attrs(path="/.well-known/jwks.json"),
            allow_redirects=True,
            params=None,
            headers=ANY,
            timeout=ANY,
        )
        self.assertEqual(
            str(err.exception), 'RSA Public Key with ID "id1" was not found.'
        )
        self.assertEqual(mock.call_count, 2)
