import unittest
import mock
import time
import sys
from ....authentication.utils.token_verifier import TokenVerifier
from ....exceptions import TokenVerificationError
from jose import jwt

KEY_PAIR_RS256 = {
    "kty": "RSA",
    "d": "MZG54l192ZJMJbAMj2her8xoOtpCoLfTOKYucbwL1FAGK-bhvxPWwbWVG4LDlnQcj7-xEniAADx8tX4iLylgmzuJyOT2ahj9oOGWjO3hhrz0kiVdmRd5NUdlJhFtLERKrPNOx1aS_0v_eIs8NIpoen7rpkcbqayK7tJDvk1Qw8pLWHgcRJVHfnQ1VL2PUV8QBkExSc7Ivd7KuoawqdLe9TANA93Yf-GqGqN2_8kdDHHEC8d3UN6-b6MhoDbgT4prGK6coIqEHaNXdLMuDVEJXg9fjNe1vU1N5K8B29qcoHq_kmKpobMZptSAq-8fqCJOdJqmbq6tBQGLZHDtAnd5YQ",
    "e": "AQAB",
    "use": "sig",
    "kid": "my_key-id",
    "alg": "RS256",
    "n": "lnRr_NzQLzytSml_8jXaKCiAUr0Z1aGTf04lRmh-6dnOD4U8fXU1d19nrxdq0MLbh05zXPi50dx9akQA6psr-F3Fb28Po5vuGHZFaZ7a9-t08HeylYssERSEMNSxJwAtWl467uVHrmrJU09yGhE6M38TshDoAyHqgkpkjDNlyYDqIg6QzM1nd3H_IlW1HYjldMP35O5y3wbaXsAcPPNpw8YPtaC2VPfMF4Qhz5eeR7sjpbyd1WcXvDWY9pbM0ZxMkpixzyLRDuhCY87DW_HfG-DolxfK6g-1uDvGN5fwp-g4sJYE2qgIyUdwRTzg5i5_ubvw9tPKo0sbcSslVOD94Q"
    }
PUBLIC_KEY_RS256 = {
    "kty": "RSA",
    "e": "AQAB",
    "use": "sig",
    "kid": "my_key-id",
    "alg": "RS256",
    "n": "lnRr_NzQLzytSml_8jXaKCiAUr0Z1aGTf04lRmh-6dnOD4U8fXU1d19nrxdq0MLbh05zXPi50dx9akQA6psr-F3Fb28Po5vuGHZFaZ7a9-t08HeylYssERSEMNSxJwAtWl467uVHrmrJU09yGhE6M38TshDoAyHqgkpkjDNlyYDqIg6QzM1nd3H_IlW1HYjldMP35O5y3wbaXsAcPPNpw8YPtaC2VPfMF4Qhz5eeR7sjpbyd1WcXvDWY9pbM0ZxMkpixzyLRDuhCY87DW_HfG-DolxfK6g-1uDvGN5fwp-g4sJYE2qgIyUdwRTzg5i5_ubvw9tPKo0sbcSslVOD94Q"
    }
OTHER_KEY_PAIR_RS256 = {
  "kty": "RSA",
  "d": "Ew_P5dCIkKctJWJkNNRojUlD7xORGsLNx0xiUHinXELqT9vnAuPvV5pq-AEnBV-_Zu9MeRykMLn7TXQ4EYSM9SAWdWs3vWF0gEymw1OwIotTJZsl-VdK5VSKUemqbJP5RtS56qV0LicQJpOGxanpIft1B7UYby4GFBkF7LdVKezZUqncBIvkMw06hg8P-IV6I01ZhuGXdajrVgsW1EHom-925MlxuxC0F_YHV3VG-kctYQ9ATuFwAW5eG-DIX_OyS2Iqw_9g_VhWXOgC7cJIW1iHjbdNGMgqBQQllP3vlD4k7XneXtVisI5IxMpXWQp-LymijJS0AfMvSQRN8Hb3gQ",
  "e": "AQAB",
  "use": "sig",
  "kid": "my_key-id",
  "alg": "RS256",
  "n": "nnlbiOVZs6zsLQ9pjP5jfkoEfh3RYGpGifV3LaijDc-Q5VhT4EUt30HpBX4A7SgyW7tkyHi4HMdEaAjAsqHe3XK4cRE3hOTQi89B03WCZPrC8eILYdK81F4qfe_346E7v1_83K3lz_o6s_c16iJRxLhLtFZjUTwWSCFR7QKxB4IeiwzP1UcktzjMDLumlU5CKgbXOjo4ECUScWl_ObMAMNDgi03FHwXWnTqwxfAFFDfq_c6P-RcuXXv5FGVUwNtTKb4cHZMZFXMstzRmqfGCjuY7RRs38UrLF_BEzuc2ygOi2aV-IAYxgesnzfFQAR9Q2vVzZKRr0gs2778Epq78mQ"
}

def date_now():
    if sys.version_info[0] < 3:
        return long(time.time())
    return int(time.time())

def generate_signed_rs256_jwt(issuer='lucho987', audience='https://lucho.auth0.com/', expires_in=date_now()+3600, not_before=date_now()-3600, key=KEY_PAIR_RS256):
    header = {
        'typ': 'JWT',
        'alg': 'RS256',
        'kid': 'my_key-id'
        }
    payload = {
        'aud': [audience],
        'iss': issuer,
        'exp': expires_in,
        'nbf': not_before
        }
    return jwt.encode(claims=payload, headers=header, key=key, algorithm='RS256')


class TestTokenVerifier(unittest.TestCase):

    @mock.patch('auth0.v3.authentication.utils.jwk_provider.UrlJwkProvider')
    def test_skips_verification_for_hs256_tokens(self, mock_jwk_provider):
        verifier = TokenVerifier(mock_jwk_provider)
        mock_jwk_provider.get_jwk.return_value = PUBLIC_KEY_RS256
        hs256_signed_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJsdWNobzk4NyIsImlzcyI6WyJodHRwczovL2x1Y2hvLmF1dGgwLmNvbS8iXX0.rMl5ozrAQQcKHSRtifW02rIyYd4AjPOLVbkDHog0Lww'
        try:
            verifier.verify(
                hs256_signed_token,
                'https://lucho.auth0.com/',
                'lucho987'
                )
            #Verify should return inmediately when the algorithm is HS256
            #If an exception is raised this test case will fail
        except:
            self.fail("Verification shouldn't be performed for HS256 signed tokens")
        mock_jwk_provider.assert_not_called()

    @mock.patch('auth0.v3.authentication.utils.jwk_provider.UrlJwkProvider')
    def test_fails_verification_with_invalid_audience(self, mock_jwk_provider):
        verifier = TokenVerifier(mock_jwk_provider)
        mock_jwk_provider.get_jwk.return_value = PUBLIC_KEY_RS256
        invalid_audience_token = generate_signed_rs256_jwt(audience='https://someone.auth0.com/')
        self.assertRaises(TokenVerificationError, verifier.verify,
            invalid_audience_token, 'lucho987', 'https://lucho.auth0.com/'
            )
        mock_jwk_provider.get_jwk.assert_called_once_with('my_key-id')
        
    @mock.patch('auth0.v3.authentication.utils.jwk_provider.UrlJwkProvider')
    def test_fails_verification_with_invalid_issuer(self, mock_jwk_provider):
        verifier = TokenVerifier(mock_jwk_provider)
        mock_jwk_provider.get_jwk.return_value = PUBLIC_KEY_RS256
        invalid_issuer_token = generate_signed_rs256_jwt(issuer='user123')
        self.assertRaises(TokenVerificationError, verifier.verify,
            invalid_issuer_token, 'lucho987', 'https://lucho.auth0.com/'
            )
        mock_jwk_provider.get_jwk.assert_called_once_with('my_key-id')

    @mock.patch('auth0.v3.authentication.utils.jwk_provider.UrlJwkProvider')
    def test_fails_verification_when_expired(self, mock_jwk_provider):
        verifier = TokenVerifier(mock_jwk_provider)
        mock_jwk_provider.get_jwk.return_value = PUBLIC_KEY_RS256
        expired_token = generate_signed_rs256_jwt(expires_in=date_now()-100)
        self.assertRaises(TokenVerificationError, verifier.verify,
            expired_token, 'lucho987', 'https://lucho.auth0.com/'
            )
        mock_jwk_provider.get_jwk.assert_called_once_with('my_key-id')

    @mock.patch('auth0.v3.authentication.utils.jwk_provider.UrlJwkProvider')
    def test_fails_verification_with_invalid_signature(self, mock_jwk_provider):
        verifier = TokenVerifier(mock_jwk_provider)
        mock_jwk_provider.get_jwk.return_value = PUBLIC_KEY_RS256
        other_signature_token = generate_signed_rs256_jwt(key=OTHER_KEY_PAIR_RS256)
        self.assertRaises(TokenVerificationError, verifier.verify,
            other_signature_token, 'lucho987', 'https://lucho.auth0.com/'
            )
        mock_jwk_provider.get_jwk.assert_called_once_with('my_key-id')

    @mock.patch('auth0.v3.authentication.utils.jwk_provider.UrlJwkProvider')
    def test_verifies_token_signature(self, mock_jwk_provider):
        verifier = TokenVerifier(mock_jwk_provider)
        mock_jwk_provider.get_jwk.return_value = PUBLIC_KEY_RS256
        good_token = generate_signed_rs256_jwt()
        try:
            verifier.verify(good_token, 'lucho987', 'https://lucho.auth0.com/')
            mock_jwk_provider.get_jwk.assert_called_once_with('my_key-id')
        except:
            self.fail("Failed to verify a good RS256 token")