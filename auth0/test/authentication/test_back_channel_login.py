
import unittest
from unittest import mock
import json

import requests
from ...exceptions import Auth0Error, RateLimitError

from ...authentication.back_channel_login import BackChannelLogin

class TestBackChannelLogin(unittest.TestCase):
    @mock.patch("auth0.rest.RestClient.post")
    def test_ciba(self, mock_post):
        g = BackChannelLogin("my.domain.com", "cid", client_secret="clsec")

        g.back_channel_login(
            binding_message="This is a binding message",
            login_hint="{ \"format\": \"iss_sub\", \"iss\": \"https://my.domain.auth0.com/\", \"sub\": \"auth0|[USER ID]\" }",
            scope="openid",
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/bc-authorize")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "clsec",
                "binding_message": "This is a binding message",
                "login_hint": "{ \"format\": \"iss_sub\", \"iss\": \"https://my.domain.auth0.com/\", \"sub\": \"auth0|[USER ID]\" }",
                "scope": "openid",
            },
        )

    @mock.patch("requests.request")
    def test_server_error(self, mock_requests_request):
        response = requests.Response()
        response.status_code = 400
        response._content = b'{"error":"foo"}'
        mock_requests_request.return_value = response

        g = BackChannelLogin("my.domain.com", "cid", client_secret="clsec")
        with self.assertRaises(Auth0Error) as context:
            g.back_channel_login(
                binding_message="msg",
                login_hint="hint",
                scope="openid"
            )
        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.message, 'foo')

    @mock.patch("auth0.rest.RestClient.post")
    def test_should_require_binding_message(self, mock_post):
        g = BackChannelLogin("my.domain.com", "cid", client_secret="clsec")

        # Expecting an exception to be raised when binding_message is missing
        with self.assertRaises(Exception) as context:
            g.back_channel_login(
                login_hint='{ "format": "iss_sub", "iss": "https://my.domain.auth0.com/", "sub": "auth0|USER_ID" }',
                scope="openid",
            )

        # Assert the error message is correct
        self.assertIn("missing 1 required positional argument: \'binding_message\'", str(context.exception))

    @mock.patch("auth0.rest.RestClient.post")
    def test_should_require_login_hint(self, mock_post):
        g = BackChannelLogin("my.domain.com", "cid", client_secret="clsec")

        # Expecting an exception to be raised when login_hint is missing
        with self.assertRaises(Exception) as context:
            g.back_channel_login(
                binding_message="This is a binding message.",
                scope="openid",
            )

        # Assert the error message is correct
        self.assertIn("missing 1 required positional argument: \'login_hint\'", str(context.exception))
    
    @mock.patch("auth0.rest.RestClient.post")
    def test_should_require_scope(self, mock_post):
        g = BackChannelLogin("my.domain.com", "cid", client_secret="clsec")

        # Expecting an exception to be raised when scope is missing
        with self.assertRaises(Exception) as context:
            g.back_channel_login(
                binding_message="This is a binding message.",
                login_hint='{ "format": "iss_sub", "iss": "https://my.domain.auth0.com/", "sub": "auth0|USER_ID" }',
            )

        # Assert the error message is correct
        self.assertIn("missing 1 required positional argument: \'scope\'", str(context.exception))

    @mock.patch("auth0.rest.RestClient.post")
    def test_with_authorization_details(self, mock_post):
        g = BackChannelLogin("my.domain.com", "cid", client_secret="clsec")
        g.back_channel_login(
            binding_message="This is a binding message.",
            login_hint= json.dumps({"format": "iss_sub", "iss": "https://my.domain.auth0.com/", "sub": "auth0|USER_ID"}),
            scope="openid",
            authorization_details=[
                {
                    "type":"payment_initiation","locations":["https://example.com/payments"],
                    "instructedAmount":
                    {
                        "currency":"EUR","amount":"123.50"
                    },
                    "creditorName":"Merchant A",
                    "creditorAccount":
                    {
                        "bic":"ABCIDEFFXXX",
                        "iban":"DE021001001093071118603"
                    },
                    "remittanceInformationUnstructured":"Ref Number Merchant"
                }
            ],
        )

        args, kwargs = mock_post.call_args

        expected_data = {
            "client_id": "cid",
            "client_secret": "clsec",
            "binding_message": "This is a binding message.",
            "login_hint": json.dumps({"format": "iss_sub", "iss": "https://my.domain.auth0.com/", "sub": "auth0|USER_ID"}),
            "scope": "openid",
            "authorization_details": json.dumps([
                {
                    "type":"payment_initiation","locations":["https://example.com/payments"],
                    "instructedAmount":
                    {
                        "currency":"EUR","amount":"123.50"
                    },
                    "creditorName":"Merchant A",
                    "creditorAccount":
                    {
                        "bic":"ABCIDEFFXXX",
                        "iban":"DE021001001093071118603"
                    },
                    "remittanceInformationUnstructured":"Ref Number Merchant"
                }
            ]),
        }

        actual_data = kwargs["data"]

        self.assertEqual(args[0], "https://my.domain.com/bc-authorize")

        self.assertEqual(
            actual_data,
            expected_data,
            "Request data does not match expected data after JSON serialization."
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_with_request_expiry(self, mock_post):
        g = BackChannelLogin("my.domain.com", "cid", client_secret="clsec")

        g.back_channel_login(
            binding_message="This is a binding message",
            login_hint="{ \"format\": \"iss_sub\", \"iss\": \"https://my.domain.auth0.com/\", \"sub\": \"auth0|[USER ID]\" }",
            scope="openid",
            requested_expiry=100
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/bc-authorize")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "clsec",
                "binding_message": "This is a binding message",
                "login_hint": "{ \"format\": \"iss_sub\", \"iss\": \"https://my.domain.auth0.com/\", \"sub\": \"auth0|[USER ID]\" }",
                "scope": "openid",
                "requested_expiry": "100",
            },
        )

    def test_requested_expiry_negative_raises(self):
        g = BackChannelLogin("my.domain.com", "cid", client_secret="clsec")
        with self.assertRaises(ValueError):
            g.back_channel_login(
                binding_message="msg",
                login_hint="hint",
                scope="openid",
                requested_expiry=-10
            )

    def test_requested_expiry_zero_raises(self):
        g = BackChannelLogin("my.domain.com", "cid", client_secret="clsec")
        with self.assertRaises(ValueError):
            g.back_channel_login(
                binding_message="msg",
                login_hint="hint",
                scope="openid",
                requested_expiry=0
            )

    def test_requested_non_int_raises(self):
        g = BackChannelLogin("my.domain.com", "cid", client_secret="clsec")
        with self.assertRaises(ValueError):
            g.back_channel_login(
                binding_message="msg",
                login_hint="hint",
                scope="openid",
                requested_expiry="string_instead_of_int"
            )
