from .conftest import get_client, verify_request_count


def test_eventStreams_deliveries_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "event_streams.deliveries.list_.0"
    client = get_client(test_id)
    client.event_streams.deliveries.list(
        id="id",
        statuses="statuses",
        event_types="event_types",
        date_from="date_from",
        date_to="date_to",
        from_="from",
        take=1,
    )
    verify_request_count(
        test_id,
        "GET",
        "/event-streams/id/deliveries",
        {
            "statuses": "statuses",
            "event_types": "event_types",
            "date_from": "date_from",
            "date_to": "date_to",
            "from": "from",
            "take": "1",
        },
        1,
    )


def test_eventStreams_deliveries_get_history() -> None:
    """Test getHistory endpoint with WireMock"""
    test_id = "event_streams.deliveries.get_history.0"
    client = get_client(test_id)
    client.event_streams.deliveries.get_history(id="id", event_id="event_id")
    verify_request_count(test_id, "GET", "/event-streams/id/deliveries/event_id", None, 1)
