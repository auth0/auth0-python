from .conftest import get_client, verify_request_count


def test_users_roles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "users.roles.list_.0"
    client = get_client(test_id)
    client.users.roles.list(id="id", per_page=1, page=1, include_totals=True)
    verify_request_count(test_id, "GET", "/users/id/roles", {"per_page": "1", "page": "1", "include_totals": "true"}, 1)


def test_users_roles_assign() -> None:
    """Test assign endpoint with WireMock"""
    test_id = "users.roles.assign.0"
    client = get_client(test_id)
    client.users.roles.assign(id="id", roles=["roles"])
    verify_request_count(test_id, "POST", "/users/id/roles", None, 1)


def test_users_roles_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "users.roles.delete.0"
    client = get_client(test_id)
    client.users.roles.delete(id="id", roles=["roles"])
    verify_request_count(test_id, "DELETE", "/users/id/roles", None, 1)
