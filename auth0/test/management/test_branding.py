import unittest
from unittest import mock

from ...management.branding import Branding


class TestBranding(unittest.TestCase):
    def test_init_with_optionals(self):
        branding = Branding(
            domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2)
        )
        self.assertEqual(branding.client.options.timeout, (10, 2))

        telemetry = branding.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry, None)

    @mock.patch("auth0.management.branding.RestClient")
    def test_get(self, mock_rc):
        api = mock_rc.return_value

        branding = Branding(domain="domain", token="jwttoken")
        branding.get()

        api.get.assert_called_with(
            "https://domain/api/v2/branding",
        )

    @mock.patch("auth0.management.branding.RestClient")
    def test_update(self, mock_rc):
        api = mock_rc.return_value
        api.patch.return_value = {}

        branding = Branding(domain="domain", token="jwttoken")
        branding.update({"a": "b", "c": "d"})

        api.patch.assert_called_with(
            "https://domain/api/v2/branding", data={"a": "b", "c": "d"}
        )

    @mock.patch("auth0.management.branding.RestClient")
    def test_get_template_universal_login(self, mock_rc):
        api = mock_rc.return_value

        branding = Branding(domain="domain", token="jwttoken")
        branding.get_template_universal_login()

        api.get.assert_called_with(
            "https://domain/api/v2/branding/templates/universal-login",
        )

    @mock.patch("auth0.management.branding.RestClient")
    def test_delete_template_universal_login(self, mock_rc):
        api = mock_rc.return_value

        branding = Branding(domain="domain", token="jwttoken")
        branding.delete_template_universal_login()

        api.delete.assert_called_with(
            "https://domain/api/v2/branding/templates/universal-login",
        )

    @mock.patch("auth0.rest.requests.request")
    def test_update_template_universal_login(self, mock_rc):
        mock_rc.return_value.status_code = 200
        mock_rc.return_value.text = "{}"

        branding = Branding(domain="domain", token="jwttoken")
        branding.update_template_universal_login({"a": "b", "c": "d"})

        mock_rc.assert_called_with(
            "PUT",
            "https://domain/api/v2/branding/templates/universal-login",
            json={"template": {"a": "b", "c": "d"}},
            headers=mock.ANY,
            timeout=5.0,
        )

    @mock.patch("auth0.management.branding.RestClient")
    def test_get_default_branding_theme(self, mock_rc):
        api = mock_rc.return_value
        api.get.return_value = {}

        branding = Branding(domain="domain", token="jwttoken")
        branding.get_default_branding_theme()

        api.get.assert_called_with(
            "https://domain/api/v2/branding/themes/default",
        )

    @mock.patch("auth0.management.branding.RestClient")
    def test_get_branding_theme(self, mock_rc):
        api = mock_rc.return_value
        api.get.return_value = {}

        branding = Branding(domain="domain", token="jwttoken")
        branding.get_branding_theme("theme_id")

        api.get.assert_called_with(
            "https://domain/api/v2/branding/themes/theme_id",
        )

    @mock.patch("auth0.management.branding.RestClient")
    def test_delete_branding_theme(self, mock_rc):
        api = mock_rc.return_value
        api.delete.return_value = {}

        branding = Branding(domain="domain", token="jwttoken")
        branding.delete_branding_theme("theme_id")

        api.delete.assert_called_with(
            "https://domain/api/v2/branding/themes/theme_id",
        )

    @mock.patch("auth0.management.branding.RestClient")
    def test_update_branding_theme(self, mock_rc):
        api = mock_rc.return_value
        api.patch.return_value = {}

        branding = Branding(domain="domain", token="jwttoken")
        branding.update_branding_theme("theme_id", {})

        api.patch.assert_called_with(
            "https://domain/api/v2/branding/themes/theme_id",
            data={},
        )

    @mock.patch("auth0.management.branding.RestClient")
    def test_create_branding_theme(self, mock_rc):
        api = mock_rc.return_value
        api.post.return_value = {}

        branding = Branding(domain="domain", token="jwttoken")
        branding.create_branding_theme({})

        api.post.assert_called_with(
            "https://domain/api/v2/branding/themes",
            data={},
        )
