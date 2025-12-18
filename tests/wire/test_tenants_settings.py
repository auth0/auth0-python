from .conftest import get_client, verify_request_count


def test_tenants_settings_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "tenants.settings.get.0"
    client = get_client(test_id)
    client.tenants.settings.get(fields="fields", include_fields=True)
    verify_request_count(test_id, "GET", "/tenants/settings", {"fields": "fields", "include_fields": "true"}, 1)


def test_tenants_settings_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "tenants.settings.update.0"
    client = get_client(test_id)
    client.tenants.settings.update()
    verify_request_count(test_id, "PATCH", "/tenants/settings", None, 1)
