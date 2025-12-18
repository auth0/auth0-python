from .conftest import get_client, verify_request_count


def test_attackProtection_suspiciousIpThrottling_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "attack_protection.suspicious_ip_throttling.get.0"
    client = get_client(test_id)
    client.attack_protection.suspicious_ip_throttling.get()
    verify_request_count(test_id, "GET", "/attack-protection/suspicious-ip-throttling", None, 1)


def test_attackProtection_suspiciousIpThrottling_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "attack_protection.suspicious_ip_throttling.update.0"
    client = get_client(test_id)
    client.attack_protection.suspicious_ip_throttling.update()
    verify_request_count(test_id, "PATCH", "/attack-protection/suspicious-ip-throttling", None, 1)
