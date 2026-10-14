from .conftest import get_client, verify_request_count

from auth0.management import AttackProtectionCaptchaPolicyActionInput, AttackProtectionCaptchaPolicyMatch


def test_attackProtection_captchaPolicies_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "attack_protection.captcha_policies.list_.0"
    client = get_client(test_id)
    client.attack_protection.captcha_policies.list()
    verify_request_count(test_id, "GET", "/attack-protection/captcha/policies", None, 1)


def test_attackProtection_captchaPolicies_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "attack_protection.captcha_policies.create.0"
    client = get_client(test_id)
    client.attack_protection.captcha_policies.create(
        name="name",
        priority=1,
        match=AttackProtectionCaptchaPolicyMatch(),
        action=AttackProtectionCaptchaPolicyActionInput(),
    )
    verify_request_count(test_id, "POST", "/attack-protection/captcha/policies", None, 1)


def test_attackProtection_captchaPolicies_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "attack_protection.captcha_policies.get.0"
    client = get_client(test_id)
    client.attack_protection.captcha_policies.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/attack-protection/captcha/policies/id", None, 1)


def test_attackProtection_captchaPolicies_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "attack_protection.captcha_policies.delete.0"
    client = get_client(test_id)
    client.attack_protection.captcha_policies.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/attack-protection/captcha/policies/id", None, 1)


def test_attackProtection_captchaPolicies_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "attack_protection.captcha_policies.update.0"
    client = get_client(test_id)
    client.attack_protection.captcha_policies.update(
        id="id",
    )
    verify_request_count(test_id, "PATCH", "/attack-protection/captcha/policies/id", None, 1)
