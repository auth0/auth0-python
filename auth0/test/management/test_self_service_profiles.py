import unittest
from unittest import mock

from ...management.self_service_profiles import SelfServiceProfiles


class TestSelfServiceProfiles(unittest.TestCase):
    def test_init_with_optionals(self):
        t = SelfServiceProfiles(
            domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2)
        )
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.self_service_profiles.RestClient")
    def test_list(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = SelfServiceProfiles(domain="domain", token="jwttoken")
        s.list()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual(args[0], "https://domain/api/v2/self-service-profiles")
        self.assertEqual(
            kwargs["params"], {"page": 0, "per_page": 25, "include_totals": "true"}
        )

        s.list(page=1, per_page=50, include_totals=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual(args[0], "https://domain/api/v2/self-service-profiles")
        self.assertEqual(
            kwargs["params"], {"page": 1, "per_page": 50, "include_totals": "false"}
        )
