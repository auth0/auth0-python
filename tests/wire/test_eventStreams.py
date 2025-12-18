from .conftest import get_client, verify_request_count


def test_eventStreams_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "event_streams.list_.0"
    client = get_client(test_id)
    client.event_streams.list(from_="from", take=1)
    verify_request_count(test_id, "GET", "/event-streams", {"from": "from", "take": "1"}, 1)


def test_eventStreams_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "event_streams.create.0"
    client = get_client(test_id)
    client.event_streams.create(
        request={
            "destination": {
                "type": "webhook",
                "configuration": {
                    "webhook_endpoint": "webhook_endpoint",
                    "webhook_authorization": {"method": "basic", "username": "username"},
                },
            }
        }
    )
    verify_request_count(test_id, "POST", "/event-streams", None, 1)


def test_eventStreams_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "event_streams.get.0"
    client = get_client(test_id)
    client.event_streams.get(id="id")
    verify_request_count(test_id, "GET", "/event-streams/id", None, 1)


def test_eventStreams_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "event_streams.delete.0"
    client = get_client(test_id)
    client.event_streams.delete(id="id")
    verify_request_count(test_id, "DELETE", "/event-streams/id", None, 1)


def test_eventStreams_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "event_streams.update.0"
    client = get_client(test_id)
    client.event_streams.update(id="id")
    verify_request_count(test_id, "PATCH", "/event-streams/id", None, 1)


def test_eventStreams_test() -> None:
    """Test test endpoint with WireMock"""
    test_id = "event_streams.test.0"
    client = get_client(test_id)
    client.event_streams.test(id="id", event_type="user.created")
    verify_request_count(test_id, "POST", "/event-streams/id/test", None, 1)
