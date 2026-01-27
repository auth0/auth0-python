from .conftest import get_client, verify_request_count


def test_connections_scimConfiguration_tokens_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "connections.scim_configuration.tokens.get.0"
    client = get_client(test_id)
    client.connections.scim_configuration.tokens.get(id="id")
    verify_request_count(test_id, "GET", "/connections/id/scim-configuration/tokens", None, 1)


def test_connections_scimConfiguration_tokens_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "connections.scim_configuration.tokens.create.0"
    client = get_client(test_id)
    client.connections.scim_configuration.tokens.create(id="id")
    verify_request_count(test_id, "POST", "/connections/id/scim-configuration/tokens", None, 1)


def test_connections_scimConfiguration_tokens_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "connections.scim_configuration.tokens.delete.0"
    client = get_client(test_id)
    client.connections.scim_configuration.tokens.delete(id="id", token_id="tokenId")
    verify_request_count(test_id, "DELETE", "/connections/id/scim-configuration/tokens/tokenId", None, 1)
