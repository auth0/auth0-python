from .conftest import get_client, verify_request_count


def test_users_effectiveRoles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "users.effective_roles.list_.0"
    client = get_client(test_id)
    client.users.effective_roles.list(
        id="id",
        from_="from",
        take=1,
    )
    verify_request_count(test_id, "GET", "/users/id/effective-roles", {"from": "from", "take": "1"}, 1)
