
import unittest
from unittest import mock

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



