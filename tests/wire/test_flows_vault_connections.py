from .conftest import get_client, verify_request_count


def test_flows_vault_connections_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "flows.vault.connections.list_.0"
    client = get_client(test_id)
    client.flows.vault.connections.list(page=1, per_page=1, include_totals=True)
    verify_request_count(
        test_id, "GET", "/flows/vault/connections", {"page": "1", "per_page": "1", "include_totals": "true"}, 1
    )


def test_flows_vault_connections_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "flows.vault.connections.create.0"
    client = get_client(test_id)
    client.flows.vault.connections.create(
        request={
            "name": "name",
            "app_id": "ACTIVECAMPAIGN",
            "setup": {"type": "API_KEY", "api_key": "api_key", "base_url": "base_url"},
        }
    )
    verify_request_count(test_id, "POST", "/flows/vault/connections", None, 1)


def test_flows_vault_connections_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "flows.vault.connections.get.0"
    client = get_client(test_id)
    client.flows.vault.connections.get(id="id")
    verify_request_count(test_id, "GET", "/flows/vault/connections/id", None, 1)


def test_flows_vault_connections_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "flows.vault.connections.delete.0"
    client = get_client(test_id)
    client.flows.vault.connections.delete(id="id")
    verify_request_count(test_id, "DELETE", "/flows/vault/connections/id", None, 1)


def test_flows_vault_connections_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "flows.vault.connections.update.0"
    client = get_client(test_id)
    client.flows.vault.connections.update(id="id")
    verify_request_count(test_id, "PATCH", "/flows/vault/connections/id", None, 1)
