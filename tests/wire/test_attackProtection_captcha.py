from .conftest import get_client, verify_request_count


def test_attackProtection_captcha_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "attack_protection.captcha.get.0"
    client = get_client(test_id)
    client.attack_protection.captcha.get()
    verify_request_count(test_id, "GET", "/attack-protection/captcha", None, 1)


def test_attackProtection_captcha_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "attack_protection.captcha.update.0"
    client = get_client(test_id)
    client.attack_protection.captcha.update()
    verify_request_count(test_id, "PATCH", "/attack-protection/captcha", None, 1)
