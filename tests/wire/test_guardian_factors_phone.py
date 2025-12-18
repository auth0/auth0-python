from .conftest import get_client, verify_request_count


def test_guardian_factors_phone_get_message_types() -> None:
    """Test getMessageTypes endpoint with WireMock"""
    test_id = "guardian.factors.phone.get_message_types.0"
    client = get_client(test_id)
    client.guardian.factors.phone.get_message_types()
    verify_request_count(test_id, "GET", "/guardian/factors/phone/message-types", None, 1)


def test_guardian_factors_phone_set_message_types() -> None:
    """Test setMessageTypes endpoint with WireMock"""
    test_id = "guardian.factors.phone.set_message_types.0"
    client = get_client(test_id)
    client.guardian.factors.phone.set_message_types(message_types=["sms"])
    verify_request_count(test_id, "PUT", "/guardian/factors/phone/message-types", None, 1)


def test_guardian_factors_phone_get_twilio_provider() -> None:
    """Test getTwilioProvider endpoint with WireMock"""
    test_id = "guardian.factors.phone.get_twilio_provider.0"
    client = get_client(test_id)
    client.guardian.factors.phone.get_twilio_provider()
    verify_request_count(test_id, "GET", "/guardian/factors/phone/providers/twilio", None, 1)


def test_guardian_factors_phone_set_twilio_provider() -> None:
    """Test setTwilioProvider endpoint with WireMock"""
    test_id = "guardian.factors.phone.set_twilio_provider.0"
    client = get_client(test_id)
    client.guardian.factors.phone.set_twilio_provider()
    verify_request_count(test_id, "PUT", "/guardian/factors/phone/providers/twilio", None, 1)


def test_guardian_factors_phone_get_selected_provider() -> None:
    """Test getSelectedProvider endpoint with WireMock"""
    test_id = "guardian.factors.phone.get_selected_provider.0"
    client = get_client(test_id)
    client.guardian.factors.phone.get_selected_provider()
    verify_request_count(test_id, "GET", "/guardian/factors/phone/selected-provider", None, 1)


def test_guardian_factors_phone_set_provider() -> None:
    """Test setProvider endpoint with WireMock"""
    test_id = "guardian.factors.phone.set_provider.0"
    client = get_client(test_id)
    client.guardian.factors.phone.set_provider(provider="auth0")
    verify_request_count(test_id, "PUT", "/guardian/factors/phone/selected-provider", None, 1)


def test_guardian_factors_phone_get_templates() -> None:
    """Test getTemplates endpoint with WireMock"""
    test_id = "guardian.factors.phone.get_templates.0"
    client = get_client(test_id)
    client.guardian.factors.phone.get_templates()
    verify_request_count(test_id, "GET", "/guardian/factors/phone/templates", None, 1)


def test_guardian_factors_phone_set_templates() -> None:
    """Test setTemplates endpoint with WireMock"""
    test_id = "guardian.factors.phone.set_templates.0"
    client = get_client(test_id)
    client.guardian.factors.phone.set_templates(
        enrollment_message="enrollment_message", verification_message="verification_message"
    )
    verify_request_count(test_id, "PUT", "/guardian/factors/phone/templates", None, 1)
