from .conftest import get_client, verify_request_count


def test_organizations_members_effectiveRoles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.members.effective_roles.list_.0"
    client = get_client(test_id)
    client.organizations.members.effective_roles.list(
        id="id",
        user_id="user_id",
        from_="from",
        take=1,
    )
    verify_request_count(
        test_id, "GET", "/organizations/id/members/user_id/effective-roles", {"from": "from", "take": "1"}, 1
    )
