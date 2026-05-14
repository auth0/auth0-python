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
    def test_all(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = SelfServiceProfiles(domain="domain", token="jwttoken")
        s.all()

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/self-service-profiles",
            params={"page": 0, "per_page": 25, "include_totals": "true"},
        )

        s.all(page=1, per_page=50, include_totals=False)

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/self-service-profiles",
            params={"page": 1, "per_page": 50, "include_totals": "false"},
        )

    @mock.patch("auth0.management.self_service_profiles.RestClient")
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = SelfServiceProfiles(domain="domain", token="jwttoken")
        s.create({"name": "test"})

        mock_instance.post.assert_called_with(
            "https://domain/api/v2/self-service-profiles", data={"name": "test"}
        )

    @mock.patch("auth0.management.self_service_profiles.RestClient")
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = SelfServiceProfiles(domain="domain", token="jwttoken")
        s.get("an-id")

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/self-service-profiles/an-id"
        )

    @mock.patch("auth0.management.self_service_profiles.RestClient")
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = SelfServiceProfiles(domain="domain", token="jwttoken")
        s.delete("an-id")

        mock_instance.delete.assert_called_with(
            "https://domain/api/v2/self-service-profiles/an-id"
        )

    @mock.patch("auth0.management.self_service_profiles.RestClient")
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = SelfServiceProfiles(domain="domain", token="jwttoken")
        s.update("an-id", {"a": "b", "c": "d"})

        mock_instance.patch.assert_called_with(
            "https://domain/api/v2/self-service-profiles/an-id",
            data={"a": "b", "c": "d"},
        )

    @mock.patch("auth0.management.self_service_profiles.RestClient")
    def test_get_custom_text(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = SelfServiceProfiles(domain="domain", token="jwttoken")
        s.get_custom_text("an-id", "en", "page")

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/self-service-profiles/an-id/custom-text/en/page"
        )

    @mock.patch("auth0.management.self_service_profiles.RestClient")
    def test_update_custom_text(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = SelfServiceProfiles(domain="domain", token="jwttoken")
        s.update_custom_text("an-id", "en", "page", {"a": "b", "c": "d"})

        mock_instance.put.assert_called_with(
            "https://domain/api/v2/self-service-profiles/an-id/custom-text/en/page",
            data={"a": "b", "c": "d"},
        )

    @mock.patch("auth0.management.self_service_profiles.RestClient")
    def test_create_sso_ticket(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = SelfServiceProfiles(domain="domain", token="jwttoken")
        s.create_sso_ticket("an-id", {"a": "b", "c": "d"})

        mock_instance.post.assert_called_with(
            "https://domain/api/v2/self-service-profiles/an-id/sso-ticket",
            data={"a": "b", "c": "d"},
        )

    @mock.patch("auth0.management.self_service_profiles.RestClient")
    def test_revoke_sso_ticket(self, mock_rc):
        mock_instance = mock_rc.return_value

        s = SelfServiceProfiles(domain="domain", token="jwttoken")
        s.revoke_sso_ticket("an-id", "ticket-id")

        mock_instance.post.assert_called_with(
            "https://domain/api/v2/self-service-profiles/an-id/sso-ticket/ticket-id/revoke"
        )