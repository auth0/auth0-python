from .conftest import get_client, verify_request_count


def test_selfServiceProfiles_ssoTicket_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "self_service_profiles.sso_ticket.create.0"
    client = get_client(test_id)
    client.self_service_profiles.sso_ticket.create(id="id")
    verify_request_count(test_id, "POST", "/self-service-profiles/id/sso-ticket", None, 1)


def test_selfServiceProfiles_ssoTicket_revoke() -> None:
    """Test revoke endpoint with WireMock"""
    test_id = "self_service_profiles.sso_ticket.revoke.0"
    client = get_client(test_id)
    client.self_service_profiles.sso_ticket.revoke(profile_id="profileId", id="id")
    verify_request_count(test_id, "POST", "/self-service-profiles/profileId/sso-ticket/id/revoke", None, 1)
