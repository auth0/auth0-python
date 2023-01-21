import unittest
from unittest import mock

from ...management.email_templates import EmailTemplates


class TestClients(unittest.TestCase):
    def test_init_with_optionals(self):
        t = EmailTemplates(
            domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2)
        )
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.email_templates.RestClient")
    def test_create(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = EmailTemplates(domain="domain", token="jwttoken")
        c.create({"a": "b", "c": "d"})

        mock_instance.post.assert_called_with(
            "https://domain/api/v2/email-templates", data={"a": "b", "c": "d"}
        )

    @mock.patch("auth0.management.email_templates.RestClient")
    def test_get(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = EmailTemplates(domain="domain", token="jwttoken")
        c.get("this-template-name")

        mock_instance.get.assert_called_with(
            "https://domain/api/v2/email-templates/this-template-name"
        )

    @mock.patch("auth0.management.email_templates.RestClient")
    def test_update(self, mock_rc):
        mock_instance = mock_rc.return_value

        c = EmailTemplates(domain="domain", token="jwttoken")
        c.update("this-template-name", {"a": "b", "c": "d"})

        mock_instance.patch.assert_called_with(
            "https://domain/api/v2/email-templates/this-template-name",
            data={"a": "b", "c": "d"},
        )
