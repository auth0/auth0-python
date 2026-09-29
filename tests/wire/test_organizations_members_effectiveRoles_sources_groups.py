from .conftest import get_client, verify_request_count


def test_organizations_members_effectiveRoles_sources_groups_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.members.effective_roles.sources.groups.list_.0"
    client = get_client(test_id)
    client.organizations.members.effective_roles.sources.groups.list(
        id="id",
        user_id="user_id",
        from_="from",
        take=1,
        role_id="role_id",
    )
    verify_request_count(
        test_id,
        "GET",
        "/organizations/id/members/user_id/effective-roles/sources/groups",
        {"from": "from", "take": "1", "role_id": "role_id"},
        1,
    )
