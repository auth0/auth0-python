import json

import jwt
import unittest
import time

from mock import MagicMock, patch

from ...authentication.token_verifier import TokenVerifier, AsymmetricSignatureVerifier, \
    SymmetricSignatureVerifier, JwksFetcher, SignatureVerifier
from ...exceptions import TokenValidationError

RSA_PUB_KEY_1_PEM = b"""-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuGbXWiK3dQTyCbX5xdE4\nyCuYp0AF2d15Qq1JSXT/lx8CEcXb9RbDddl8jGDv+spi5qPa8qEHiK7FwV2KpRE9\n83wGPnYsAm9BxLFb4YrLYcDFOIGULuk2FtrPS512Qea1bXASuvYXEpQNpGbnTGVs\nWXI9C+yjHztqyL2h8P6mlThPY9E9ue2fCqdgixfTFIF9Dm4SLHbphUS2iw7w1JgT\n69s7of9+I9l5lsJ9cozf1rxrXX4V1u/SotUuNB3Fp8oB4C1fLBEhSlMcUJirz1E8\nAziMCxS+VrRPDM+zfvpIJg3JljAh3PJHDiLu902v9w+Iplu1WyoB2aPfitxEhRN0\nYwIDAQAB\n-----END PUBLIC KEY-----\n"""
RSA_PUB_KEY_2_PEM = b"""-----BEGIN PUBLIC KEY-----\nMDowDQYJKoZIhvcNAQEBBQADKQAwJgIfAI7TBUCn8e1hj/fNpb5dqMf8Jj6Ja6qN\npqyeOGYEzAIDAQAB\n-----END PUBLIC KEY-----\n"""
RSA_PUB_KEY_1_JWK = {"kty": "RSA", "use": "sig", "n": "uGbXWiK3dQTyCbX5xdE4yCuYp0AF2d15Qq1JSXT_lx8CEcXb9RbDddl8jGDv-spi5qPa8qEHiK7FwV2KpRE983wGPnYsAm9BxLFb4YrLYcDFOIGULuk2FtrPS512Qea1bXASuvYXEpQNpGbnTGVsWXI9C-yjHztqyL2h8P6mlThPY9E9ue2fCqdgixfTFIF9Dm4SLHbphUS2iw7w1JgT69s7of9-I9l5lsJ9cozf1rxrXX4V1u_SotUuNB3Fp8oB4C1fLBEhSlMcUJirz1E8AziMCxS-VrRPDM-zfvpIJg3JljAh3PJHDiLu902v9w-Iplu1WyoB2aPfitxEhRN0Yw", "e": "AQAB", "kid": "test-key-1"}
RSA_PUB_KEY_2_JWK = {"kty": "RSA", "use": "sig", "n": "jtMFQKfx7WGP982lvl2ox_wmPolrqo2mrJ44ZgTM", "e": "AQAB", "kid": "test-key-2"}
JWKS_RESPONSE_SINGLE_KEY = {"keys": [RSA_PUB_KEY_1_JWK]}
JWKS_RESPONSE_MULTIPLE_KEYS = {"keys": [RSA_PUB_KEY_1_JWK, RSA_PUB_KEY_2_JWK]}
HMAC_SHARED_SECRET = "secret"

MOCKED_CLOCK = 1587592561  # Apr 22 2020 21:56:01 UTC
DEFAULT_LEEWAY = 60

expectations = {
  "audience": "tokens-test-123",
  "audience_alt": "external-test-999",
  "issuer": "https://tokens-test.auth0.com/",
  "nonce": "a1b2c3d4e5"
}


class TestSignatureVerifier(unittest.TestCase):

    def test_fail_at_creation_with_invalid_algorithm(self):
        alg = 12345

        with self.assertRaises(ValueError) as err:
            SymmetricSignatureVerifier("some secret", algorithm=alg)
        self.assertEqual(str(err.exception), "algorithm must be specified.")

        with self.assertRaises(ValueError) as err:
            AsymmetricSignatureVerifier("some url", algorithm=alg)
        self.assertEqual(str(err.exception), "algorithm must be specified.")

        with self.assertRaises(ValueError) as err:
            SignatureVerifier(algorithm=alg)
        self.assertEqual(str(err.exception), "algorithm must be specified.")

    def test_symmetric_verifier_uses_hs256_alg(self):
        verifier = SymmetricSignatureVerifier("some secret")
        self.assertEqual(verifier._algorithm, "HS256")

    def test_asymmetric_verifier_uses_rs256_alg(self):
        verifier = AsymmetricSignatureVerifier("some URL")
        self.assertEqual(verifier._algorithm, "RS256")

    def test_symmetric_verifier_fetches_key(self):
        verifier = SymmetricSignatureVerifier("some secret")
        key = verifier._fetch_key()

        self.assertEqual(verifier._shared_secret, "some secret")
        self.assertEqual(key, "some secret")

    def test_asymmetric_verifier_fetches_key(self):

        mock_fetcher = JwksFetcher('some URL')
        mock_fetcher.get_key = MagicMock('get_key')
        mock_fetcher.get_key.return_value = RSA_PUB_KEY_1_JWK

        verifier = AsymmetricSignatureVerifier("some URL")
        verifier._fetcher = mock_fetcher

        key = verifier._fetch_key('test-key')

        args, kwargs = mock_fetcher.get_key.call_args
        self.assertEqual(args[0], 'test-key')

        self.assertEqual(mock_fetcher, verifier._fetcher)
        self.assertEqual(mock_fetcher._jwks_url, "some URL")
        self.assertEqual(key, RSA_PUB_KEY_1_JWK)

    def test_fails_with_none_algorithm(self):
        # below is a token without signature and "signed" with none
        jwt = "ewogICJhbGciOiAibm9uZSIsCiAgInR5cCI6ICJKV1QiCn0.eyJ1c2VybmFtZSI6ImFkbWluIn0."

        verifier = SymmetricSignatureVerifier("some secret")
        with self.assertRaises(Exception) as err:
            verifier.verify_signature(jwt)
        self.assertEqual(str(err.exception), 'Signature algorithm of "none" is not supported. Expected the ID token to be signed with "HS256"')

        verifier = AsymmetricSignatureVerifier("some url")
        with self.assertRaises(Exception) as err:
            verifier.verify_signature(jwt)
        self.assertEqual(str(err.exception),
                         'Signature algorithm of "none" is not supported. Expected the ID token to be signed with "RS256"')


class TestJwksFetcher(unittest.TestCase):

    @staticmethod
    def _get_pem_bytes(rsa_public_key):
        # noinspection PyPackageRequirements
        # requirement already includes cryptography -> pyjwt[crypto]
        from cryptography.hazmat.primitives import serialization
        return rsa_public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)

    @patch('requests.get')
    def test_get_jwks_json_twice_on_cache_expired(self, mock_get):
        JWKS_URL = 'https://app.myhosting.com/.well-known/jwks.json'
        fetcher = JwksFetcher(JWKS_URL, cache_ttl=1)

        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = JWKS_RESPONSE_SINGLE_KEY

        key_1 = fetcher.get_key('test-key-1')
        expected_key_1_pem = self._get_pem_bytes(key_1)
        self.assertEqual(expected_key_1_pem, RSA_PUB_KEY_1_PEM)

        mock_get.assert_called_with(JWKS_URL)
        self.assertEqual(mock_get.call_count, 1)

        time.sleep(2)

        # 2 seconds has passed, cache should be expired
        key_1 = fetcher.get_key('test-key-1')
        expected_key_1_pem = self._get_pem_bytes(key_1)
        self.assertEqual(expected_key_1_pem, RSA_PUB_KEY_1_PEM)

        mock_get.assert_called_with(JWKS_URL)
        self.assertEqual(mock_get.call_count, 2)

    @patch('requests.get')
    def test_get_jwks_json_once_on_cache_hit(self, mock_get):
        JWKS_URL = 'https://app.myhosting.com/.well-known/jwks.json'
        fetcher = JwksFetcher(JWKS_URL)

        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = JWKS_RESPONSE_MULTIPLE_KEYS

        key_1 = fetcher.get_key('test-key-1')
        key_2 = fetcher.get_key('test-key-2')
        expected_key_1_pem = self._get_pem_bytes(key_1)
        expected_key_2_pem = self._get_pem_bytes(key_2)
        self.assertEqual(expected_key_1_pem, RSA_PUB_KEY_1_PEM)
        self.assertEqual(expected_key_2_pem, RSA_PUB_KEY_2_PEM)

        mock_get.assert_called_with(JWKS_URL)
        self.assertEqual(mock_get.call_count, 1)

    @patch('requests.get')
    def test_fetches_jwks_json_forced_on_cache_miss(self, mock_get):
        JWKS_URL = 'https://app.myhosting.com/.well-known/jwks.json'
        fetcher = JwksFetcher(JWKS_URL)

        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'keys':[RSA_PUB_KEY_1_JWK]}

        # Triggers the first call
        key_1 = fetcher.get_key('test-key-1')
        expected_key_1_pem = self._get_pem_bytes(key_1)
        self.assertEqual(expected_key_1_pem, RSA_PUB_KEY_1_PEM)

        mock_get.assert_called_with(JWKS_URL)
        self.assertEqual(mock_get.call_count, 1)

        mock_get.return_value.json.return_value = JWKS_RESPONSE_MULTIPLE_KEYS

        # Triggers the second call
        key_2 = fetcher.get_key('test-key-2')
        expected_key_2_pem = self._get_pem_bytes(key_2)
        self.assertEqual(expected_key_2_pem, RSA_PUB_KEY_2_PEM)

        mock_get.assert_called_with(JWKS_URL)
        self.assertEqual(mock_get.call_count, 2)

    @patch('requests.get')
    def test_fetches_jwks_json_once_on_cache_miss(self, mock_get):
        JWKS_URL = 'https://app.myhosting.com/.well-known/jwks.json'
        fetcher = JwksFetcher(JWKS_URL)

        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = JWKS_RESPONSE_SINGLE_KEY

        with self.assertRaises(Exception) as err:
            key_1 = fetcher.get_key('missing-key')

        mock_get.assert_called_with(JWKS_URL)
        self.assertEqual(str(err.exception), 'RSA Public Key with ID "missing-key" was not found.')
        self.assertEqual(mock_get.call_count, 1)

    @patch('requests.get')
    def test_fails_to_fetch_jwks_json_after_retrying_twice(self, mock_get):
        JWKS_URL = 'https://app.myhosting.com/.well-known/jwks.json'
        fetcher = JwksFetcher(JWKS_URL)

        mock_get.return_value.ok = False
        mock_get.return_value.status_code = 500
        mock_get.return_value.text = "Some error happened"

        with self.assertRaises(Exception) as err:
            key_1 = fetcher.get_key('id1')

        mock_get.assert_called_with(JWKS_URL)
        self.assertEqual(str(err.exception), 'RSA Public Key with ID "id1" was not found.')
        self.assertEqual(mock_get.call_count, 2)


class TestTokenVerifier(unittest.TestCase):

    @staticmethod
    def asymmetric_signature_verifier_mock():
        verifier = AsymmetricSignatureVerifier('some URL')
        verifier._fetch_key = MagicMock('_fetch_key')

        # noinspection PyUnresolvedReferences
        # requirement already includes cryptography -> pyjwt[crypto]
        verifier._fetch_key.return_value = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(RSA_PUB_KEY_1_JWK))
        return verifier

    def assert_fails_with_error(self, token, error_message, signature_verifier=None, audience=expectations['audience'], issuer=expectations['issuer'], nonce=None, max_age=None, clock=MOCKED_CLOCK, organization=None):
        sv = signature_verifier or self.asymmetric_signature_verifier_mock()
        tv = TokenVerifier(
            signature_verifier=sv,
            issuer=issuer,
            audience=audience,
            leeway=DEFAULT_LEEWAY
        )
        tv._clock = clock
        with self.assertRaises(TokenValidationError) as err:
            tv.verify(token, nonce, max_age, organization)
        self.assertEqual(str(err.exception), error_message)

    def test_fails_at_creation_with_invalid_signature_verifier(self):
        sv = "string is not an instance of signature verifier"
        with self.assertRaises(TypeError) as err:
            # noinspection PyTypeChecker
            TokenVerifier(signature_verifier=sv, issuer="valid issuer", audience="valid audience")
        self.assertEqual(str(err.exception), "signature_verifier must be an instance of SignatureVerifier.")

    def test_err_token_empty(self):
        token = ""
        self.assert_fails_with_error(token, "ID token is required but missing.")
        token = None
        self.assert_fails_with_error(token, "ID token is required but missing.")

    def test_err_token_format_invalid(self):
        token = "a.b"
        self.assert_fails_with_error(token, "ID token could not be decoded.")
        token = "a.b."
        self.assert_fails_with_error(token, "ID token could not be decoded.")
        token = "a.b.c.d"
        self.assert_fails_with_error(token, "ID token could not be decoded.")

    def test_HS256_token_signature_passes(self):
        token = "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF6cCI6InRva2Vucy10ZXN0LTEyMyIsImF1dGhfdGltZSI6MTU4NzY3ODk2MX0.Hn38QVtN_mWN0c-jOa-Fqq69kXpbBp0THsvE-CQ47Ps"

        sv = SymmetricSignatureVerifier(HMAC_SHARED_SECRET)
        tv = TokenVerifier(
            signature_verifier=sv,
            issuer=expectations['issuer'],
            audience=expectations['audience']
        )
        tv._clock = MOCKED_CLOCK
        tv.verify(token)

    def test_RS256_token_signature_passes(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF6cCI6InRva2Vucy10ZXN0LTEyMyIsImF1dGhfdGltZSI6MTU4NzY3ODk2MX0.Eo2jxdlrKmutIeyn9Un6VHorMJaCL5txPDCC3QiAQn0pYYnrRU7VMQwqbTiXLQ9zPYh5Q4pQmT-XRaGL-HwDH8vCUieVJKOm0-gNFAMzx1i8sRH1ubw75sn69y09AQKcitYtjnBmahgfZrswtsxOXM7XovlLftPjv6goAi_U38GYsS_V_zOBvdbX2cM5zdooJAC0e7vlCr3bXNo90qwgCuezvCGt1ZrgWyDNO9oMzK-TlK86q36LuIkux7XZboF5rc3zsThEce_tPufA5qoEa-7I_ybmjwlvOCWmngYLT52_S2CbHeRNarePMjZIlmAuG-DcetwO8jJsX84Ra0SdUw"

        sv = self.asymmetric_signature_verifier_mock()
        tv = TokenVerifier(
            signature_verifier=sv,
            issuer=expectations['issuer'],
            audience=expectations['audience']
        )
        tv._clock = MOCKED_CLOCK
        tv.verify(token)

    def test_HS256_token_signature_fails(self):
        token = "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF6cCI6InRva2Vucy10ZXN0LTEyMyIsImF1dGhfdGltZSI6MTU4NzY3ODk2MX0.invalidsignature"
        sv = SymmetricSignatureVerifier(HMAC_SHARED_SECRET)

        self.assert_fails_with_error(token, "Invalid token signature.", signature_verifier=sv)

    def test_RS256_token_signature_fails(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF6cCI6InRva2Vucy10ZXN0LTEyMyIsImF1dGhfdGltZSI6MTU4NzY3ODk2MX0.invalidsignature"
        sv = self.asymmetric_signature_verifier_mock()

        self.assert_fails_with_error(token, "Invalid token signature.", signature_verifier=sv)

    def test_fails_with_algorithm_not_supported(self):
        token = "eyJhbGciOiJub25lIn0.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF6cCI6InRva2Vucy10ZXN0LTEyMyIsImF1dGhfdGltZSI6MTU4NzY3ODk2MX0."
        self.assert_fails_with_error(token, 'Signature algorithm of "none" is not supported. Expected the ID token to be signed with "RS256"')
        return

    def test_fails_with_iss_missing(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF6cCI6InRva2Vucy10ZXN0LTEyMyIsImF1dGhfdGltZSI6MTU4NzY3ODk2MX0.XuWmo_XxNET0mOW1AaLwi8koUOd05TZULWCGF_3WbeR5VJB6aK0rzo8AkHXrSv9Yr6he_1N8xFDKBIIyXFa4Y2PN8kdwUQtsJcj-cj8_2Ta2S0vV6O7XqbW58eXhX8Ng0OUrqgkHT1leIUJnBZ10YhM0-0zmdIq_WlNnwTdmvAGtYAUGcjyUmq-QEKBc2YYnf83vtGuFT2xGUGsTKR_Jj7lH_QTYdFaiT4t7gwFyXhP5KVUkG3ebdQUkIAQnoY0TXwrgDDCQhAWiUYZehMlv7Ml4tqLsiIUMgm4w5wSfdTdhVEMa7wHPj7gp4s-bfEqaOuyg0xH24rP19LkJROITDw"
        self.assert_fails_with_error(token, 'Issuer (iss) claim must be a string present in the ID token')

    def test_fails_with_iss_invalid(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJzb21ldGhpbmctZWxzZSIsInN1YiI6ImF1dGgwfDEyMzQ1Njc4OSIsImF1ZCI6WyJ0b2tlbnMtdGVzdC0xMjMiLCJleHRlcm5hbC10ZXN0LTk5OSJdLCJleHAiOjE1ODc3NjUzNjEsImlhdCI6MTU4NzU5MjU2MSwibm9uY2UiOiJhMWIyYzNkNGU1IiwiYXpwIjoidG9rZW5zLXRlc3QtMTIzIiwiYXV0aF90aW1lIjoxNTg3Njc4OTYxfQ.HNQ1lXWWQOC4D1-D4XfYlF2MBE6F7TW1EoBqt3ayxehNqtc8ZUJ6MR4aE_o7NnY0aBNbp7J9okgRC2PIKPHZkXUdxHvGZNldrEDDKeKPe0kZFxF5sEK8RYCnJk5m28JFpgRYvXA9KjKnLsBsbV--8VnkgRlw0-LClxqp3ynoGgmh2dVvBqXV8DiAbRvvRPZOg7CVFqCxJoMFD0FJ_dej7ChxMDSe_NDW-CjG9rgEsw_el-_vUcKSp7bzZ1jKm0zOcPDRPfgda5oek0xR6_bg2es_TarYKCwlQCVG1NEmgcJ5gNeVIsrwaPrMXqGr9KNs-nLerQO9Jl1EhCU8No5Sfg"
        self.assert_fails_with_error(token, 'Issuer (iss) claim mismatch in the ID token; expected "{}", found "something-else"'.format(expectations['issuer']))

    def test_fails_with_sub_missing(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF6cCI6InRva2Vucy10ZXN0LTEyMyIsImF1dGhfdGltZSI6MTU4NzY3ODk2MX0.VtPtxkKh7vZKECzFiNXLWBeWcRgaX1lIOhW0fKU5WSgTcjYZRYoxW-wwI8pai7vgJMQQCizBpLpjMPpCBYBGEiYgGpa9D7vAD8XmYjcVZujG1FLFGkOTkgisCtgVT6WpvwxIejNrl_TcgSEBkCcD9f7gGnFVOjJe4YtSMEUdtuDz-pHEGGNbJLdq0L-pPUrO2Fyw3NspX1RrEYVn7uGuAlDQWQ4x6IOtM40NPzAmyLVrsOPmz_5Igyi7ZZar6epcfd5dBeUbgp8yK178XV-r6-UMuj39NJE4Bx8cDQR1qjxMsxgZ3Lem6OLfFvKWXsgJs7dh13kJDqrx2jXfhvpd-w"
        self.assert_fails_with_error(token, 'Subject (sub) claim must be a string present in the ID token')

    def test_fails_with_aud_missing(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJleHAiOjE1ODc3NjUzNjEsImlhdCI6MTU4NzU5MjU2MSwibm9uY2UiOiJhMWIyYzNkNGU1IiwiYXpwIjoidG9rZW5zLXRlc3QtMTIzIiwiYXV0aF90aW1lIjoxNTg3Njc4OTYxfQ.t5SBd_J-k_GwPHfyGfPxOcT8n0Pbwy9R-pj7tK8231m3My1Zg3LyKx3tl7MFtymgRHcs2hd4WrWrKjyFrHMOzUWX8dQ2-b6KVRuFQjc70gnW54igj-cT-oo07Lzen0Ol6_7w_5rabWCOL9lM0UM9jpau_llVh97zyYgcUEBeA5lLld5ZLTB-JKMVehjJelBR-MPEDvMr2zT9nRPPUXqezAWZOPYG83oRRB2ktoafaUM4RVvp34q6uUWJq49m-qY2DfKuyDGK4axo1fHKE3JmrsayEDpuGDYDFNDQzy4g1lJvzBKxV2SJl0LKP6sxbM8sw7qaH4ViRNZpFQBZ7veGPQ"
        self.assert_fails_with_error(token, 'Audience (aud) claim must be a string or array of strings present in the ID token')

    def test_fails_with_aud_invalid(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF6cCI6InRva2Vucy10ZXN0LTEyMyIsImF1dGhfdGltZSI6MTU4NzY3ODk2MX0.d1BFaw_h5VOAw0tXAQ98hrru4gWCNjIxcCQktFVcLIqrX9m74-vWv2SVoFBAQlXihEXoDS-5QSMhVPG1iry9arseN16PnSOmilBhSebiqAVSBojLxq5KFEDuUz90lApt4d5BSCMAIAQ1Dp1pGKwJC0BiLrFNOQ2KrmoEvQMgaD0PLlCLy1lL7MntABE86tX_BoqI4ZkWJ1lX1n2-SZAn-ldoOK8W8RUYiwBUDTktpgAfICFUSPAZXj_vn05vwvQBoozhMQkuJrPziz81Tj8lPh0iPsnMBtsAqvAhdwtp3p-eadXPVcjNu4yE3dkBgFDQwoNtV_elWQtmFBn49FEKyw"
        self.assert_fails_with_error(token, 'Audience (aud) claim mismatch in the ID token; expected "{}" but was not one of "external-test-999"'.format(expectations['audience']))

    def test_fails_with_exp_missing(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiaWF0IjoxNTg3NTkyNTYxLCJub25jZSI6ImExYjJjM2Q0ZTUiLCJhenAiOiJ0b2tlbnMtdGVzdC0xMjMiLCJhdXRoX3RpbWUiOjE1ODc2Nzg5NjF9.qq4Tyz8VGnAJy2KmKo3zmThnWXviGwJB-Bz18lnJlicjAXk4ObeUVoX0WHB3I8vmDMscC9JXhkDP5KIGSAkeaLzil0FFJwwQB_saFE_y3zjfMQgdsz_qtDR96S1SQtnZ7AhChIAZ7cV4p_wmj_-TQYuZVQ0F6MoBmFsJITIr7gxnNFJWw6KJEU94nq8-q_IAyC5-9epdEtphUi_wkalHzEy6w8tQawKXCLYxo12VNlEy5mi8PlwqGsqVcwFwqec-ERt2hajyuqL1210-cZJMA-NmXz4mv4scHdiE09KZcLScKcezs9KaM5iaButMBL0Fyec0KcwwfELX_zghekALOA"
        self.assert_fails_with_error(token, 'Expiration Time (exp) claim must be a number present in the ID token')

    def test_fails_with_exp_invalid(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NTkyNTYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF6cCI6InRva2Vucy10ZXN0LTEyMyIsImF1dGhfdGltZSI6MTU4NzY3ODk2MX0.KUbd2s3Km-PVpP8KEJo1e0lyQv19TjiKMFX-lVebFoiPNwlVTXS08g5qe_G8pcOrwNfX6cRkRLbp7TNQ7tGDCuEcdia9KOaWeVWla5B3UPCv1qozCyMv4ZYrA0qdT2KgwytRMVWSov9ly29FSo6SRQksAMKZdnAzPaqnJGKBgVIjKN3a5ePIeX5yBIGxlNjS3nyWt8LIQJ9BFaQWk3i0vAKYpDeco3VLNLX-wH7739MzS7ll6t6LyuZi6kBaRG6XZc394glKidTvCp06ViQlPlcuV7JsCJfbkBc0AS5TmzOEdUCype-gzNqbuLcSXihS-qOx7Yjv8y3farV1_7qYqw"
        mocked_clock = MOCKED_CLOCK + DEFAULT_LEEWAY + 1
        self.assert_fails_with_error(token, 'Expiration Time (exp) claim error in the ID token; current time ({}) is after expiration time (1587592621)'.format(mocked_clock), clock=mocked_clock)

    def test_fails_with_iat_missing(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJub25jZSI6ImExYjJjM2Q0ZTUiLCJhenAiOiJ0b2tlbnMtdGVzdC0xMjMiLCJhdXRoX3RpbWUiOjE1ODc2Nzg5NjF9.CWW7mWUhiI-rramQ2dIGi7vBsOMmsouIg32IL9u2g4Dg3PV0C55R7dL6Jvf9hqaZXvx9Psrw0vLnOlhFztAC6LlQuq2eCaLYsDme36NxeYGC7CFXygvlU_eXD5IdNK35GriTfpG_b5hC7tl2glMmNQcZWlsIyKw7eq8o1POpqo0K2bCVjoyJkHL6WUpw6_08HPspmTL_Qd0km08z6zgvbl8Hpzk-tLmXqN7LjmuhEsjnIFphu-dGwcQsoY3RAomYxAFXAPYT8siEIf2w3zlIoUde-mujiMUtMD-Od7t7w36GO6Kubb9M9inVwPEg1yFKlFTXZBKXu91xmOmvMJ5Qfg"
        self.assert_fails_with_error(token, 'Issued At (iat) claim must be a number present in the ID token')

    def test_passes_when_nonce_missing_but_not_required(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsImF6cCI6InRva2Vucy10ZXN0LTEyMyIsImF1dGhfdGltZSI6MTU4NzY3ODk2MX0.L-DveLCDf4Te7x3JZmQ6rCkUQrenl1NFpHqKD8Fs-glhd2iyc-TYffk1M30T0-wBri-3tTgraDAjZAjXuwSk0gV_V5uKCHyIoSRphrC88aX8IeECteQpHa4KR15lbzA5JdVhJu7LuCZ2EFvdjHh5GiViLRWsTSHGUM-uqcMK0q2kWGvCEgfOIXqocnQiyCNITxfgMYJd38zOsVeP7HFf9riuFEQz65oER22o3xyIZ-ILSaU10n6Ob559Rbjc0NVKH4hrggRg8kG7cJCiXbRxXnzO_VM8LmRHhF56jh3ZSrO4bzQa5xv04bMbX6A77muMZD0vghsaslvpWerWbwaSQQ"

        sv = self.asymmetric_signature_verifier_mock()
        tv = TokenVerifier(
            signature_verifier=sv,
            issuer=expectations['issuer'],
            audience=expectations['audience']
        )
        tv._clock = MOCKED_CLOCK
        tv.verify(token)

    def test_fails_with_nonce_missing(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsImF6cCI6InRva2Vucy10ZXN0LTEyMyIsImF1dGhfdGltZSI6MTU4NzY3ODk2MX0.L-DveLCDf4Te7x3JZmQ6rCkUQrenl1NFpHqKD8Fs-glhd2iyc-TYffk1M30T0-wBri-3tTgraDAjZAjXuwSk0gV_V5uKCHyIoSRphrC88aX8IeECteQpHa4KR15lbzA5JdVhJu7LuCZ2EFvdjHh5GiViLRWsTSHGUM-uqcMK0q2kWGvCEgfOIXqocnQiyCNITxfgMYJd38zOsVeP7HFf9riuFEQz65oER22o3xyIZ-ILSaU10n6Ob559Rbjc0NVKH4hrggRg8kG7cJCiXbRxXnzO_VM8LmRHhF56jh3ZSrO4bzQa5xv04bMbX6A77muMZD0vghsaslvpWerWbwaSQQ"
        self.assert_fails_with_error(token, 'Nonce (nonce) claim must be a string present in the ID token', nonce=expectations['nonce'])

    def test_fails_with_nonce_invalid(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiMDAwOTk5IiwiYXpwIjoidG9rZW5zLXRlc3QtMTIzIiwiYXV0aF90aW1lIjoxNTg3Njc4OTYxfQ.Z0n4vKcTCTrKJXUx56TyoQk3-okpjOqCDRN9NqH5zkCi0at7WV-E3TxGbXpIN0UsXwUWxrHiuvL9lN2M4PoIvL4XvzUqgsepAYYBCPGR9Wxb-ALmhhWdS_LNRVAgfUCn94khc_G51XtyeP0bQgWRkV7VbeWxkBTnrhmGwEkVx6XbfpnTRUCDSR_luJfUu84LkFJf1n2ohnEU7Q74BXJjxIIJnhZrg4J65E3cNtZ9N7AOIrbpbZ0oB7NhcZP0xA0A75qt7ZnKOuLsbRppZjcz56QmVIArOSCkkegl3qLx4cNdVa-O840AQWCwkAcHxS9lHBIWyaToC7IVMOLxIcGVlQ"
        self.assert_fails_with_error(token, 'Nonce (nonce) claim mismatch in the ID token; expected "{}", found "000999"'.format(expectations['nonce']), nonce=expectations['nonce'])

    def test_fails_with_aud_array_and_azp_missing(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF1dGhfdGltZSI6MTU4NzY3ODk2MX0.Xpxc2tj3sDwAYftYAcoiLO3kq0X54KSngDzQu_foTjlDQFTPApVVrX_BQqMAUFsmiNdt-3Tf9lkUlAagpvXy_VUY5LIjzEihEKDzqQFMQ8wm7RK7qV2XLS1abltxXd8AuOHcPnVHbtERpsCXR5eRt0-ESSPUw_scqHOwmYQOFF0sOQJ72r9EYZFMGhojyzpbzhBF0jgi9wMqj0VSpLEzZ3MnkWBCTlmc5OAPXQGdq6C1dVfcBXy4iiIBEaPCG962Yqrr-bbL92_T_XG-FmtpIViuRjHDWRJ26uoD0cmXwePwojxlyeY7VrAoKX3VtA4lm1Co0BMh9DjMKv-p3zT6XA"
        self.assert_fails_with_error(token, 'Authorized Party (azp) claim must be a string present in the ID token when Audience (aud) claim has multiple values')

    def test_fails_with_aud_array_and_azp_invalid(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF6cCI6ImV4dGVybmFsLXRlc3QtOTk5IiwiYXV0aF90aW1lIjoxNTg3Njc4OTYxfQ.Bx56kdY8rBwlAZ8Walh6NjONs94Tdv37iP0EPKFxvpELFt_8RENhPp8Lqe52zrrgXqUdA1eeBynegqH7_duJawQ0l86u2dsaPonMOsh_W8ZjaqPOVHLv1z7xQb84UdjMSSJbMGMLPmuX2GMlc5hcjW5YgWU1xp-gpNpKMIzW19gNxpwtIWkLZ5zkjEVBYHSTAw7CO6HkncTZBqdYA3bq3ziQPljqvSvyPehuJ-2Q5TlrdVLRO5HS4-C6NEs-h8fpX25NP537FM9g7T7pRB1wDxsrJTny6uKBKFCwtNSF5laojV2edEDlDUsEEUCGh6zUzITGeZNa0M52ZsxGoAehIw"
        self.assert_fails_with_error(token,
                                     'Authorized Party (azp) claim mismatch in the ID token; expected "{}", found "external-test-999"'.format(expectations['audience']))

    def test_fails_when_max_age_sent_with_auth_time_missing(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF6cCI6InRva2Vucy10ZXN0LTEyMyJ9.pWr6hjQ9Mi9cYSYIFWG1d-KJ98OeKeKb3F7X_DdUgQ5Xir8wHLLuZDrFAalKlxYiTJTMXqh9YkxKLcEjFQsTECEXA4VMliUv4A2Egk8EDUi5SQtoQ11xGJo-S7qM4cL-x-69ZnJvNWlZZ8NnvtTOSgzpa_fsG7T3PScr0b9ukxOQ-o8suV2fLE7bOliBKZn9PC7sowtF_oeQ03f0e0thtZFl121ROL65ARh9C-ic2azgmIn3YgsvguaoT5ZpAFRe2McaP026bNimOmfEzVIwHCDuR6rkFZvX4QUduX6UQ4bOQp_EC9G0XDk08H0nBXx2JXSHCW4YPZz9bz1f12B4kg"
        self.assert_fails_with_error(token, "Authentication Time (auth_time) claim must be a number present in the ID token when Max Age (max_age) is specified", max_age=120)

    def test_fails_when_max_age_sent_with_auth_time_invalid(self):
        token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkiLCJhdWQiOlsidG9rZW5zLXRlc3QtMTIzIiwiZXh0ZXJuYWwtdGVzdC05OTkiXSwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjEsIm5vbmNlIjoiYTFiMmMzZDRlNSIsImF6cCI6InRva2Vucy10ZXN0LTEyMyIsImF1dGhfdGltZSI6MTU4NzU5MjU2MX0.VcVv1cGthPtuHZAZa-x7XZjhrcKEV3xUW6rVfhNMM_zCRBxLdyJl6gVv396eyfMX5-3dhr0-9kAYQAjPrmcvUDFLOR4Qjamg83U-TMa4agnYwQ_Iv3u_zhYmSrKzZlQvbOhT5imZShL11hycyukv2D1ODbFpvCdsHWXUFF0LotiXrBRr45AoEie2bASNSMmCZbQh-_Pq7gdhKOZMhBTErrk-aEOZrmsUG0sL2ZcVLdZ0_U-23ysR2GVpNg8jyv1HLZaPw5IJC4XucRw5r-5UiIcIIdxbUNphamPgq1cqL3QP_UsCGotCIUQTDNMbXB7-J_opBM2uGFp-cW95-Wq7qg"
        max_age = 120
        expected_auth_time = MOCKED_CLOCK + DEFAULT_LEEWAY + max_age
        mocked_clock = expected_auth_time + 1

        self.assert_fails_with_error(token, "Authentication Time (auth_time) claim in the ID token indicates that too much time has passed since the last end-user authentication. Current time ({}) is after last auth at ({})".format(mocked_clock, expected_auth_time), max_age=max_age, clock=mocked_clock)

    def test_passes_when_org_present_but_not_required(self):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhdXRoMHxzZGs0NThma3MiLCJhdWQiOiJ0b2tlbnMtdGVzdC0xMjMiLCJvcmdfaWQiOiJvcmdfMTIzIiwiaXNzIjoiaHR0cHM6Ly90b2tlbnMtdGVzdC5hdXRoMC5jb20vIiwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjF9.hjSPgJpg0Dn2z0giCdGqVLD5Kmqy_yMYlSkgwKD7ahQ"
        sv = SymmetricSignatureVerifier(HMAC_SHARED_SECRET)
        tv = TokenVerifier(
            signature_verifier=sv,
            issuer=expectations['issuer'],
            audience=expectations['audience']
        )
        tv._clock = MOCKED_CLOCK
        tv.verify(token)

    def test_passes_when_org_present_and_matches(self):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhdXRoMHxzZGs0NThma3MiLCJhdWQiOiJ0b2tlbnMtdGVzdC0xMjMiLCJvcmdfaWQiOiJvcmdfMTIzIiwiaXNzIjoiaHR0cHM6Ly90b2tlbnMtdGVzdC5hdXRoMC5jb20vIiwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjF9.hjSPgJpg0Dn2z0giCdGqVLD5Kmqy_yMYlSkgwKD7ahQ"
        sv = SymmetricSignatureVerifier(HMAC_SHARED_SECRET)
        tv = TokenVerifier(
            signature_verifier=sv,
            issuer=expectations['issuer'],
            audience=expectations['audience']
        )
        tv._clock = MOCKED_CLOCK
        tv.verify(token, organization='org_123')    

    def test_fails_when_org_specified_but_not_present(self):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhdXRoMHxzZGs0NThma3MiLCJhdWQiOiJ0b2tlbnMtdGVzdC0xMjMiLCJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJleHAiOjE1ODc3NjUzNjEsImlhdCI6MTU4NzU5MjU2MX0.wotJnUdD5IfdZMewF_-BnHc0pI56uwzwr5qaSXvSu9w"
        self.assert_fails_with_error(token, "Organization (org_id) claim must be a string present in the ID token", signature_verifier=SymmetricSignatureVerifier(HMAC_SHARED_SECRET), organization='org_123')

    def test_fails_when_org_specified_but_not_(self):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhdXRoMHxzZGs0NThma3MiLCJhdWQiOiJ0b2tlbnMtdGVzdC0xMjMiLCJvcmdfaWQiOjQyLCJpc3MiOiJodHRwczovL3Rva2Vucy10ZXN0LmF1dGgwLmNvbS8iLCJleHAiOjE1ODc3NjUzNjEsImlhdCI6MTU4NzU5MjU2MX0.fGL1_akaHikdovS7NRYla3flne1xdtCjP0ei_CRxO6k"
        self.assert_fails_with_error(token, "Organization (org_id) claim must be a string present in the ID token", signature_verifier=SymmetricSignatureVerifier(HMAC_SHARED_SECRET), organization='org_123')

    def test_fails_when_org_specified_but_does_not_match(self):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhdXRoMHxzZGs0NThma3MiLCJhdWQiOiJ0b2tlbnMtdGVzdC0xMjMiLCJvcmdfaWQiOiJvcmdfMTIzIiwiaXNzIjoiaHR0cHM6Ly90b2tlbnMtdGVzdC5hdXRoMC5jb20vIiwiZXhwIjoxNTg3NzY1MzYxLCJpYXQiOjE1ODc1OTI1NjF9.hjSPgJpg0Dn2z0giCdGqVLD5Kmqy_yMYlSkgwKD7ahQ"
        self.assert_fails_with_error(token, 'Organization (org_id) claim mismatch in the ID token; expected "org_abc", found "org_123"', signature_verifier=SymmetricSignatureVerifier(HMAC_SHARED_SECRET), organization='org_abc')