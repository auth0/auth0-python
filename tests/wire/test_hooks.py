from .conftest import get_client, verify_request_count


def test_hooks_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "hooks.list_.0"
    client = get_client(test_id)
    client.hooks.list(
        page=1, per_page=1, include_totals=True, enabled=True, fields="fields", trigger_id="credentials-exchange"
    )
    verify_request_count(
        test_id,
        "GET",
        "/hooks",
        {
            "page": "1",
            "per_page": "1",
            "include_totals": "true",
            "enabled": "true",
            "fields": "fields",
            "triggerId": "credentials-exchange",
        },
        1,
    )


def test_hooks_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "hooks.create.0"
    client = get_client(test_id)
    client.hooks.create(name="name", script="script", trigger_id="credentials-exchange")
    verify_request_count(test_id, "POST", "/hooks", None, 1)


def test_hooks_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "hooks.get.0"
    client = get_client(test_id)
    client.hooks.get(id="id", fields="fields")
    verify_request_count(test_id, "GET", "/hooks/id", {"fields": "fields"}, 1)


def test_hooks_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "hooks.delete.0"
    client = get_client(test_id)
    client.hooks.delete(id="id")
    verify_request_count(test_id, "DELETE", "/hooks/id", None, 1)


def test_hooks_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "hooks.update.0"
    client = get_client(test_id)
    client.hooks.update(id="id")
    verify_request_count(test_id, "PATCH", "/hooks/id", None, 1)
