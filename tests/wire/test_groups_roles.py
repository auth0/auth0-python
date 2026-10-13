from .conftest import get_client, verify_request_count


def test_groups_roles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "groups.roles.list_.0"
    client = get_client(test_id)
    client.groups.roles.list(
        id="id",
        from_="from",
        take=1,
    )
    verify_request_count(test_id, "GET", "/groups/id/roles", {"from": "from", "take": "1"}, 1)


def test_groups_roles_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "groups.roles.create.0"
    client = get_client(test_id)
    client.groups.roles.create(
        id="id",
        roles=["roles"],
    )
    verify_request_count(test_id, "POST", "/groups/id/roles", None, 1)


def test_groups_roles_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "groups.roles.delete.0"
    client = get_client(test_id)
    client.groups.roles.delete(
        id="id",
        roles=["roles"],
    )
    verify_request_count(test_id, "DELETE", "/groups/id/roles", None, 1)
