import unittest
from unittest import mock

from ...authentication.pushed_authorization_requests import PushedAuthorizationRequests


class TestRevokeToken(unittest.TestCase):
    @mock.patch("auth0.rest.RestClient.post")
    def test_par(self, mock_post):
        a = PushedAuthorizationRequests("my.domain.com", "cid", client_secret="sh!")
        a.pushed_authorization_request(
            response_type="code", redirect_uri="https://example.com/callback"
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/par")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "sh!",
                "response_type": "code",
                "redirect_uri": "https://example.com/callback",
            },
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_par_custom_params(self, mock_post):
        a = PushedAuthorizationRequests("my.domain.com", "cid", client_secret="sh!")
        a.pushed_authorization_request(
            response_type="code", redirect_uri="https://example.com/callback", foo="bar"
        )

        args, kwargs = mock_post.call_args

        self.assertEqual(args[0], "https://my.domain.com/oauth/par")
        self.assertEqual(
            kwargs["data"],
            {
                "client_id": "cid",
                "client_secret": "sh!",
                "response_type": "code",
                "redirect_uri": "https://example.com/callback",
                "foo": "bar",
            },
        )
