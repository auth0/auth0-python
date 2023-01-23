import unittest
from unittest import mock

from ...management.users_by_email import UsersByEmail


class TestUsersByEmail(unittest.TestCase):
    def test_init_with_optionals(self):
        t = UsersByEmail(
            domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2)
        )
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.users_by_email.RestClient")
    def test_search_users_by_email(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = UsersByEmail(domain="domain", token="jwttoken")
        u.search_users_by_email("A@B.com")

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/users-by-email", args[0])
        self.assertEqual(
            kwargs["params"],
            {"email": "A@B.com", "fields": None, "include_fields": "true"},
        )

        u.search_users_by_email(
            email="a@b.com", fields=["a", "b"], include_fields=False
        )

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/users-by-email", args[0])
        self.assertEqual(
            kwargs["params"],
            {"email": "a@b.com", "fields": "a,b", "include_fields": "false"},
        )
