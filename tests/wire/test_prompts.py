from .conftest import get_client, verify_request_count


def test_prompts_get_settings() -> None:
    """Test getSettings endpoint with WireMock"""
    test_id = "prompts.get_settings.0"
    client = get_client(test_id)
    client.prompts.get_settings()
    verify_request_count(test_id, "GET", "/prompts", None, 1)


def test_prompts_update_settings() -> None:
    """Test updateSettings endpoint with WireMock"""
    test_id = "prompts.update_settings.0"
    client = get_client(test_id)
    client.prompts.update_settings()
    verify_request_count(test_id, "PATCH", "/prompts", None, 1)
