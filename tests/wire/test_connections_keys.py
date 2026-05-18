from .conftest import get_client, verify_request_count

from auth0.management import PostConnectionKeysRequestContent, RotateConnectionKeysRequestContent


def test_connections_keys_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "connections.keys.get.0"
    client = get_client(test_id)
    client.connections.keys.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/connections/id/keys", None, 1)


def test_connections_keys_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "connections.keys.create.0"
    client = get_client(test_id)
    client.connections.keys.create(
        id="id",
        request=PostConnectionKeysRequestContent(),
    )
    verify_request_count(test_id, "POST", "/connections/id/keys", None, 1)


def test_connections_keys_rotate() -> None:
    """Test rotate endpoint with WireMock"""
    test_id = "connections.keys.rotate.0"
    client = get_client(test_id)
    client.connections.keys.rotate(
        id="id",
        request=RotateConnectionKeysRequestContent(),
    )
    verify_request_count(test_id, "POST", "/connections/id/keys/rotate", None, 1)
