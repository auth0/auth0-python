from .conftest import get_client, verify_request_count


def test_branding_templates_get_universal_login() -> None:
    """Test getUniversalLogin endpoint with WireMock"""
    test_id = "branding.templates.get_universal_login.0"
    client = get_client(test_id)
    client.branding.templates.get_universal_login()
    verify_request_count(test_id, "GET", "/branding/templates/universal-login", None, 1)


def test_branding_templates_update_universal_login() -> None:
    """Test updateUniversalLogin endpoint with WireMock"""
    test_id = "branding.templates.update_universal_login.0"
    client = get_client(test_id)
    client.branding.templates.update_universal_login(request="string")
    verify_request_count(test_id, "PUT", "/branding/templates/universal-login", None, 1)


def test_branding_templates_delete_universal_login() -> None:
    """Test deleteUniversalLogin endpoint with WireMock"""
    test_id = "branding.templates.delete_universal_login.0"
    client = get_client(test_id)
    client.branding.templates.delete_universal_login()
    verify_request_count(test_id, "DELETE", "/branding/templates/universal-login", None, 1)
