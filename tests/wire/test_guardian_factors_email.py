from .conftest import get_client, verify_request_count


def test_guardian_factors_email_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "guardian.factors.email.get.0"
    client = get_client(test_id)
    client.guardian.factors.email.get()
    verify_request_count(test_id, "GET", "/guardian/factors/email/settings", None, 1)


def test_guardian_factors_email_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "guardian.factors.email.set_.0"
    client = get_client(test_id)
    client.guardian.factors.email.set(
        otp_length=1,
        otp_expiration_time=1,
    )
    verify_request_count(test_id, "PUT", "/guardian/factors/email/settings", None, 1)
