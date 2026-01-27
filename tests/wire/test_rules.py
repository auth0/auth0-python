from .conftest import get_client, verify_request_count


def test_rules_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "rules.list_.0"
    client = get_client(test_id)
    client.rules.list(page=1, per_page=1, include_totals=True, enabled=True, fields="fields", include_fields=True)
    verify_request_count(
        test_id,
        "GET",
        "/rules",
        {
            "page": "1",
            "per_page": "1",
            "include_totals": "true",
            "enabled": "true",
            "fields": "fields",
            "include_fields": "true",
        },
        1,
    )


def test_rules_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "rules.create.0"
    client = get_client(test_id)
    client.rules.create(name="name", script="script")
    verify_request_count(test_id, "POST", "/rules", None, 1)


def test_rules_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "rules.get.0"
    client = get_client(test_id)
    client.rules.get(id="id", fields="fields", include_fields=True)
    verify_request_count(test_id, "GET", "/rules/id", {"fields": "fields", "include_fields": "true"}, 1)


def test_rules_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "rules.delete.0"
    client = get_client(test_id)
    client.rules.delete(id="id")
    verify_request_count(test_id, "DELETE", "/rules/id", None, 1)


def test_rules_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "rules.update.0"
    client = get_client(test_id)
    client.rules.update(id="id")
    verify_request_count(test_id, "PATCH", "/rules/id", None, 1)
