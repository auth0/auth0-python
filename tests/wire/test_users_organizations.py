from .conftest import get_client, verify_request_count


def test_users_organizations_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "users.organizations.list_.0"
    client = get_client(test_id)
    client.users.organizations.list(id="id", page=1, per_page=1, include_totals=True)
    verify_request_count(
        test_id, "GET", "/users/id/organizations", {"page": "1", "per_page": "1", "include_totals": "true"}, 1
    )
