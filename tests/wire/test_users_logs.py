from .conftest import get_client, verify_request_count


def test_users_logs_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "users.logs.list_.0"
    client = get_client(test_id)
    client.users.logs.list(id="id", page=1, per_page=1, sort="sort", include_totals=True)
    verify_request_count(
        test_id, "GET", "/users/id/logs", {"page": "1", "per_page": "1", "sort": "sort", "include_totals": "true"}, 1
    )
