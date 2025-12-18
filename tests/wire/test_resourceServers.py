from .conftest import get_client, verify_request_count


def test_resourceServers_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "resource_servers.list_.0"
    client = get_client(test_id)
    client.resource_servers.list(page=1, per_page=1, include_totals=True, include_fields=True)
    verify_request_count(
        test_id,
        "GET",
        "/resource-servers",
        {"page": "1", "per_page": "1", "include_totals": "true", "include_fields": "true"},
        1,
    )


def test_resourceServers_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "resource_servers.create.0"
    client = get_client(test_id)
    client.resource_servers.create(identifier="identifier")
    verify_request_count(test_id, "POST", "/resource-servers", None, 1)


def test_resourceServers_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "resource_servers.get.0"
    client = get_client(test_id)
    client.resource_servers.get(id="id", include_fields=True)
    verify_request_count(test_id, "GET", "/resource-servers/id", {"include_fields": "true"}, 1)


def test_resourceServers_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "resource_servers.delete.0"
    client = get_client(test_id)
    client.resource_servers.delete(id="id")
    verify_request_count(test_id, "DELETE", "/resource-servers/id", None, 1)


def test_resourceServers_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "resource_servers.update.0"
    client = get_client(test_id)
    client.resource_servers.update(id="id")
    verify_request_count(test_id, "PATCH", "/resource-servers/id", None, 1)
