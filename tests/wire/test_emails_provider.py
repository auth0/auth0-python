from .conftest import get_client, verify_request_count


def test_emails_provider_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "emails.provider.get.0"
    client = get_client(test_id)
    client.emails.provider.get(fields="fields", include_fields=True)
    verify_request_count(test_id, "GET", "/emails/provider", {"fields": "fields", "include_fields": "true"}, 1)


def test_emails_provider_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "emails.provider.create.0"
    client = get_client(test_id)
    client.emails.provider.create(name="mailgun", credentials={"api_key": "api_key"})
    verify_request_count(test_id, "POST", "/emails/provider", None, 1)


def test_emails_provider_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "emails.provider.delete.0"
    client = get_client(test_id)
    client.emails.provider.delete()
    verify_request_count(test_id, "DELETE", "/emails/provider", None, 1)


def test_emails_provider_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "emails.provider.update.0"
    client = get_client(test_id)
    client.emails.provider.update()
    verify_request_count(test_id, "PATCH", "/emails/provider", None, 1)
