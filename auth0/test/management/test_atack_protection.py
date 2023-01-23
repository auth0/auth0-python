import unittest
from unittest import mock

from ...management.attack_protection import AttackProtection


class TestAttackProtection(unittest.TestCase):
    def test_init_with_optionals(self):
        t = AttackProtection(
            domain="domain", token="jwttoken", telemetry=False, timeout=(10, 2)
        )
        self.assertEqual(t.client.options.timeout, (10, 2))
        telemetry_header = t.client.base_headers.get("Auth0-Client", None)
        self.assertEqual(telemetry_header, None)

    @mock.patch("auth0.management.attack_protection.RestClient")
    def test_get_breached_password_detection(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.get.return_value = {}

        ap = AttackProtection(domain="domain", token="jwttoken")
        ap.get_breached_password_detection()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual(
            "https://domain/api/v2/attack-protection/breached-password-detection",
            args[0],
        )

    @mock.patch("auth0.management.attack_protection.RestClient")
    def test_update_breached_password_detection(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.patch.return_value = {}

        c = AttackProtection(domain="domain", token="jwttoken")
        c.update_breached_password_detection({"a": "b", "c": "d"})

        mock_instance.patch.assert_called_with(
            "https://domain/api/v2/attack-protection/breached-password-detection",
            data={"a": "b", "c": "d"},
        )

    @mock.patch("auth0.management.attack_protection.RestClient")
    def test_get_brute_force_protection(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.get.return_value = {}

        ap = AttackProtection(domain="domain", token="jwttoken")
        ap.get_brute_force_protection()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual(
            "https://domain/api/v2/attack-protection/brute-force-protection", args[0]
        )

    @mock.patch("auth0.management.attack_protection.RestClient")
    def test_update_brute_force_protection(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.patch.return_value = {}

        c = AttackProtection(domain="domain", token="jwttoken")
        c.update_brute_force_protection({"a": "b", "c": "d"})

        mock_instance.patch.assert_called_with(
            "https://domain/api/v2/attack-protection/brute-force-protection",
            data={"a": "b", "c": "d"},
        )

    @mock.patch("auth0.management.attack_protection.RestClient")
    def test_get_suspicious_ip_throttling(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.get.return_value = {}

        ap = AttackProtection(domain="domain", token="jwttoken")
        ap.get_suspicious_ip_throttling()

        args, kwargs = mock_instance.get.call_args

        self.assertEqual(
            "https://domain/api/v2/attack-protection/suspicious-ip-throttling", args[0]
        )

    @mock.patch("auth0.management.attack_protection.RestClient")
    def test_update_suspicious_ip_throttling(self, mock_rc):
        mock_instance = mock_rc.return_value
        mock_instance.patch.return_value = {}

        c = AttackProtection(domain="domain", token="jwttoken")
        c.update_suspicious_ip_throttling({"a": "b", "c": "d"})

        mock_instance.patch.assert_called_with(
            "https://domain/api/v2/attack-protection/suspicious-ip-throttling",
            data={"a": "b", "c": "d"},
        )
