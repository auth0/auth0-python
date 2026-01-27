from .conftest import get_client, verify_request_count


def test_attackProtection_bruteForceProtection_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "attack_protection.brute_force_protection.get.0"
    client = get_client(test_id)
    client.attack_protection.brute_force_protection.get()
    verify_request_count(test_id, "GET", "/attack-protection/brute-force-protection", None, 1)


def test_attackProtection_bruteForceProtection_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "attack_protection.brute_force_protection.update.0"
    client = get_client(test_id)
    client.attack_protection.brute_force_protection.update()
    verify_request_count(test_id, "PATCH", "/attack-protection/brute-force-protection", None, 1)
