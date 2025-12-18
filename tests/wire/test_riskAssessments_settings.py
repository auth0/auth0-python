from .conftest import get_client, verify_request_count


def test_riskAssessments_settings_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "risk_assessments.settings.get.0"
    client = get_client(test_id)
    client.risk_assessments.settings.get()
    verify_request_count(test_id, "GET", "/risk-assessments/settings", None, 1)


def test_riskAssessments_settings_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "risk_assessments.settings.update.0"
    client = get_client(test_id)
    client.risk_assessments.settings.update(enabled=True)
    verify_request_count(test_id, "PATCH", "/risk-assessments/settings", None, 1)
