from .conftest import get_client, verify_request_count


def test_clients_connections_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "clients.connections.get.0"
    client = get_client(test_id)
    client.clients.connections.get(id="id", from_="from", take=1, fields="fields", include_fields=True)
    verify_request_count(
        test_id,
        "GET",
        "/clients/id/connections",
        {"from": "from", "take": "1", "fields": "fields", "include_fields": "true"},
        1,
    )
