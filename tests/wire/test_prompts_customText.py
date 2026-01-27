from .conftest import get_client, verify_request_count


def test_prompts_customText_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "prompts.custom_text.get.0"
    client = get_client(test_id)
    client.prompts.custom_text.get(prompt="login", language="am")
    verify_request_count(test_id, "GET", "/prompts/login/custom-text/am", None, 1)


def test_prompts_customText_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "prompts.custom_text.set_.0"
    client = get_client(test_id)
    client.prompts.custom_text.set(prompt="login", language="am", request={"key": "value"})
    verify_request_count(test_id, "PUT", "/prompts/login/custom-text/am", None, 1)
