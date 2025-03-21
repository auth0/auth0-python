import unittest
import json
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

    @mock.patch("auth0.rest.RestClient.post")
    def test_with_authorization_details(self, mock_post):
        a = PushedAuthorizationRequests("my.domain.com", "cid", client_secret="sh!")
        a.pushed_authorization_request(
            response_type="code", 
            redirect_uri="https://example.com/callback", 
            authorization_details=[{"type": "money_transfer", "instructedAmount": {"amount": 2500, "currency": "USD"}}],
        )

        args, kwargs = mock_post.call_args

        expected_data = {
            "client_id": "cid",
            "client_secret": "sh!",
            "response_type": "code",
            "redirect_uri": "https://example.com/callback",
            "authorization_details": [{"type": "money_transfer", "instructedAmount": {"amount": 2500, "currency": "USD"}}],
        }

        actual_data = kwargs["data"]
        
        self.assertEqual(args[0], "https://my.domain.com/oauth/par")
   
        self.assertEqual(
            json.dumps(actual_data, sort_keys=True), 
            json.dumps(expected_data, sort_keys=True)
        )

    @mock.patch("auth0.rest.RestClient.post")
    def test_jar(self, mock_post):
        a = PushedAuthorizationRequests("my.domain.com", "cid", client_secret="sh!")
        a.pushed_authorization_request(
            response_type="code", 
            redirect_uri="https://example.com/callback", 
            request="my-jwt-request",
        )

        args, kwargs = mock_post.call_args

        expected_data = {
            "client_id": "cid",
            "client_secret": "sh!",
            "response_type": "code",
            "redirect_uri": "https://example.com/callback",
            "request": 'my-jwt-request',
        }

        actual_data = kwargs["data"]
        
        self.assertEqual(args[0], "https://my.domain.com/oauth/par")
   
        self.assertEqual(
            json.dumps(actual_data, sort_keys=True), 
            json.dumps(expected_data, sort_keys=True)
        )