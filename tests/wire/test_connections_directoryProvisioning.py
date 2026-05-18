from .conftest import get_client, verify_request_count

from auth0.management import (
    CreateDirectoryProvisioningRequestContent,
    SynchronizedGroupPayload,
    UpdateDirectoryProvisioningRequestContent,
)


def test_connections_directoryProvisioning_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "connections.directory_provisioning.list_.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.list(
        from_="from",
        take=1,
    )
    verify_request_count(test_id, "GET", "/connections-directory-provisionings", {"from": "from", "take": "1"}, 1)


def test_connections_directoryProvisioning_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "connections.directory_provisioning.get.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/connections/id/directory-provisioning", None, 1)


def test_connections_directoryProvisioning_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "connections.directory_provisioning.create.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.create(
        id="id",
        request=CreateDirectoryProvisioningRequestContent(),
    )
    verify_request_count(test_id, "POST", "/connections/id/directory-provisioning", None, 1)


def test_connections_directoryProvisioning_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "connections.directory_provisioning.delete.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/connections/id/directory-provisioning", None, 1)


def test_connections_directoryProvisioning_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "connections.directory_provisioning.update.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.update(
        id="id",
        request=UpdateDirectoryProvisioningRequestContent(),
    )
    verify_request_count(test_id, "PATCH", "/connections/id/directory-provisioning", None, 1)


def test_connections_directoryProvisioning_get_default_mapping() -> None:
    """Test getDefaultMapping endpoint with WireMock"""
    test_id = "connections.directory_provisioning.get_default_mapping.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.get_default_mapping(
        id="id",
    )
    verify_request_count(test_id, "GET", "/connections/id/directory-provisioning/default-mapping", None, 1)


def test_connections_directoryProvisioning_list_synchronized_groups() -> None:
    """Test listSynchronizedGroups endpoint with WireMock"""
    test_id = "connections.directory_provisioning.list_synchronized_groups.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.list_synchronized_groups(
        id="id",
        from_="from",
        take=1,
    )
    verify_request_count(
        test_id, "GET", "/connections/id/directory-provisioning/synchronized-groups", {"from": "from", "take": "1"}, 1
    )


def test_connections_directoryProvisioning_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "connections.directory_provisioning.set_.0"
    client = get_client(test_id)
    client.connections.directory_provisioning.set(
        id="id",
        groups=[
            SynchronizedGroupPayload(
                id="id",
            )
        ],
    )
    verify_request_count(test_id, "PUT", "/connections/id/directory-provisioning/synchronized-groups", None, 1)
