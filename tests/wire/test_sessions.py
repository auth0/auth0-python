from .conftest import get_client, verify_request_count


def test_sessions_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "sessions.get.0"
    client = get_client(test_id)
    client.sessions.get(id="id")
    verify_request_count(test_id, "GET", "/sessions/id", None, 1)


def test_sessions_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "sessions.delete.0"
    client = get_client(test_id)
    client.sessions.delete(id="id")
    verify_request_count(test_id, "DELETE", "/sessions/id", None, 1)


def test_sessions_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "sessions.update.0"
    client = get_client(test_id)
    client.sessions.update(id="id")
    verify_request_count(test_id, "PATCH", "/sessions/id", None, 1)


def test_sessions_revoke() -> None:
    """Test revoke endpoint with WireMock"""
    test_id = "sessions.revoke.0"
    client = get_client(test_id)
    client.sessions.revoke(id="id")
    verify_request_count(test_id, "POST", "/sessions/id/revoke", None, 1)
