from .conftest import get_client, verify_request_count


def test_jobs_verificationEmail_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "jobs.verification_email.create.0"
    client = get_client(test_id)
    client.jobs.verification_email.create(user_id="user_id")
    verify_request_count(test_id, "POST", "/jobs/verification-email", None, 1)
