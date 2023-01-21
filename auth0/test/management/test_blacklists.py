import unittest
from unittest import mock

from ...management.blacklists import Blacklists


class TestBlacklists(unittest.TestCase):
    def test_init_with_optionals(self):
        t = Blacklists(
            domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2)
        )
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.blacklists.RestClient")
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        t = Blacklists(domain="domain", token="jwttoken")
        t.get(aud="an-id")

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/blacklists/tokens", params={"aud": "an-id"}
        )

    @mock.patch("auth0.management.blacklists.RestClient")
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        t = Blacklists(domain="domain", token="jwttoken")

        # create without audience
        t.create(jti="the-jti")

        args, kwargs = mock_instance.post.call_args

        self.assertEqual("https://domain/api/v2/blacklists/tokens", args[0])
        self.assertEqual(kwargs["data"], {"jti": "the-jti"})

        # create with audience
        t.create(jti="the-jti", aud="the-aud")

        args, kwargs = mock_instance.post.call_args

        self.assertEqual("https://domain/api/v2/blacklists/tokens", args[0])
        self.assertEqual(kwargs["data"], {"jti": "the-jti", "aud": "the-aud"})
