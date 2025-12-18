from .conftest import get_client, verify_request_count


def test_logStreams_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "log_streams.list_.0"
    client = get_client(test_id)
    client.log_streams.list()
    verify_request_count(test_id, "GET", "/log-streams", None, 1)


def test_logStreams_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "log_streams.create.0"
    client = get_client(test_id)
    client.log_streams.create(request={"type": "http", "sink": {"http_endpoint": "httpEndpoint"}})
    verify_request_count(test_id, "POST", "/log-streams", None, 1)


def test_logStreams_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "log_streams.get.0"
    client = get_client(test_id)
    client.log_streams.get(id="id")
    verify_request_count(test_id, "GET", "/log-streams/id", None, 1)


def test_logStreams_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "log_streams.delete.0"
    client = get_client(test_id)
    client.log_streams.delete(id="id")
    verify_request_count(test_id, "DELETE", "/log-streams/id", None, 1)


def test_logStreams_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "log_streams.update.0"
    client = get_client(test_id)
    client.log_streams.update(id="id")
    verify_request_count(test_id, "PATCH", "/log-streams/id", None, 1)
