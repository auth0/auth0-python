from .conftest import get_client, verify_request_count


def test_organizations_roles_groups_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.roles.groups.list_.0"
    client = get_client(test_id)
    client.organizations.roles.groups.list(
        organization_id="organization_id",
        role_id="role_id",
        from_="from",
        take=1,
    )
    verify_request_count(
        test_id, "GET", "/organizations/organization_id/roles/role_id/groups", {"from": "from", "take": "1"}, 1
    )
