from .conftest import get_client, verify_request_count


def test_organizations_members_roles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.members.roles.list_.0"
    client = get_client(test_id)
    client.organizations.members.roles.list(id="id", user_id="user_id", page=1, per_page=1, include_totals=True)
    verify_request_count(
        test_id,
        "GET",
        "/organizations/id/members/user_id/roles",
        {"page": "1", "per_page": "1", "include_totals": "true"},
        1,
    )


def test_organizations_members_roles_assign() -> None:
    """Test assign endpoint with WireMock"""
    test_id = "organizations.members.roles.assign.0"
    client = get_client(test_id)
    client.organizations.members.roles.assign(id="id", user_id="user_id", roles=["roles"])
    verify_request_count(test_id, "POST", "/organizations/id/members/user_id/roles", None, 1)


def test_organizations_members_roles_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organizations.members.roles.delete.0"
    client = get_client(test_id)
    client.organizations.members.roles.delete(id="id", user_id="user_id", roles=["roles"])
    verify_request_count(test_id, "DELETE", "/organizations/id/members/user_id/roles", None, 1)
