import unittest

import mock

from ...management.branding import Branding


class TestBranding(unittest.TestCase):
    def test_init_with_optionals(self):
        branding = Branding(
            domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2)
        )
        self.assertEqual(branding.client.options.timeout, (10, 2))

        telemetry = branding.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry, None)

    @mock.patch("auth0.v3.management.branding.RestClient")
    def test_get(self, mock_rc):
        api = mock_rc.return_value

        branding = Branding(domain="domain", token="jwttoken")
        branding.get()

        api.get.assert_called_with(
            "https://domain/api/v2/branding",
        )

    @mock.patch("auth0.v3.management.branding.RestClient")
    def test_update(self, mock_rc):
        api = mock_rc.return_value
        api.patch.return_value = {}

        branding = Branding(domain="domain", token="jwttoken")
        branding.update({"a": "b", "c": "d"})

        api.patch.assert_called_with(
            "https://domain/api/v2/branding", data={"a": "b", "c": "d"}
        )

    @mock.patch("auth0.v3.management.branding.RestClient")
    def test_get_template_universal_login(self, mock_rc):
        api = mock_rc.return_value

        branding = Branding(domain="domain", token="jwttoken")
        branding.get_template_universal_login()

        api.get.assert_called_with(
            "https://domain/api/v2/branding/templates/universal-login",
        )

    @mock.patch("auth0.v3.management.branding.RestClient")
    def test_delete_template_universal_login(self, mock_rc):
        api = mock_rc.return_value

        branding = Branding(domain="domain", token="jwttoken")
        branding.delete_template_universal_login()

        api.delete.assert_called_with(
            "https://domain/api/v2/branding/templates/universal-login",
        )

    @mock.patch("auth0.v3.management.branding.RestClient")
    def test_update_template_universal_login(self, mock_rc):
        api = mock_rc.return_value
        api.put.return_value = {}

        branding = Branding(domain="domain", token="jwttoken")
        branding.update_template_universal_login({"a": "b", "c": "d"})

        api.put.assert_called_with(
            "https://domain/api/v2/branding/templates/universal-login",
            type="put_universal-login_body",
            body={"template": {"a": "b", "c": "d"}},
        )
