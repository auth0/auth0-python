from .conftest import get_client, verify_request_count


def test_riskAssessments_settings_newDevice_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "risk_assessments.settings.new_device.get.0"
    client = get_client(test_id)
    client.risk_assessments.settings.new_device.get()
    verify_request_count(test_id, "GET", "/risk-assessments/settings/new-device", None, 1)


def test_riskAssessments_settings_newDevice_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "risk_assessments.settings.new_device.update.0"
    client = get_client(test_id)
    client.risk_assessments.settings.new_device.update(remember_for=1)
    verify_request_count(test_id, "PATCH", "/risk-assessments/settings/new-device", None, 1)
