from .conftest import get_client, verify_request_count


def test_selfServiceProfiles_customText_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "self_service_profiles.custom_text.list_.0"
    client = get_client(test_id)
    client.self_service_profiles.custom_text.list(id="id")
    verify_request_count(test_id, "GET", "/self-service-profiles/id/custom-text/en/get-started", None, 1)


def test_selfServiceProfiles_customText_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "self_service_profiles.custom_text.set_.0"
    client = get_client(test_id)
    client.self_service_profiles.custom_text.set(id="id", request={"key": "value"})
    verify_request_count(test_id, "PUT", "/self-service-profiles/id/custom-text/en/get-started", None, 1)
