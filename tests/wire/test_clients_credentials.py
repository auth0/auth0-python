from .conftest import get_client, verify_request_count


def test_clients_credentials_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "clients.credentials.list_.0"
    client = get_client(test_id)
    client.clients.credentials.list(client_id="client_id")
    verify_request_count(test_id, "GET", "/clients/client_id/credentials", None, 1)


def test_clients_credentials_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "clients.credentials.create.0"
    client = get_client(test_id)
    client.clients.credentials.create(client_id="client_id", credential_type="public_key")
    verify_request_count(test_id, "POST", "/clients/client_id/credentials", None, 1)


def test_clients_credentials_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "clients.credentials.get.0"
    client = get_client(test_id)
    client.clients.credentials.get(client_id="client_id", credential_id="credential_id")
    verify_request_count(test_id, "GET", "/clients/client_id/credentials/credential_id", None, 1)


def test_clients_credentials_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "clients.credentials.delete.0"
    client = get_client(test_id)
    client.clients.credentials.delete(client_id="client_id", credential_id="credential_id")
    verify_request_count(test_id, "DELETE", "/clients/client_id/credentials/credential_id", None, 1)


def test_clients_credentials_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "clients.credentials.update.0"
    client = get_client(test_id)
    client.clients.credentials.update(client_id="client_id", credential_id="credential_id")
    verify_request_count(test_id, "PATCH", "/clients/client_id/credentials/credential_id", None, 1)
