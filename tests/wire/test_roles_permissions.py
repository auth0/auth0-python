from .conftest import get_client, verify_request_count


def test_roles_permissions_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "roles.permissions.list_.0"
    client = get_client(test_id)
    client.roles.permissions.list(id="id", per_page=1, page=1, include_totals=True)
    verify_request_count(
        test_id, "GET", "/roles/id/permissions", {"per_page": "1", "page": "1", "include_totals": "true"}, 1
    )


def test_roles_permissions_add() -> None:
    """Test add endpoint with WireMock"""
    test_id = "roles.permissions.add.0"
    client = get_client(test_id)
    client.roles.permissions.add(
        id="id",
        permissions=[
            {"resource_server_identifier": "resource_server_identifier", "permission_name": "permission_name"}
        ],
    )
    verify_request_count(test_id, "POST", "/roles/id/permissions", None, 1)


def test_roles_permissions_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "roles.permissions.delete.0"
    client = get_client(test_id)
    client.roles.permissions.delete(
        id="id",
        permissions=[
            {"resource_server_identifier": "resource_server_identifier", "permission_name": "permission_name"}
        ],
    )
    verify_request_count(test_id, "DELETE", "/roles/id/permissions", None, 1)
