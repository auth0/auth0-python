from .conftest import get_client, verify_request_count


def test_users_multifactor_invalidate_remember_browser() -> None:
    """Test invalidateRememberBrowser endpoint with WireMock"""
    test_id = "users.multifactor.invalidate_remember_browser.0"
    client = get_client(test_id)
    client.users.multifactor.invalidate_remember_browser(id="id")
    verify_request_count(test_id, "POST", "/users/id/multifactor/actions/invalidate-remember-browser", None, 1)


def test_users_multifactor_delete_provider() -> None:
    """Test deleteProvider endpoint with WireMock"""
    test_id = "users.multifactor.delete_provider.0"
    client = get_client(test_id)
    client.users.multifactor.delete_provider(id="id", provider="duo")
    verify_request_count(test_id, "DELETE", "/users/id/multifactor/duo", None, 1)
