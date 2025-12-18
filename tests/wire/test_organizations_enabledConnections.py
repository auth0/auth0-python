from .conftest import get_client, verify_request_count


def test_organizations_enabledConnections_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.enabled_connections.list_.0"
    client = get_client(test_id)
    client.organizations.enabled_connections.list(id="id", page=1, per_page=1, include_totals=True)
    verify_request_count(
        test_id,
        "GET",
        "/organizations/id/enabled_connections",
        {"page": "1", "per_page": "1", "include_totals": "true"},
        1,
    )


def test_organizations_enabledConnections_add() -> None:
    """Test add endpoint with WireMock"""
    test_id = "organizations.enabled_connections.add.0"
    client = get_client(test_id)
    client.organizations.enabled_connections.add(id="id", connection_id="connection_id")
    verify_request_count(test_id, "POST", "/organizations/id/enabled_connections", None, 1)


def test_organizations_enabledConnections_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organizations.enabled_connections.get.0"
    client = get_client(test_id)
    client.organizations.enabled_connections.get(id="id", connection_id="connectionId")
    verify_request_count(test_id, "GET", "/organizations/id/enabled_connections/connectionId", None, 1)


def test_organizations_enabledConnections_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organizations.enabled_connections.delete.0"
    client = get_client(test_id)
    client.organizations.enabled_connections.delete(id="id", connection_id="connectionId")
    verify_request_count(test_id, "DELETE", "/organizations/id/enabled_connections/connectionId", None, 1)


def test_organizations_enabledConnections_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "organizations.enabled_connections.update.0"
    client = get_client(test_id)
    client.organizations.enabled_connections.update(id="id", connection_id="connectionId")
    verify_request_count(test_id, "PATCH", "/organizations/id/enabled_connections/connectionId", None, 1)
