from .conftest import get_client, verify_request_count


def test_users_permissions_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "users.permissions.list_.0"
    client = get_client(test_id)
    client.users.permissions.list(id="id", per_page=1, page=1, include_totals=True)
    verify_request_count(
        test_id, "GET", "/users/id/permissions", {"per_page": "1", "page": "1", "include_totals": "true"}, 1
    )


def test_users_permissions_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "users.permissions.create.0"
    client = get_client(test_id)
    client.users.permissions.create(
        id="id",
        permissions=[
            {"resource_server_identifier": "resource_server_identifier", "permission_name": "permission_name"}
        ],
    )
    verify_request_count(test_id, "POST", "/users/id/permissions", None, 1)


def test_users_permissions_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "users.permissions.delete.0"
    client = get_client(test_id)
    client.users.permissions.delete(
        id="id",
        permissions=[
            {"resource_server_identifier": "resource_server_identifier", "permission_name": "permission_name"}
        ],
    )
    verify_request_count(test_id, "DELETE", "/users/id/permissions", None, 1)
