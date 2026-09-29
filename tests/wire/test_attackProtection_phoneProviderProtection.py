from .conftest import get_client, verify_request_count


def test_attackProtection_phoneProviderProtection_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "attack_protection.phone_provider_protection.get.0"
    client = get_client(test_id)
    client.attack_protection.phone_provider_protection.get()
    verify_request_count(test_id, "GET", "/attack-protection/phone-provider-protection", None, 1)


def test_attackProtection_phoneProviderProtection_patch() -> None:
    """Test patch endpoint with WireMock"""
    test_id = "attack_protection.phone_provider_protection.patch.0"
    client = get_client(test_id)
    client.attack_protection.phone_provider_protection.patch(
        type="exponential",
    )
    verify_request_count(test_id, "PATCH", "/attack-protection/phone-provider-protection", None, 1)
