from .conftest import get_client, verify_request_count


def test_prompts_partials_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "prompts.partials.get.0"
    client = get_client(test_id)
    client.prompts.partials.get(prompt="login")
    verify_request_count(test_id, "GET", "/prompts/login/partials", None, 1)


def test_prompts_partials_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "prompts.partials.set_.0"
    client = get_client(test_id)
    client.prompts.partials.set(prompt="login", request={"key": "value"})
    verify_request_count(test_id, "PUT", "/prompts/login/partials", None, 1)
