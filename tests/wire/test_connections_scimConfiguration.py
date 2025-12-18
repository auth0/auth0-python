from .conftest import get_client, verify_request_count


def test_connections_scimConfiguration_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "connections.scim_configuration.get.0"
    client = get_client(test_id)
    client.connections.scim_configuration.get(id="id")
    verify_request_count(test_id, "GET", "/connections/id/scim-configuration", None, 1)


def test_connections_scimConfiguration_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "connections.scim_configuration.create.0"
    client = get_client(test_id)
    client.connections.scim_configuration.create(id="id", request={})
    verify_request_count(test_id, "POST", "/connections/id/scim-configuration", None, 1)


def test_connections_scimConfiguration_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "connections.scim_configuration.delete.0"
    client = get_client(test_id)
    client.connections.scim_configuration.delete(id="id")
    verify_request_count(test_id, "DELETE", "/connections/id/scim-configuration", None, 1)


def test_connections_scimConfiguration_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "connections.scim_configuration.update.0"
    client = get_client(test_id)
    client.connections.scim_configuration.update(id="id", user_id_attribute="user_id_attribute", mapping=[{}])
    verify_request_count(test_id, "PATCH", "/connections/id/scim-configuration", None, 1)


def test_connections_scimConfiguration_get_default_mapping() -> None:
    """Test getDefaultMapping endpoint with WireMock"""
    test_id = "connections.scim_configuration.get_default_mapping.0"
    client = get_client(test_id)
    client.connections.scim_configuration.get_default_mapping(id="id")
    verify_request_count(test_id, "GET", "/connections/id/scim-configuration/default-mapping", None, 1)
