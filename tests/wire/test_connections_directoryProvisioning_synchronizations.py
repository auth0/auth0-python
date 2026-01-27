from .conftest import get_client, verify_request_count


def test_connections_directoryProvisioning_synchronizations_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "connections.directory_provisioning.synchronizations.create.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.synchronizations.create(id="id")
    verify_request_count(test_id, "POST", "/connections/id/directory-provisioning/synchronizations", None, 1)
