from .conftest import get_client, verify_request_count


def test_connections_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "connections.list_.0"
    client = get_client(test_id)
    client.connections.list(from_="from", take=1, name="name", fields="fields", include_fields=True)
    verify_request_count(
        test_id,
        "GET",
        "/connections",
        {"from": "from", "take": "1", "name": "name", "fields": "fields", "include_fields": "true"},
        1,
    )


def test_connections_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "connections.create.0"
    client = get_client(test_id)
    client.connections.create(name="name", strategy="ad")
    verify_request_count(test_id, "POST", "/connections", None, 1)


def test_connections_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "connections.get.0"
    client = get_client(test_id)
    client.connections.get(id="id", fields="fields", include_fields=True)
    verify_request_count(test_id, "GET", "/connections/id", {"fields": "fields", "include_fields": "true"}, 1)


def test_connections_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "connections.delete.0"
    client = get_client(test_id)
    client.connections.delete(id="id")
    verify_request_count(test_id, "DELETE", "/connections/id", None, 1)


def test_connections_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "connections.update.0"
    client = get_client(test_id)
    client.connections.update(id="id")
    verify_request_count(test_id, "PATCH", "/connections/id", None, 1)


def test_connections_check_status() -> None:
    """Test checkStatus endpoint with WireMock"""
    test_id = "connections.check_status.0"
    client = get_client(test_id)
    client.connections.check_status(id="id")
    verify_request_count(test_id, "GET", "/connections/id/status", None, 1)
