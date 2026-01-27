from .conftest import get_client, verify_request_count


def test_connections_clients_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "connections.clients.get.0"
    client = get_client(test_id)
    client.connections.clients.get(id="id", take=1, from_="from")
    verify_request_count(test_id, "GET", "/connections/id/clients", {"take": "1", "from": "from"}, 1)


def test_connections_clients_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "connections.clients.update.0"
    client = get_client(test_id)
    client.connections.clients.update(id="id", request=[{"client_id": "client_id", "status": True}])
    verify_request_count(test_id, "PATCH", "/connections/id/clients", None, 1)
