from .conftest import get_client, verify_request_count


def test_users_connectedAccounts_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "users.connected_accounts.list_.0"
    client = get_client(test_id)
    client.users.connected_accounts.list(id="id", from_="from", take=1)
    verify_request_count(test_id, "GET", "/users/id/connected-accounts", {"from": "from", "take": "1"}, 1)
