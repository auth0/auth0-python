from .conftest import get_client, verify_request_count


def test_guardian_factors_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "guardian.factors.list_.0"
    client = get_client(test_id)
    client.guardian.factors.list()
    verify_request_count(test_id, "GET", "/guardian/factors", None, 1)


def test_guardian_factors_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "guardian.factors.set_.0"
    client = get_client(test_id)
    client.guardian.factors.set(name="push-notification", enabled=True)
    verify_request_count(test_id, "PUT", "/guardian/factors/push-notification", None, 1)
