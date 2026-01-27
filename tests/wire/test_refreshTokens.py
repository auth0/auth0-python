from .conftest import get_client, verify_request_count


def test_refreshTokens_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "refresh_tokens.get.0"
    client = get_client(test_id)
    client.refresh_tokens.get(id="id")
    verify_request_count(test_id, "GET", "/refresh-tokens/id", None, 1)


def test_refreshTokens_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "refresh_tokens.delete.0"
    client = get_client(test_id)
    client.refresh_tokens.delete(id="id")
    verify_request_count(test_id, "DELETE", "/refresh-tokens/id", None, 1)


def test_refreshTokens_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "refresh_tokens.update.0"
    client = get_client(test_id)
    client.refresh_tokens.update(id="id")
    verify_request_count(test_id, "PATCH", "/refresh-tokens/id", None, 1)
