from .conftest import get_client, verify_request_count


def test_connections_directoryProvisioning_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "connections.directory_provisioning.list_.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.list(from_="from", take=1)
    verify_request_count(test_id, "GET", "/connections-directory-provisionings", {"from": "from", "take": "1"}, 1)


def test_connections_directoryProvisioning_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "connections.directory_provisioning.get.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.get(id="id")
    verify_request_count(test_id, "GET", "/connections/id/directory-provisioning", None, 1)


def test_connections_directoryProvisioning_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "connections.directory_provisioning.create.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.create(id="id", request={})
    verify_request_count(test_id, "POST", "/connections/id/directory-provisioning", None, 1)


def test_connections_directoryProvisioning_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "connections.directory_provisioning.delete.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.delete(id="id")
    verify_request_count(test_id, "DELETE", "/connections/id/directory-provisioning", None, 1)


def test_connections_directoryProvisioning_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "connections.directory_provisioning.update.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.update(id="id", request={})
    verify_request_count(test_id, "PATCH", "/connections/id/directory-provisioning", None, 1)


def test_connections_directoryProvisioning_get_default_mapping() -> None:
    """Test getDefaultMapping endpoint with WireMock"""
    test_id = "connections.directory_provisioning.get_default_mapping.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.get_default_mapping(id="id")
    verify_request_count(test_id, "GET", "/connections/id/directory-provisioning/default-mapping", None, 1)
