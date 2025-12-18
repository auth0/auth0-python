from .conftest import get_client, verify_request_count


def test_guardian_policies_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "guardian.policies.list_.0"
    client = get_client(test_id)
    client.guardian.policies.list()
    verify_request_count(test_id, "GET", "/guardian/policies", None, 1)


def test_guardian_policies_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "guardian.policies.set_.0"
    client = get_client(test_id)
    client.guardian.policies.set(request=["all-applications"])
    verify_request_count(test_id, "PUT", "/guardian/policies", None, 1)
