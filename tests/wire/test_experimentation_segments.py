from .conftest import get_client, verify_request_count

from auth0.management import SegmentRule


def test_experimentation_segments_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "experimentation.segments.list_.0"
    client = get_client(test_id)
    client.experimentation.segments.list(
        from_="from",
        take=1,
        type="auth0",
    )
    verify_request_count(test_id, "GET", "/experimentation/segments", {"from": "from", "take": "1", "type": "auth0"}, 1)


def test_experimentation_segments_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "experimentation.segments.create.0"
    client = get_client(test_id)
    client.experimentation.segments.create(
        name="name",
        rules=[SegmentRule()],
    )
    verify_request_count(test_id, "POST", "/experimentation/segments", None, 1)


def test_experimentation_segments_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "experimentation.segments.get.0"
    client = get_client(test_id)
    client.experimentation.segments.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/experimentation/segments/id", None, 1)


def test_experimentation_segments_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "experimentation.segments.delete.0"
    client = get_client(test_id)
    client.experimentation.segments.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/experimentation/segments/id", None, 1)


def test_experimentation_segments_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "experimentation.segments.update.0"
    client = get_client(test_id)
    client.experimentation.segments.update(
        id="id",
    )
    verify_request_count(test_id, "PATCH", "/experimentation/segments/id", None, 1)
