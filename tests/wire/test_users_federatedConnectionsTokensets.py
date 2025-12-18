from .conftest import get_client, verify_request_count


def test_users_federatedConnectionsTokensets_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "users.federated_connections_tokensets.list_.0"
    client = get_client(test_id)
    client.users.federated_connections_tokensets.list(id="id")
    verify_request_count(test_id, "GET", "/users/id/federated-connections-tokensets", None, 1)


def test_users_federatedConnectionsTokensets_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "users.federated_connections_tokensets.delete.0"
    client = get_client(test_id)
    client.users.federated_connections_tokensets.delete(id="id", tokenset_id="tokenset_id")
    verify_request_count(test_id, "DELETE", "/users/id/federated-connections-tokensets/tokenset_id", None, 1)
