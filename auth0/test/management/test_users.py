import unittest
from unittest import mock

from ...management.users import Users


class TestUsers(unittest.TestCase):
    def test_init_with_optionals(self):
        t = Users(domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.users.RestClient")
    def test_list(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.list()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/users", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "per_page": 25,
                "page": 0,
                "include_totals": "true",
                "sort": None,
                "connection": None,
                "fields": None,
                "include_fields": "true",
                "q": None,
                "search_engine": None,
            },
        )

        u.list(
            page=1,
            per_page=50,
            sort="s",
            connection="con",
            q="q",
            search_engine="se",
            include_totals=False,
            fields=["a", "b"],
            include_fields=False,
        )

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/users", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "per_page": 50,
                "page": 1,
                "include_totals": "false",
                "sort": "s",
                "connection": "con",
                "fields": "a,b",
                "include_fields": "false",
                "q": "q",
                "search_engine": "se",
            },
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.create({"a": "b", "c": "d"})

        args, kwargs = mock_instance.post.call_args

        self.assertEqual("https://domain/api/v2/users", args[0])
        self.assertEqual(kwargs["data"], {"a": "b", "c": "d"})

    @mock.patch("auth0.management.users.RestClient")
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.get("an-id")

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/users/an-id", args[0])
        self.assertEqual(kwargs["params"], {"fields": None, "include_fields": "true"})

        u.get("an-id", fields=["a", "b"], include_fields=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/users/an-id", args[0])
        self.assertEqual(kwargs["params"], {"fields": "a,b", "include_fields": "false"})

    @mock.patch("auth0.management.users.RestClient")
    def test_delete(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.delete("an-id")

        mock_instance.delete.assert_called_with("https://domain/api/v2/users/an-id")

    @mock.patch("auth0.management.users.RestClient")
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.update("an-id", {"a": "b", "c": "d"})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual("https://domain/api/v2/users/an-id", args[0])
        self.assertEqual(kwargs["data"], {"a": "b", "c": "d"})

    @mock.patch("auth0.management.users.RestClient")
    def test_list_organizations(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.list_organizations("an-id")

        args, kwargs = mock_instance.get.call_args
        self.assertEqual("https://domain/api/v2/users/an-id/organizations", args[0])
        self.assertEqual(
            kwargs["params"], {"per_page": 25, "page": 0, "include_totals": "true"}
        )

        u.list_organizations(id="an-id", page=1, per_page=50, include_totals=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/users/an-id/organizations", args[0])
        self.assertEqual(
            kwargs["params"], {"per_page": 50, "page": 1, "include_totals": "false"}
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_list_roles(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.list_roles("an-id")

        args, kwargs = mock_instance.get.call_args
        self.assertEqual("https://domain/api/v2/users/an-id/roles", args[0])
        self.assertEqual(
            kwargs["params"], {"per_page": 25, "page": 0, "include_totals": "true"}
        )

        u.list_roles(id="an-id", page=1, per_page=50, include_totals=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/users/an-id/roles", args[0])
        self.assertEqual(
            kwargs["params"], {"per_page": 50, "page": 1, "include_totals": "false"}
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_remove_roles(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.remove_roles("an-id", ["a", "b"])

        args, kwargs = mock_instance.delete.call_args

        self.assertEqual("https://domain/api/v2/users/an-id/roles", args[0])
        self.assertEqual(kwargs["data"], {"roles": ["a", "b"]})

    @mock.patch("auth0.management.users.RestClient")
    def test_add_roles(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.add_roles("an-id", ["a", "b"])

        args, kwargs = mock_instance.post.call_args

        self.assertEqual("https://domain/api/v2/users/an-id/roles", args[0])
        self.assertEqual(kwargs["data"], {"roles": ["a", "b"]})

    @mock.patch("auth0.management.users.RestClient")
    def test_list_permissions(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.list_permissions("an-id")

        args, kwargs = mock_instance.get.call_args
        self.assertEqual("https://domain/api/v2/users/an-id/permissions", args[0])
        self.assertEqual(
            kwargs["params"], {"per_page": 25, "page": 0, "include_totals": "true"}
        )

        u.list_permissions(id="an-id", page=1, per_page=50, include_totals=False)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/users/an-id/permissions", args[0])
        self.assertEqual(
            kwargs["params"], {"per_page": 50, "page": 1, "include_totals": "false"}
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_remove_permissions(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.remove_permissions("an-id", ["a", "b"])

        args, kwargs = mock_instance.delete.call_args

        self.assertEqual("https://domain/api/v2/users/an-id/permissions", args[0])
        self.assertEqual(kwargs["data"], {"permissions": ["a", "b"]})

    @mock.patch("auth0.management.users.RestClient")
    def test_add_permissions(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.add_permissions("an-id", ["a", "b"])

        args, kwargs = mock_instance.post.call_args

        self.assertEqual("https://domain/api/v2/users/an-id/permissions", args[0])
        self.assertEqual(kwargs["data"], {"permissions": ["a", "b"]})

    @mock.patch("auth0.management.users.RestClient")
    def test_delete_multifactor(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.delete_multifactor("an-id", "provider")

        mock_instance.delete.assert_called_with(
            "https://domain/api/v2/users/an-id/multifactor/provider"
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_delete_authenticators(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.delete_authenticators("an-id")

        mock_instance.delete.assert_called_with(
            "https://domain/api/v2/users/an-id/authenticators"
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_unlink_user_account(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.unlink_user_account("an-id", "provider", "user-id")

        mock_instance.delete.assert_called_with(
            "https://domain/api/v2/users/an-id/identities/provider/user-id"
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_link_user_account(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.link_user_account("user-id", {"a": "b", "c": "d"})

        args, kwargs = mock_instance.post.call_args

        self.assertEqual("https://domain/api/v2/users/user-id/identities", args[0])
        self.assertEqual(kwargs["data"], {"a": "b", "c": "d"})

    @mock.patch("auth0.management.users.RestClient")
    def test_regenerate_recovery_code(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.regenerate_recovery_code("user-id")

        mock_instance.post.assert_called_with(
            "https://domain/api/v2/users/user-id/recovery-code-regeneration"
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_get_guardian_enrollments(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.get_guardian_enrollments("user-id")

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/users/user-id/enrollments"
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_get_log_events(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.get_log_events("used_id")

        args, kwargs = mock_instance.get.call_args
        self.assertEqual("https://domain/api/v2/users/used_id/logs", args[0])
        self.assertEqual(kwargs["params"]["page"], 0)
        self.assertEqual(kwargs["params"]["per_page"], 50)
        self.assertIsNone(kwargs["params"]["sort"])
        self.assertEqual(kwargs["params"]["include_totals"], "false")

    @mock.patch("auth0.management.users.RestClient")
    def test_invalidate_remembered_browsers(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.invalidate_remembered_browsers("user-id")

        args, kwargs = mock_instance.post.call_args
        self.assertEqual(
            "https://domain/api/v2/users/user-id/multifactor/actions/invalidate-remember-browser",
            args[0],
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_get_authentication_methods(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.get_authentication_methods("user_id")

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/users/user_id/authentication-methods"
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_get_authentication_method_by_id(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.get_authentication_method_by_id("user_id", "authentication_method_id")

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/users/user_id/authentication-methods/authentication_method_id"
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_create_authentication_method(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.create_authentication_method("user_id", {})

        mock_instance.post.assert_called_with(
            "https://domain/api/v2/users/user_id/authentication-methods", data={}
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_update_authentication_methods(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.update_authentication_methods("user_id", {})

        mock_instance.put.assert_called_with(
            "https://domain/api/v2/users/user_id/authentication-methods", data={}
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_update_authentication_method_by_id(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.update_authentication_method_by_id("user_id", "authentication_method_id", {})

        mock_instance.patch.assert_called_with(
            "https://domain/api/v2/users/user_id/authentication-methods/authentication_method_id",
            data={},
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_delete_authentication_methods(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.delete_authentication_methods("user_id")

        mock_instance.delete.assert_called_with(
            "https://domain/api/v2/users/user_id/authentication-methods"
        )

    @mock.patch("auth0.management.users.RestClient")
    def test_delete_authentication_method_by_id(self, mock_rc):
        mock_instance = mock_rc.return_value

        u = Users(domain="domain", token="jwttoken")
        u.delete_authentication_method_by_id("user_id", "authentication_method_id")

        mock_instance.delete.assert_called_with(
            "https://domain/api/v2/users/user_id/authentication-methods/authentication_method_id"
        )
