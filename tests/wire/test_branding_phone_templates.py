from .conftest import get_client, verify_request_count


def test_branding_phone_templates_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "branding.phone.templates.list_.0"
    client = get_client(test_id)
    client.branding.phone.templates.list(disabled=True)
    verify_request_count(test_id, "GET", "/branding/phone/templates", {"disabled": "true"}, 1)


def test_branding_phone_templates_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "branding.phone.templates.create.0"
    client = get_client(test_id)
    client.branding.phone.templates.create()
    verify_request_count(test_id, "POST", "/branding/phone/templates", None, 1)


def test_branding_phone_templates_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "branding.phone.templates.get.0"
    client = get_client(test_id)
    client.branding.phone.templates.get(id="id")
    verify_request_count(test_id, "GET", "/branding/phone/templates/id", None, 1)


def test_branding_phone_templates_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "branding.phone.templates.delete.0"
    client = get_client(test_id)
    client.branding.phone.templates.delete(id="id")
    verify_request_count(test_id, "DELETE", "/branding/phone/templates/id", None, 1)


def test_branding_phone_templates_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "branding.phone.templates.update.0"
    client = get_client(test_id)
    client.branding.phone.templates.update(id="id")
    verify_request_count(test_id, "PATCH", "/branding/phone/templates/id", None, 1)


def test_branding_phone_templates_reset() -> None:
    """Test reset endpoint with WireMock"""
    test_id = "branding.phone.templates.reset.0"
    client = get_client(test_id)
    client.branding.phone.templates.reset(
        id="id",
        request={
            "key": "value",
        },
    )
    verify_request_count(test_id, "PATCH", "/branding/phone/templates/id/reset", None, 1)


def test_branding_phone_templates_test() -> None:
    """Test test endpoint with WireMock"""
    test_id = "branding.phone.templates.test.0"
    client = get_client(test_id)
    client.branding.phone.templates.test(id="id", to="to")
    verify_request_count(test_id, "POST", "/branding/phone/templates/id/try", None, 1)
