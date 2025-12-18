from .conftest import get_client, verify_request_count


def test_users_refreshToken_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "users.refresh_token.list_.0"
    client = get_client(test_id)
    client.users.refresh_token.list(user_id="user_id", from_="from", take=1)
    verify_request_count(test_id, "GET", "/users/user_id/refresh-tokens", {"from": "from", "take": "1"}, 1)


def test_users_refreshToken_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "users.refresh_token.delete.0"
    client = get_client(test_id)
    client.users.refresh_token.delete(user_id="user_id")
    verify_request_count(test_id, "DELETE", "/users/user_id/refresh-tokens", None, 1)
