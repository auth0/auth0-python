from .conftest import get_client, verify_request_count


def test_users_enrollments_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "users.enrollments.get.0"
    client = get_client(test_id)
    client.users.enrollments.get(id="id")
    verify_request_count(test_id, "GET", "/users/id/enrollments", None, 1)
