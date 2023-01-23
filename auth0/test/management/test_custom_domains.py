import unittest
from unittest import mock

from ...management.custom_domains import CustomDomains


class TestCustomDomains(unittest.TestCase):
    def test_init_with_optionals(self):
        t = CustomDomains(
            domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2)
        )
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.custom_domains.RestClient")
    def test_get_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = CustomDomains(domain="domain", token="jwttoken")
        g.all()

        mock_instance.get.assert_called_with("https://domain/api/v2/custom-domains")

    @mock.patch("auth0.management.custom_domains.RestClient")
    def test_create_new(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = CustomDomains(domain="domain", token="jwttoken")
        g.create_new(body={"a": "b", "c": "d", "e": "f"})

        args, kwargs = mock_instance.post.call_args

        self.assertEqual("https://domain/api/v2/custom-domains", args[0])
        self.assertEqual(kwargs["data"], {"a": "b", "c": "d", "e": "f"})

    @mock.patch("auth0.management.custom_domains.RestClient")
    def test_get_domain_by_id(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = CustomDomains(domain="domain", token="jwttoken")
        g.get("an-id")

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/custom-domains/an-id"
        )

    @mock.patch("auth0.management.custom_domains.RestClient")
    def test_verify(self, mock_rc):
        mock_instance = mock_rc.return_value

        g = CustomDomains(domain="domain", token="jwttoken")
        g.verify("an-id")

        args, kwargs = mock_instance.post.call_args

        self.assertEqual("https://domain/api/v2/custom-domains/an-id/verify", args[0])
