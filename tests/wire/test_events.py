from .conftest import get_client, verify_request_count


def test_events_subscribe() -> None:
    """Test subscribe endpoint with WireMock"""
    test_id = "events.subscribe.0"
    client = get_client(test_id)
    for _ in client.events.subscribe(
        from_="from",
        from_timestamp="from_timestamp",
        event_type=["group.created"],
    ):
        pass
    verify_request_count(
        test_id,
        "GET",
        "/events",
        {"from": "from", "from_timestamp": "from_timestamp", "event_type": "group.created"},
        1,
    )
