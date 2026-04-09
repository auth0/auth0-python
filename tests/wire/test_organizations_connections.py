from .conftest import get_client, verify_request_count


def test_organizations_connections_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.connections.list_.0"
    client = get_client(test_id)
    client.organizations.connections.list(
        id="id",
        page=1,
        per_page=1,
        include_totals=True,
        is_enabled=True,
    )
    verify_request_count(
        test_id,
        "GET",
        "/organizations/id/connections",
        {"page": "1", "per_page": "1", "include_totals": "true", "is_enabled": "true"},
        1,
    )


def test_organizations_connections_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organizations.connections.create.0"
    client = get_client(test_id)
    client.organizations.connections.create(
        id="id",
        connection_id="connection_id",
    )
    verify_request_count(test_id, "POST", "/organizations/id/connections", None, 1)


def test_organizations_connections_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organizations.connections.get.0"
    client = get_client(test_id)
    client.organizations.connections.get(
        id="id",
        connection_id="connection_id",
    )
    verify_request_count(test_id, "GET", "/organizations/id/connections/connection_id", None, 1)


def test_organizations_connections_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organizations.connections.delete.0"
    client = get_client(test_id)
    client.organizations.connections.delete(
        id="id",
        connection_id="connection_id",
    )
    verify_request_count(test_id, "DELETE", "/organizations/id/connections/connection_id", None, 1)


def test_organizations_connections_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "organizations.connections.update.0"
    client = get_client(test_id)
    client.organizations.connections.update(
        id="id",
        connection_id="connection_id",
    )
    verify_request_count(test_id, "PATCH", "/organizations/id/connections/connection_id", None, 1)
