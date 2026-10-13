from .conftest import get_client, verify_request_count


def test_guardian_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "guardian.get.0"
    client = get_client(test_id)
    client.guardian.get()
    verify_request_count(test_id, "GET", "/guardian/settings", None, 1)


def test_guardian_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "guardian.set_.0"
    client = get_client(test_id)
    client.guardian.set(
        display_remember_me_checkbox=True,
        remember_me_default_value=True,
        mfa_session_inactivity_timeout=1,
        mfa_session_overall_timeout=1,
    )
    verify_request_count(test_id, "PUT", "/guardian/settings", None, 1)
