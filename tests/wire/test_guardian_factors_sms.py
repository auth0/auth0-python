from .conftest import get_client, verify_request_count


def test_guardian_factors_sms_get_twilio_provider() -> None:
    """Test getTwilioProvider endpoint with WireMock"""
    test_id = "guardian.factors.sms.get_twilio_provider.0"
    client = get_client(test_id)
    client.guardian.factors.sms.get_twilio_provider()
    verify_request_count(test_id, "GET", "/guardian/factors/sms/providers/twilio", None, 1)


def test_guardian_factors_sms_set_twilio_provider() -> None:
    """Test setTwilioProvider endpoint with WireMock"""
    test_id = "guardian.factors.sms.set_twilio_provider.0"
    client = get_client(test_id)
    client.guardian.factors.sms.set_twilio_provider()
    verify_request_count(test_id, "PUT", "/guardian/factors/sms/providers/twilio", None, 1)


def test_guardian_factors_sms_get_selected_provider() -> None:
    """Test getSelectedProvider endpoint with WireMock"""
    test_id = "guardian.factors.sms.get_selected_provider.0"
    client = get_client(test_id)
    client.guardian.factors.sms.get_selected_provider()
    verify_request_count(test_id, "GET", "/guardian/factors/sms/selected-provider", None, 1)


def test_guardian_factors_sms_set_provider() -> None:
    """Test setProvider endpoint with WireMock"""
    test_id = "guardian.factors.sms.set_provider.0"
    client = get_client(test_id)
    client.guardian.factors.sms.set_provider(provider="auth0")
    verify_request_count(test_id, "PUT", "/guardian/factors/sms/selected-provider", None, 1)


def test_guardian_factors_sms_get_templates() -> None:
    """Test getTemplates endpoint with WireMock"""
    test_id = "guardian.factors.sms.get_templates.0"
    client = get_client(test_id)
    client.guardian.factors.sms.get_templates()
    verify_request_count(test_id, "GET", "/guardian/factors/sms/templates", None, 1)


def test_guardian_factors_sms_set_templates() -> None:
    """Test setTemplates endpoint with WireMock"""
    test_id = "guardian.factors.sms.set_templates.0"
    client = get_client(test_id)
    client.guardian.factors.sms.set_templates(
        enrollment_message="enrollment_message", verification_message="verification_message"
    )
    verify_request_count(test_id, "PUT", "/guardian/factors/sms/templates", None, 1)
