from .conftest import get_client, verify_request_count


def test_users_effectivePermissions_sources_roles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "users.effective_permissions.sources.roles.list_.0"
    client = get_client(test_id)
    client.users.effective_permissions.sources.roles.list(
        id="id",
        from_="from",
        take=1,
        resource_server_identifier="resource_server_identifier",
        permission_name="permission_name",
    )
    verify_request_count(
        test_id,
        "GET",
        "/users/id/effective-permissions/sources/effective-roles",
        {
            "from": "from",
            "take": "1",
            "resource_server_identifier": "resource_server_identifier",
            "permission_name": "permission_name",
        },
        1,
    )
