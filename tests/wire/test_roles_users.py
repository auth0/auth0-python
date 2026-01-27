from .conftest import get_client, verify_request_count


def test_roles_users_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "roles.users.list_.0"
    client = get_client(test_id)
    client.roles.users.list(id="id", from_="from", take=1)
    verify_request_count(test_id, "GET", "/roles/id/users", {"from": "from", "take": "1"}, 1)


def test_roles_users_assign() -> None:
    """Test assign endpoint with WireMock"""
    test_id = "roles.users.assign.0"
    client = get_client(test_id)
    client.roles.users.assign(id="id", users=["users"])
    verify_request_count(test_id, "POST", "/roles/id/users", None, 1)
