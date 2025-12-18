from .conftest import get_client, verify_request_count


def test_attackProtection_botDetection_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "attack_protection.bot_detection.get.0"
    client = get_client(test_id)
    client.attack_protection.bot_detection.get()
    verify_request_count(test_id, "GET", "/attack-protection/bot-detection", None, 1)


def test_attackProtection_botDetection_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "attack_protection.bot_detection.update.0"
    client = get_client(test_id)
    client.attack_protection.bot_detection.update()
    verify_request_count(test_id, "PATCH", "/attack-protection/bot-detection", None, 1)
