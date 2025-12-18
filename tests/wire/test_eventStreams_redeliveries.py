from .conftest import get_client, verify_request_count


def test_eventStreams_redeliveries_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "event_streams.redeliveries.create.0"
    client = get_client(test_id)
    client.event_streams.redeliveries.create(id="id")
    verify_request_count(test_id, "POST", "/event-streams/id/redeliver", None, 1)


def test_eventStreams_redeliveries_create_by_id() -> None:
    """Test createById endpoint with WireMock"""
    test_id = "event_streams.redeliveries.create_by_id.0"
    client = get_client(test_id)
    client.event_streams.redeliveries.create_by_id(id="id", event_id="event_id")
    verify_request_count(test_id, "POST", "/event-streams/id/redeliver/event_id", None, 1)
