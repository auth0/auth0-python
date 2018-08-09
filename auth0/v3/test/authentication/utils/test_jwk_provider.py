import unittest
import mock
from ....authentication.utils.jwk_provider import UrlJwkProvider
from ....exceptions import JwkProviderError

MY_JWK = {
        "kty": "RSA",
        "e": "AQAB",
        "use": "sig",
        "kid": "my_key-id",
        "alg": "RS256",
        "n": "nnlbiOVZs6zsLQ9pjP5jfkoEfh3RYGpGifV3LaijDc-Q5VhT4EUt30HpBX4A7SgyW7tkyHi4HMdEaAjAsqHe3XK4cRE3hOTQi89B03WCZPrC8eILYdK81F4qfe_346E7v1_83K3lz_o6s_c16iJRxLhLtFZjUTwWSCFR7QKxB4IeiwzP1UcktzjMDLumlU5CKgbXOjo4ECUScWl_ObMAMNDgi03FHwXWnTqwxfAFFDfq_c6P-RcuXXv5FGVUwNtTKb4cHZMZFXMstzRmqfGCjuY7RRs38UrLF_BEzuc2ygOi2aV-IAYxgesnzfFQAR9Q2vVzZKRr0gs2778Epq78mQ"
        }
OTHER_JWK = {
    "kty": "RSA",
    "e": "AQAB",
    "use": "sig",
    "kid": "other_key-id",
    "alg": "RS256",
    "n": "iaRryrqYg_8Kkha2d4Qzo5AMAoveIqCfqNAxxT1CZaoFHJSxShKBr-2J6SbH_O5B3TD5ap0ol46sXCivMSmNsiLiqggxI4lDREL5tB_nHTFoWfWtGGUllh_GPPZCL9rN43wc-_EFggb2XHakalJsu1UQcyTGR2Mb1TMYn0mVeKjcvTl4mcc0-PdKGn8IvxWM0U3xO1-Oy1NhnUJMVaThQEui6lSbvGdIcSkEyrR8fzmn9uHcXIgEnqRtCa5GhUJ_Wg7J-aVzexW8Wq-W8UrIEM0qfS1o1s0hzoP745n_5SZM7uqKp_Rpjk932IMJTCYi7SmXhUhPEv-qiEgXl3Eg2w"
    }

class TestJwkProvider(unittest.TestCase):

    @mock.patch('requests.get')
    def test_call_once_the_right_url(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {"keys": [MY_JWK, OTHER_JWK]}
        mock_get.return_value = mock_response
        provider = UrlJwkProvider('lucho.auth0.com')

        provider.get_jwk('my_key-id')
        provider.get_jwk('my_key-id')
        provider.get_jwk('my_key-id')

        jwks_url = 'https://lucho.auth0.com/.well-known/jwks.json'
        mock_get.assert_called_once_with(jwks_url)

    @mock.patch('requests.get')
    def test_gets_many_jwk(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {"keys": [MY_JWK, OTHER_JWK]}
        mock_get.return_value = mock_response
        provider = UrlJwkProvider('lucho.auth0.com')

        myJwk = provider.get_jwk('my_key-id')
        self.assertEqual(myJwk, MY_JWK)
        otherJwk = provider.get_jwk('other_key-id')
        self.assertEqual(otherJwk, OTHER_JWK)

    @mock.patch('requests.get')
    def test_get_jwk_without_key_id(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {"keys": [OTHER_JWK]}
        mock_get.return_value = mock_response
        provider = UrlJwkProvider('lucho.auth0.com')

        otherJwk = provider.get_jwk()
        self.assertEqual(otherJwk, OTHER_JWK)

    @mock.patch('requests.get')
    def test_fails_to_get_jwk_when_key_id_does_not_match(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {"keys": [MY_JWK, OTHER_JWK]}
        mock_get.return_value = mock_response
        provider = UrlJwkProvider('lucho.auth0.com')
        self.assertRaises(JwkProviderError, provider.get_jwk, 'inexisting_key-id')

    @mock.patch('requests.get')
    def test_fails_to_get_jwk_when_jwks_is_empty(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {"keys": []}
        mock_get.return_value = mock_response
        provider = UrlJwkProvider('lucho.auth0.com')
        self.assertRaises(JwkProviderError, provider.get_jwk, 'inexisting_key-id')


