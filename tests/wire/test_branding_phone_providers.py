from .conftest import get_client, verify_request_count


def test_branding_phone_providers_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "branding.phone.providers.list_.0"
    client = get_client(test_id)
    client.branding.phone.providers.list(disabled=True)
    verify_request_count(test_id, "GET", "/branding/phone/providers", {"disabled": "true"}, 1)


def test_branding_phone_providers_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "branding.phone.providers.create.0"
    client = get_client(test_id)
    client.branding.phone.providers.create(name="twilio", credentials={"auth_token": "auth_token"})
    verify_request_count(test_id, "POST", "/branding/phone/providers", None, 1)


def test_branding_phone_providers_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "branding.phone.providers.get.0"
    client = get_client(test_id)
    client.branding.phone.providers.get(id="id")
    verify_request_count(test_id, "GET", "/branding/phone/providers/id", None, 1)


def test_branding_phone_providers_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "branding.phone.providers.delete.0"
    client = get_client(test_id)
    client.branding.phone.providers.delete(id="id")
    verify_request_count(test_id, "DELETE", "/branding/phone/providers/id", None, 1)


def test_branding_phone_providers_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "branding.phone.providers.update.0"
    client = get_client(test_id)
    client.branding.phone.providers.update(id="id")
    verify_request_count(test_id, "PATCH", "/branding/phone/providers/id", None, 1)


def test_branding_phone_providers_test() -> None:
    """Test test endpoint with WireMock"""
    test_id = "branding.phone.providers.test.0"
    client = get_client(test_id)
    client.branding.phone.providers.test(id="id", to="to")
    verify_request_count(test_id, "POST", "/branding/phone/providers/id/try", None, 1)
