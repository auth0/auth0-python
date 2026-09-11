from .conftest import get_client, verify_request_count


def test_roles_groups_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "roles.groups.get.0"
    client = get_client(test_id)
    client.roles.groups.get(
        id="id",
        from_="from",
        take=1,
    )
    verify_request_count(test_id, "GET", "/roles/id/groups", {"from": "from", "take": "1"}, 1)


def test_roles_groups_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "roles.groups.create.0"
    client = get_client(test_id)
    client.roles.groups.create(
        id="id",
        groups=["groups"],
    )
    verify_request_count(test_id, "POST", "/roles/id/groups", None, 1)


def test_roles_groups_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "roles.groups.delete.0"
    client = get_client(test_id)
    client.roles.groups.delete(
        id="id",
        groups=["groups"],
    )
    verify_request_count(test_id, "DELETE", "/roles/id/groups", None, 1)
