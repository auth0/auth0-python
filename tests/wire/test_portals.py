from .conftest import get_client, verify_request_count

from auth0.management import PortalClientSecretPostRequest


def test_portals_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "portals.list_.0"
    client = get_client(test_id)
    client.portals.list()
    verify_request_count(test_id, "GET", "/portals", None, 1)


def test_portals_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "portals.create.0"
    client = get_client(test_id)
    client.portals.create(
        slug="slug",
        name="name",
        client=PortalClientSecretPostRequest(
            token_endpoint_auth_method="client_secret_post",
            client_id="client_id",
            client_secret="client_secret",
        ),
    )
    verify_request_count(test_id, "POST", "/portals", None, 1)


def test_portals_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "portals.get.0"
    client = get_client(test_id)
    client.portals.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/portals/id", None, 1)


def test_portals_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "portals.delete.0"
    client = get_client(test_id)
    client.portals.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/portals/id", None, 1)


def test_portals_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "portals.update.0"
    client = get_client(test_id)
    client.portals.update(
        id="id",
    )
    verify_request_count(test_id, "PATCH", "/portals/id", None, 1)
