from .conftest import get_client, verify_request_count


def test_organizations_roles_members_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.roles.members.list_.0"
    client = get_client(test_id)
    client.organizations.roles.members.list(
        id="id",
        role_id="role_id",
        from_="from",
        take=1,
        fields="fields",
        include_fields=True,
    )
    verify_request_count(
        test_id,
        "GET",
        "/organizations/id/roles/role_id/members",
        {"from": "from", "take": "1", "fields": "fields", "include_fields": "true"},
        1,
    )
