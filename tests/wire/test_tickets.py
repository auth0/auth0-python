from .conftest import get_client, verify_request_count


def test_tickets_verify_email() -> None:
    """Test verifyEmail endpoint with WireMock"""
    test_id = "tickets.verify_email.0"
    client = get_client(test_id)
    client.tickets.verify_email(user_id="user_id")
    verify_request_count(test_id, "POST", "/tickets/email-verification", None, 1)


def test_tickets_change_password() -> None:
    """Test changePassword endpoint with WireMock"""
    test_id = "tickets.change_password.0"
    client = get_client(test_id)
    client.tickets.change_password()
    verify_request_count(test_id, "POST", "/tickets/password-change", None, 1)
