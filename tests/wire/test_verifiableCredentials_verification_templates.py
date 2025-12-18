from .conftest import get_client, verify_request_count


def test_verifiableCredentials_verification_templates_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "verifiable_credentials.verification.templates.list_.0"
    client = get_client(test_id)
    client.verifiable_credentials.verification.templates.list(from_="from", take=1)
    verify_request_count(
        test_id, "GET", "/verifiable-credentials/verification/templates", {"from": "from", "take": "1"}, 1
    )


def test_verifiableCredentials_verification_templates_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "verifiable_credentials.verification.templates.create.0"
    client = get_client(test_id)
    client.verifiable_credentials.verification.templates.create(
        name="name",
        type="type",
        dialect="dialect",
        presentation={"org_iso_18013_5_1_m_dl": {"org_iso_18013_5_1": {}}},
        well_known_trusted_issuers="well_known_trusted_issuers",
    )
    verify_request_count(test_id, "POST", "/verifiable-credentials/verification/templates", None, 1)


def test_verifiableCredentials_verification_templates_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "verifiable_credentials.verification.templates.get.0"
    client = get_client(test_id)
    client.verifiable_credentials.verification.templates.get(id="id")
    verify_request_count(test_id, "GET", "/verifiable-credentials/verification/templates/id", None, 1)


def test_verifiableCredentials_verification_templates_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "verifiable_credentials.verification.templates.delete.0"
    client = get_client(test_id)
    client.verifiable_credentials.verification.templates.delete(id="id")
    verify_request_count(test_id, "DELETE", "/verifiable-credentials/verification/templates/id", None, 1)


def test_verifiableCredentials_verification_templates_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "verifiable_credentials.verification.templates.update.0"
    client = get_client(test_id)
    client.verifiable_credentials.verification.templates.update(id="id")
    verify_request_count(test_id, "PATCH", "/verifiable-credentials/verification/templates/id", None, 1)
