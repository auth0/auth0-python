import base64
import json
import sys
import unittest
from unittest import mock

import requests

from ...authentication.base import AuthenticationBase
from ...exceptions import Auth0Error, RateLimitError


class TestBase(unittest.TestCase):
    def test_telemetry_enabled_by_default(self):
        ab = AuthenticationBase("auth0.com", "cid")
        base_headers = ab.client.base_headers

        user_agent = base_headers["User-Agent"]
        auth0_client_bytes = base64.b64decode(base_headers["Auth0-Client"])
        auth0_client_json = auth0_client_bytes.decode("utf-8")
        auth0_client = json.loads(auth0_client_json)
        content_type = base_headers["Content-Type"]

        from auth0 import __version__ as auth0_version

        python_version = "{}.{}.{}".format(
            sys.version_info.major, sys.version_info.minor, sys.version_info.micro
        )

        client_info = {
            "name": "auth0-python",
            "version": auth0_version,
            "env": {"python": python_version},
        }

        self.assertEqual(user_agent, f"Python/{python_version}")
        self.assertEqual(auth0_client, client_info)
        self.assertEqual(content_type, "application/json")

    def test_telemetry_disabled(self):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False)

        self.assertEqual(ab.client.base_headers, {"Content-Type": "application/json"})

    @mock.patch("requests.request")
    def test_post(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False, timeout=(10, 2))

        mock_request.return_value.status_code = 200
        mock_request.return_value.text = '{"x": "y"}'

        data = ab.post("the-url", data={"a": "b"}, headers={"c": "d"})

        mock_request.assert_called_with(
            "POST",
            "the-url",
            json={"a": "b"},
            headers={"c": "d", "Content-Type": "application/json"},
            timeout=(10, 2),
        )

        self.assertEqual(data, {"x": "y"})

    @mock.patch("requests.request")
    def test_post_with_defaults(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False)

        mock_request.return_value.status_code = 200
        mock_request.return_value.text = '{"x": "y"}'

        # Only required params are passed
        data = ab.post("the-url")

        mock_request.assert_called_with(
            "POST",
            "the-url",
            headers={"Content-Type": "application/json"},
            timeout=5.0,
        )

        self.assertEqual(data, {"x": "y"})

    @mock.patch("requests.request")
    def test_post_includes_telemetry(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid")

        mock_request.return_value.status_code = 200
        mock_request.return_value.text = '{"x": "y"}'

        data = ab.post("the-url", data={"a": "b"}, headers={"c": "d"})

        self.assertEqual(mock_request.call_count, 1)
        call_args, call_kwargs = mock_request.call_args
        self.assertEqual(call_args[0], "POST")
        self.assertEqual(call_args[1], "the-url")
        self.assertEqual(call_kwargs["json"], {"a": "b"})
        headers = call_kwargs["headers"]
        self.assertEqual(headers["c"], "d")
        self.assertEqual(headers["Content-Type"], "application/json")
        self.assertIn("User-Agent", headers)
        self.assertIn("Auth0-Client", headers)

        self.assertEqual(data, {"x": "y"})

    @mock.patch("requests.request")
    def test_post_error(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False)

        for error_status in [400, 500, None]:
            mock_request.return_value.status_code = error_status
            mock_request.return_value.text = (
                '{"error": "e0","error_description": "desc"}'
            )

            with self.assertRaises(Auth0Error) as context:
                ab.post("the-url", data={"a": "b"}, headers={"c": "d"})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, "e0")
            self.assertEqual(context.exception.message, "desc")

    @mock.patch("requests.request")
    def test_post_error_mfa_required(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False)

        mock_request.return_value.status_code = 403
        mock_request.return_value.text = '{"error": "mfa_required", "error_description": "Multifactor authentication required", "mfa_token": "Fe26...Ha"}'

        with self.assertRaises(Auth0Error) as context:
            ab.post("the-url", data={"a": "b"}, headers={"c": "d"})

        self.assertEqual(context.exception.status_code, 403)
        self.assertEqual(context.exception.error_code, "mfa_required")
        self.assertEqual(
            context.exception.message, "Multifactor authentication required"
        )
        self.assertEqual(context.exception.content.get("mfa_token"), "Fe26...Ha")

    @mock.patch("requests.request")
    def test_post_rate_limit_error(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False)

        mock_request.return_value.text = (
            '{"statusCode": 429, "error": "e0", "error_description": "desc"}'
        )
        mock_request.return_value.status_code = 429
        mock_request.return_value.headers = {
            "x-ratelimit-limit": "3",
            "x-ratelimit-remaining": "6",
            "x-ratelimit-reset": "9",
        }

        with self.assertRaises(Auth0Error) as context:
            ab.post("the-url", data={"a": "b"}, headers={"c": "d"})

        self.assertEqual(context.exception.status_code, 429)
        self.assertEqual(context.exception.error_code, "e0")
        self.assertEqual(context.exception.message, "desc")
        self.assertIsInstance(context.exception, RateLimitError)
        self.assertEqual(context.exception.reset_at, 9)

    @mock.patch("requests.request")
    def test_post_rate_limit_error_without_headers(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False)

        mock_request.return_value.text = (
            '{"statusCode": 429, "error": "e0", "error_description": "desc"}'
        )
        mock_request.return_value.status_code = 429
        mock_request.return_value.headers = {}

        with self.assertRaises(Auth0Error) as context:
            ab.post("the-url", data={"a": "b"}, headers={"c": "d"})

        self.assertEqual(context.exception.status_code, 429)
        self.assertEqual(context.exception.error_code, "e0")
        self.assertEqual(context.exception.message, "desc")
        self.assertIsInstance(context.exception, RateLimitError)
        self.assertEqual(context.exception.reset_at, -1)

    @mock.patch("requests.request")
    def test_post_error_with_code_property(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False)

        for error_status in [400, 500, None]:
            mock_request.return_value.status_code = error_status
            mock_request.return_value.text = (
                '{"code": "e0","error_description": "desc"}'
            )

            with self.assertRaises(Auth0Error) as context:
                ab.post("the-url", data={"a": "b"}, headers={"c": "d"})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, "e0")
            self.assertEqual(context.exception.message, "desc")

    @mock.patch("requests.request")
    def test_post_error_with_no_error_code(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False)

        for error_status in [400, 500, None]:
            mock_request.return_value.status_code = error_status
            mock_request.return_value.text = '{"error_description": "desc"}'

            with self.assertRaises(Auth0Error) as context:
                ab.post("the-url", data={"a": "b"}, headers={"c": "d"})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, "a0.sdk.internal.unknown")
            self.assertEqual(context.exception.message, "desc")

    @mock.patch("requests.request")
    def test_post_error_with_text_response(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False)

        for error_status in [400, 500, None]:
            mock_request.return_value.status_code = error_status
            mock_request.return_value.text = "there has been a terrible error"

            with self.assertRaises(Auth0Error) as context:
                ab.post("the-url", data={"a": "b"}, headers={"c": "d"})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, "a0.sdk.internal.unknown")
            self.assertEqual(
                context.exception.message, "there has been a terrible error"
            )

    @mock.patch("requests.request")
    def test_post_error_with_no_response_text(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False)

        for error_status in [400, 500, None]:
            mock_request.return_value.status_code = error_status
            mock_request.return_value.text = None

            with self.assertRaises(Auth0Error) as context:
                ab.post("the-url", data={"a": "b"}, headers={"c": "d"})

            self.assertEqual(context.exception.status_code, error_status)
            self.assertEqual(context.exception.error_code, "a0.sdk.internal.unknown")
            self.assertEqual(context.exception.message, "")

    @mock.patch("requests.request")
    def test_get(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False, timeout=(10, 2))

        mock_request.return_value.status_code = 200
        mock_request.return_value.text = '{"x": "y"}'

        data = ab.get("the-url", params={"a": "b"}, headers={"c": "d"})

        mock_request.assert_called_with(
            "GET",
            "the-url",
            params={"a": "b"},
            headers={"c": "d", "Content-Type": "application/json"},
            timeout=(10, 2),
        )

        self.assertEqual(data, {"x": "y"})

    @mock.patch("requests.request")
    def test_get_with_defaults(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid", telemetry=False)

        mock_request.return_value.status_code = 200
        mock_request.return_value.text = '{"x": "y"}'

        # Only required params are passed
        data = ab.get("the-url")

        mock_request.assert_called_with(
            "GET",
            "the-url",
            headers={"Content-Type": "application/json"},
            timeout=5.0,
        )

        self.assertEqual(data, {"x": "y"})

    @mock.patch("requests.request")
    def test_get_includes_telemetry(self, mock_request):
        ab = AuthenticationBase("auth0.com", "cid")

        mock_request.return_value.status_code = 200
        mock_request.return_value.text = '{"x": "y"}'

        data = ab.get("the-url", params={"a": "b"}, headers={"c": "d"})

        self.assertEqual(mock_request.call_count, 1)
        call_args, call_kwargs = mock_request.call_args
        self.assertEqual(call_args[0], "GET")
        self.assertEqual(call_args[1], "the-url")
        self.assertEqual(call_kwargs["params"], {"a": "b"})
        headers = call_kwargs["headers"]
        self.assertEqual(headers["c"], "d")
        self.assertEqual(headers["Content-Type"], "application/json")
        self.assertIn("User-Agent", headers)
        self.assertIn("Auth0-Client", headers)

        self.assertEqual(data, {"x": "y"})

    # TODO: Replace the following with more reliable tests. Failing on GitHub Actions.

    # def test_get_can_timeout(self):
    #     ab = AuthenticationBase("auth0.com", "cid", timeout=0.00002)

    #     with self.assertRaises(requests.exceptions.Timeout):
    #         ab.get("https://google.com", params={"a": "b"}, headers={"c": "d"})

    # def test_post_can_timeout(self):
    #     ab = AuthenticationBase("auth0.com", "cid", timeout=0.00002)

    #     with self.assertRaises(requests.exceptions.Timeout):
    #         ab.post("https://google.com", data={"a": "b"}, headers={"c": "d"})
