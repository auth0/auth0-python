from .conftest import get_client, verify_request_count


def test_prompts_rendering_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "prompts.rendering.list_.0"
    client = get_client(test_id)
    client.prompts.rendering.list(
        fields="fields",
        include_fields=True,
        page=1,
        per_page=1,
        include_totals=True,
        prompt="prompt",
        screen="screen",
        rendering_mode="advanced",
    )
    verify_request_count(
        test_id,
        "GET",
        "/prompts/rendering",
        {
            "fields": "fields",
            "include_fields": "true",
            "page": "1",
            "per_page": "1",
            "include_totals": "true",
            "prompt": "prompt",
            "screen": "screen",
            "rendering_mode": "advanced",
        },
        1,
    )


def test_prompts_rendering_bulk_update() -> None:
    """Test bulkUpdate endpoint with WireMock"""
    test_id = "prompts.rendering.bulk_update.0"
    client = get_client(test_id)
    client.prompts.rendering.bulk_update(configs=[{"prompt": "login", "screen": "login"}])
    verify_request_count(test_id, "PATCH", "/prompts/rendering", None, 1)


def test_prompts_rendering_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "prompts.rendering.get.0"
    client = get_client(test_id)
    client.prompts.rendering.get(prompt="login", screen="login")
    verify_request_count(test_id, "GET", "/prompts/login/screen/login/rendering", None, 1)


def test_prompts_rendering_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "prompts.rendering.update.0"
    client = get_client(test_id)
    client.prompts.rendering.update(prompt="login", screen="login")
    verify_request_count(test_id, "PATCH", "/prompts/login/screen/login/rendering", None, 1)
