from .conftest import get_client, verify_request_count


def test_organizations_groups_roles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.groups.roles.list_.0"
    client = get_client(test_id)
    client.organizations.groups.roles.list(
        organization_id="organization_id",
        group_id="group_id",
        from_="from",
        take=1,
    )
    verify_request_count(
        test_id, "GET", "/organizations/organization_id/groups/group_id/roles", {"from": "from", "take": "1"}, 1
    )


def test_organizations_groups_roles_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organizations.groups.roles.create.0"
    client = get_client(test_id)
    client.organizations.groups.roles.create(
        organization_id="organization_id",
        group_id="group_id",
        roles=["roles"],
    )
    verify_request_count(test_id, "POST", "/organizations/organization_id/groups/group_id/roles", None, 1)


def test_organizations_groups_roles_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organizations.groups.roles.delete.0"
    client = get_client(test_id)
    client.organizations.groups.roles.delete(
        organization_id="organization_id",
        group_id="group_id",
        roles=["roles"],
    )
    verify_request_count(test_id, "DELETE", "/organizations/organization_id/groups/group_id/roles", None, 1)
