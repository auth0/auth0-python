from .conftest import get_client, verify_request_count


def test_organizations_invitations_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.invitations.list_.0"
    client = get_client(test_id)
    client.organizations.invitations.list(
        id="id", page=1, per_page=1, include_totals=True, fields="fields", include_fields=True, sort="sort"
    )
    verify_request_count(
        test_id,
        "GET",
        "/organizations/id/invitations",
        {
            "page": "1",
            "per_page": "1",
            "include_totals": "true",
            "fields": "fields",
            "include_fields": "true",
            "sort": "sort",
        },
        1,
    )


def test_organizations_invitations_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organizations.invitations.create.0"
    client = get_client(test_id)
    client.organizations.invitations.create(
        id="id", inviter={"name": "name"}, invitee={"email": "email"}, client_id="client_id"
    )
    verify_request_count(test_id, "POST", "/organizations/id/invitations", None, 1)


def test_organizations_invitations_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organizations.invitations.get.0"
    client = get_client(test_id)
    client.organizations.invitations.get(id="id", invitation_id="invitation_id", fields="fields", include_fields=True)
    verify_request_count(
        test_id, "GET", "/organizations/id/invitations/invitation_id", {"fields": "fields", "include_fields": "true"}, 1
    )


def test_organizations_invitations_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organizations.invitations.delete.0"
    client = get_client(test_id)
    client.organizations.invitations.delete(id="id", invitation_id="invitation_id")
    verify_request_count(test_id, "DELETE", "/organizations/id/invitations/invitation_id", None, 1)
