from .conftest import get_client, verify_request_count


def test_attackProtection_breachedPasswordDetection_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "attack_protection.breached_password_detection.get.0"
    client = get_client(test_id)
    client.attack_protection.breached_password_detection.get()
    verify_request_count(test_id, "GET", "/attack-protection/breached-password-detection", None, 1)


def test_attackProtection_breachedPasswordDetection_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "attack_protection.breached_password_detection.update.0"
    client = get_client(test_id)
    client.attack_protection.breached_password_detection.update()
    verify_request_count(test_id, "PATCH", "/attack-protection/breached-password-detection", None, 1)
