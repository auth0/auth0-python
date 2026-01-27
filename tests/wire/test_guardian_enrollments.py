from .conftest import get_client, verify_request_count


def test_guardian_enrollments_create_ticket() -> None:
    """Test createTicket endpoint with WireMock"""
    test_id = "guardian.enrollments.create_ticket.0"
    client = get_client(test_id)
    client.guardian.enrollments.create_ticket(user_id="user_id")
    verify_request_count(test_id, "POST", "/guardian/enrollments/ticket", None, 1)


def test_guardian_enrollments_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "guardian.enrollments.get.0"
    client = get_client(test_id)
    client.guardian.enrollments.get(id="id")
    verify_request_count(test_id, "GET", "/guardian/enrollments/id", None, 1)


def test_guardian_enrollments_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "guardian.enrollments.delete.0"
    client = get_client(test_id)
    client.guardian.enrollments.delete(id="id")
    verify_request_count(test_id, "DELETE", "/guardian/enrollments/id", None, 1)
