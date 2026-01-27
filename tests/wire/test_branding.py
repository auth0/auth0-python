from .conftest import get_client, verify_request_count


def test_branding_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "branding.get.0"
    client = get_client(test_id)
    client.branding.get()
    verify_request_count(test_id, "GET", "/branding", None, 1)


def test_branding_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "branding.update.0"
    client = get_client(test_id)
    client.branding.update()
    verify_request_count(test_id, "PATCH", "/branding", None, 1)
