import unittest
from fnmatch import fnmatch
from unittest import mock
from unittest.mock import ANY

from cryptography.hazmat.primitives import asymmetric, serialization

from ...authentication.get_token import GetToken


def get_private_key():
    private_key = asymmetric.rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )


class TestGetToken(unittest.TestCase):
    @mock.patch("auth0.rest.RestClient.post")
    def test_authorization_code(self, mock_post):
        g = GetToken("my.domain.com", "cid", client_secret="clsec")

        g.authorization_code(
            code="cd",
            grant_type="gt",
            redirect_uri="idt",
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "clsec",
                "code": "cd",
                "grant_type": "gt",
                "redirect_uri": "idt",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_authorization_code_with_client_assertion(self, mock_post):
        g = GetToken(
            "my.domain.com", "cid", client_assertion_signing_key=get_private_key()
        )

        g.authorization_code(code="cd", grant_type="gt", redirect_uri="idt")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_assertion": ANY,
                "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
                "code": "cd",
                "grant_type": "gt",
                "redirect_uri": "idt",
            },
        )

        self.assertTrue(fnmatch(kwargs["data"]["client_assertion"], "*.*.*"))

    @mock.patch("auth0.rest.RestClient.post")
    def test_authorization_code_pkce(self, mock_post):
        g = GetToken("my.domain.com", "cid")

        g.authorization_code_pkce(
            code_verifier="cdver",
            code="cd",
            grant_type="gt",
            redirect_uri="idt",
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "code_verifier": "cdver",
                "code": "cd",
                "grant_type": "gt",
                "redirect_uri": "idt",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_client_credentials(self, mock_post):
        g = GetToken("my.domain.com", "cid", client_secret="clsec")

        g.client_credentials(audience="aud", grant_type="gt")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "clsec",
                "audience": "aud",
                "grant_type": "gt",
                "organization": None,
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_client_credentials_with_client_assertion(self, mock_post):
        g = GetToken(
            "my.domain.com", "cid", client_assertion_signing_key=get_private_key()
        )

        g.client_credentials("aud", grant_type="gt")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_assertion": ANY,
                "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
                "audience": "aud",
                "grant_type": "gt",
                "organization": None,
            },
        )

        self.assertTrue(fnmatch(kwargs["data"]["client_assertion"], "*.*.*"))

    @mock.patch("auth0.rest.RestClient.post")
    def test_client_credentials_with_organization(self, mock_post):
        g = GetToken("my.domain.com", "cid", client_secret="clsec")

        g.client_credentials("aud", organization="my-org")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "grant_type": "client_credentials",
                "client_secret": "clsec",
                "audience": "aud",
                "organization": "my-org",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_login(self, mock_post):
        g = GetToken("my.domain.com", "cid", client_secret="clsec")

        g.login(
            username="usrnm",
            password="pswd",
            scope="http://test.com/api",
            realm="rlm",
            audience="aud",
            grant_type="gt",
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "clsec",
                "username": "usrnm",
                "password": "pswd",
                "scope": "http://test.com/api",
                "realm": "rlm",
                "audience": "aud",
                "grant_type": "gt",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_login_simple(self, mock_post):
        g = GetToken("my.domain.com", "cid", client_secret="clsec")

        g.login(
            username="usrnm",
            password="pswd",
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "clsec",
                "username": "usrnm",
                "password": "pswd",
                "realm": None,
                "scope": None,
                "audience": None,
                "grant_type": "http://auth0.com/oauth/grant-type/password-realm",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_login_with_forwarded_for(self, mock_post):
        g = GetToken("my.domain.com", "cid", client_secret="clsec")

        g.login(username="usrnm", password="pswd", forwarded_for="192.168.0.1")

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["headers"],
            {
                "auth0-forwarded-for": "192.168.0.1",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_refresh_token(self, mock_post):
        g = GetToken("my.domain.com", "cid", client_secret="clsec")

        g.refresh_token(
            refresh_token="rt",
            grant_type="gt",
            scope="s",
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "clsec",
                "refresh_token": "rt",
                "grant_type": "gt",
                "scope": "s",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_passwordless_login_with_sms(self, mock_post):
        g = GetToken("my.domain.com", "cid", client_secret="csec")

        g.passwordless_login(
            username="123456",
            otp="abcd",
            realm="sms",
            audience="aud",
            scope="openid",
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "csec",
                "realm": "sms",
                "grant_type": "http://auth0.com/oauth/grant-type/passwordless/otp",
                "username": "123456",
                "otp": "abcd",
                "audience": "aud",
                "scope": "openid",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_passwordless_login_with_email(self, mock_post):
        g = GetToken("my.domain.com", "cid", client_secret="csec")

        g.passwordless_login(
            username="a@b.c",
            otp="abcd",
            realm="email",
            audience="aud",
            scope="openid",
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "csec",
                "realm": "email",
                "grant_type": "http://auth0.com/oauth/grant-type/passwordless/otp",
                "username": "a@b.c",
                "otp": "abcd",
                "audience": "aud",
                "scope": "openid",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_backchannel_login(self, mock_post):
        g = GetToken("my.domain.com", "cid", client_secret="csec")

        g.backchannel_login(
            auth_req_id="reqid",
            grant_type="urn:openid:params:grant-type:ciba",
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "csec",
                "auth_req_id": "reqid",
                "grant_type": "urn:openid:params:grant-type:ciba",
            },
        )
        
    @mock.patch("auth0.rest.RestClient.post")
    def test_connection_login(self, mock_post):
        g = GetToken("my.domain.com", "cid", client_secret="csec")

        g.access_token_for_connection(
            grant_type="urn:auth0:params:oauth:grant-type:token-exchange:federated-connection-access-token",
            subject_token_type="urn:ietf:params:oauth:token-type:refresh_token",
            subject_token="refid",
            requested_token_type="http://auth0.com/oauth/token-type/federated-connection-access-token",
            connection="google-oauth2"
        )

        args, kwargs = mock_post.call_args

        print(kwargs["data"])

        self.assertEqual(args[0], "https://my.domain.com/oauth/token")
        self.assertEqual(
            kwargs["data"],
            {
                "grant_type": "urn:auth0:params:oauth:grant-type:token-exchange:federated-connection-access-token",
                "client_id": "cid",
                "client_secret": "csec",
                "subject_token_type": "urn:ietf:params:oauth:token-type:refresh_token",
                "subject_token": "refid",
                "requested_token_type": "http://auth0.com/oauth/token-type/federated-connection-access-token",
                "connection": "google-oauth2"
            },
        )