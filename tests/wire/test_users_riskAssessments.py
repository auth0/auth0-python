from .conftest import get_client, verify_request_count


def test_users_riskAssessments_clear() -> None:
    """Test clear endpoint with WireMock"""
    test_id = "users.risk_assessments.clear.0"
    client = get_client(test_id)
    client.users.risk_assessments.clear(id="id", connection="connection", assessors=["new-device"])
    verify_request_count(test_id, "POST", "/users/id/risk-assessments/clear", None, 1)
