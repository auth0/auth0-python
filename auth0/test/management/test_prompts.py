import unittest
from unittest import mock

from ...management.prompts import Prompts


class TestPrompts(unittest.TestCase):
    def test_init_with_optionals(self):
        t = Prompts(domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.prompts.RestClient")
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        p = Prompts(domain="domain", token="jwttoken")
        p.get()

        args, _ = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/prompts", args[0])

    @mock.patch("auth0.management.prompts.RestClient")
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        p = Prompts(domain="domain", token="jwttoken")
        p.update({"a": "b", "c": "d"})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual("https://domain/api/v2/prompts", args[0])
        self.assertEqual(kwargs["data"], {"a": "b", "c": "d"})

    @mock.patch("auth0.management.prompts.RestClient")
    def test_get_custom_text(self, mock_rc):
        mock_instance = mock_rc.return_value

        p = Prompts(domain="domain", token="jwttoken")
        p.get_custom_text("some-prompt", "some-language")

        args, _ = mock_instance.get.call_args

        self.assertEqual(
            "https://domain/api/v2/prompts/some-prompt/custom-text/some-language",
            args[0],
        )

    @mock.patch("auth0.management.prompts.RestClient")
    def test_update_custom_text(self, mock_rc):
        mock_instance = mock_rc.return_value

        p = Prompts(domain="domain", token="jwttoken")
        p.update_custom_text("some-prompt", "some-language", {"a": "b", "c": "d"})

        args, kwargs = mock_instance.put.call_args

        self.assertEqual(
            "https://domain/api/v2/prompts/some-prompt/custom-text/some-language",
            args[0],
        )
        self.assertEqual(kwargs["data"], {"a": "b", "c": "d"})
