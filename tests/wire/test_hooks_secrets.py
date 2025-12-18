from .conftest import get_client, verify_request_count


def test_hooks_secrets_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "hooks.secrets.get.0"
    client = get_client(test_id)
    client.hooks.secrets.get(id="id")
    verify_request_count(test_id, "GET", "/hooks/id/secrets", None, 1)


def test_hooks_secrets_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "hooks.secrets.create.0"
    client = get_client(test_id)
    client.hooks.secrets.create(id="id", request={"key": "value"})
    verify_request_count(test_id, "POST", "/hooks/id/secrets", None, 1)


def test_hooks_secrets_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "hooks.secrets.delete.0"
    client = get_client(test_id)
    client.hooks.secrets.delete(id="id", request=["string"])
    verify_request_count(test_id, "DELETE", "/hooks/id/secrets", None, 1)


def test_hooks_secrets_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "hooks.secrets.update.0"
    client = get_client(test_id)
    client.hooks.secrets.update(id="id", request={"key": "value"})
    verify_request_count(test_id, "PATCH", "/hooks/id/secrets", None, 1)
