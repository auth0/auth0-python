from .conftest import get_client, verify_request_count


def test_organizations_members_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.members.list_.0"
    client = get_client(test_id)
    client.organizations.members.list(id="id", from_="from", take=1, fields="fields", include_fields=True)
    verify_request_count(
        test_id,
        "GET",
        "/organizations/id/members",
        {"from": "from", "take": "1", "fields": "fields", "include_fields": "true"},
        1,
    )


def test_organizations_members_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organizations.members.create.0"
    client = get_client(test_id)
    client.organizations.members.create(id="id", members=["members"])
    verify_request_count(test_id, "POST", "/organizations/id/members", None, 1)


def test_organizations_members_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organizations.members.delete.0"
    client = get_client(test_id)
    client.organizations.members.delete(id="id", members=["members"])
    verify_request_count(test_id, "DELETE", "/organizations/id/members", None, 1)
