import unittest
from unittest import mock

from ...management.actions import Actions


class TestActions(unittest.TestCase):
    def test_init_with_optionals(self):
        t = Actions(domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2))
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.actions.RestClient")
    def test_get_actions(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")

        c.get_actions()
        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/actions/actions", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "triggerId": None,
                "actionName": None,
                "deployed": None,
                "installed": "false",
                "page": None,
                "per_page": None,
            },
        )

        c.get_actions("trigger-id", "action-name", True, True, 0, 5)
        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/actions/actions", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "triggerId": "trigger-id",
                "actionName": "action-name",
                "deployed": "true",
                "installed": "true",
                "page": 0,
                "per_page": 5,
            },
        )

        c.get_actions("trigger-id", "action-name", False, True, 0, 5)
        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/actions/actions", args[0])
        self.assertEqual(
            kwargs["params"],
            {
                "triggerId": "trigger-id",
                "actionName": "action-name",
                "deployed": "false",
                "installed": "true",
                "page": 0,
                "per_page": 5,
            },
        )

    @mock.patch("auth0.management.actions.RestClient")
    def test_create_action(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")
        c.create_action({"a": "b", "c": "d"})

        mock_instance.post.assert_called_with(
            "https://domain/api/v2/actions/actions", data={"a": "b", "c": "d"}
        )

    @mock.patch("auth0.management.actions.RestClient")
    def test_update_action(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")
        c.update_action("action-id", {"a": "b", "c": "d"})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual("https://domain/api/v2/actions/actions/action-id", args[0])
        self.assertEqual(kwargs["data"], {"a": "b", "c": "d"})

    @mock.patch("auth0.management.actions.RestClient")
    def test_get_action(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")
        c.get_action("action-id")

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/actions/actions/action-id", args[0])
        self.assertEqual(kwargs["params"], {})

    @mock.patch("auth0.management.actions.RestClient")
    def test_get_triggers(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")
        c.get_triggers()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual("https://domain/api/v2/actions/triggers", args[0])
        self.assertEqual(kwargs["params"], {})

    @mock.patch("auth0.management.actions.RestClient")
    def test_delete_action(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")
        c.delete_action("action-id")

        args, kwargs = mock_instance.delete.call_args

        self.assertEqual("https://domain/api/v2/actions/actions/action-id", args[0])
        self.assertEqual(kwargs["params"], {"force": "false"})

        c.delete_action("action-id", True)

        args, kwargs = mock_instance.delete.call_args

        self.assertEqual("https://domain/api/v2/actions/actions/action-id", args[0])
        self.assertEqual(kwargs["params"], {"force": "true"})

    @mock.patch("auth0.management.actions.RestClient")
    def test_get_execution(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")
        c.get_execution("execution-id")

        args, kwargs = mock_instance.get.call_args

        self.assertEqual(
            "https://domain/api/v2/actions/executions/execution-id", args[0]
        )
        self.assertEqual(kwargs["params"], {})

    @mock.patch("auth0.management.actions.RestClient")
    def test_get_action_versions(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")
        c.get_action_versions("action-id")

        args, kwargs = mock_instance.get.call_args

        self.assertEqual(
            "https://domain/api/v2/actions/actions/action-id/versions", args[0]
        )
        self.assertEqual(kwargs["params"], {"page": None, "per_page": None})

        c.get_action_versions("action-id", 0, 5)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual(
            "https://domain/api/v2/actions/actions/action-id/versions", args[0]
        )
        self.assertEqual(kwargs["params"], {"page": 0, "per_page": 5})

    @mock.patch("auth0.management.actions.RestClient")
    def test_get_trigger_bindings(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")
        c.get_trigger_bindings("trigger-id")

        args, kwargs = mock_instance.get.call_args

        self.assertEqual(
            "https://domain/api/v2/actions/triggers/trigger-id/bindings", args[0]
        )
        self.assertEqual(kwargs["params"], {"page": None, "per_page": None})

        c.get_trigger_bindings("trigger-id", 0, 5)

        args, kwargs = mock_instance.get.call_args

        self.assertEqual(
            "https://domain/api/v2/actions/triggers/trigger-id/bindings", args[0]
        )
        self.assertEqual(kwargs["params"], {"page": 0, "per_page": 5})

    @mock.patch("auth0.management.actions.RestClient")
    def test_get_action_version(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")
        c.get_action_version("action-id", "version-id")

        args, kwargs = mock_instance.get.call_args

        self.assertEqual(
            "https://domain/api/v2/actions/actions/action-id/versions/version-id",
            args[0],
        )
        self.assertEqual(kwargs["params"], {})

    @mock.patch("auth0.management.actions.RestClient")
    def test_deploy_action(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")
        c.deploy_action("action-id")

        args, kwargs = mock_instance.post.call_args

        self.assertEqual(
            "https://domain/api/v2/actions/actions/action-id/deploy", args[0]
        )

    @mock.patch("auth0.management.actions.RestClient")
    def test_rollback_action(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")
        c.rollback_action_version("action-id", "version-id")

        args, kwargs = mock_instance.post.call_args

        self.assertEqual(
            "https://domain/api/v2/actions/actions/action-id/versions/version-id/deploy",
            args[0],
        )
        self.assertEqual(kwargs["data"], {})

    @mock.patch("auth0.management.actions.RestClient")
    def test_update_trigger_bindings(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = Actions(domain="domain", token="jwttoken")
        c.update_trigger_bindings("trigger-id", {"a": "b", "c": "d"})

        args, kwargs = mock_instance.patch.call_args

        self.assertEqual(
            "https://domain/api/v2/actions/triggers/trigger-id/bindings", args[0]
        )
        self.assertEqual(kwargs["data"], {"a": "b", "c": "d"})
