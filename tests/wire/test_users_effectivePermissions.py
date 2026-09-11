from .conftest import get_client, verify_request_count


def test_users_effectivePermissions_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "users.effective_permissions.list_.0"
    client = get_client(test_id)
    client.users.effective_permissions.list(
        id="id",
        from_="from",
        take=1,
        resource_server_identifier="resource_server_identifier",
    )
    verify_request_count(
        test_id,
        "GET",
        "/users/id/effective-permissions",
        {"from": "from", "take": "1", "resource_server_identifier": "resource_server_identifier"},
        1,
    )
