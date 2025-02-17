import unittest
from unittest import mock

from ...management.users import Sessions


class TestUsers(unittest.TestCase):
    def test_init_with_optionals(self):
        t = Sessions(domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.users.RestClient")
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Sessions(domain="domain", token="jwttoken")
        u.get("user_id")

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/sessions/session_id"
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Sessions(domain="domain", token="jwttoken")
        u.delete("session_id")

        mock_instance.delete.assert_called_with(
            "https://domain/api/v2/sessions/session_id"
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_revoke(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Sessions(domain="domain", token="jwttoken")
        u.revoke("session_id")

        mock_instance.post.assert_called_with(
            "https://domain/api/v2/sessions/session_id/sessions"
        )
