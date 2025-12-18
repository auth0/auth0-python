from .conftest import get_client, verify_request_count


def test_keys_customSigning_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "keys.custom_signing.get.0"
    client = get_client(test_id)
    client.keys.custom_signing.get()
    verify_request_count(test_id, "GET", "/keys/custom-signing", None, 1)


def test_keys_customSigning_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "keys.custom_signing.set_.0"
    client = get_client(test_id)
    client.keys.custom_signing.set(keys=[{"kty": "EC"}])
    verify_request_count(test_id, "PUT", "/keys/custom-signing", None, 1)


def test_keys_customSigning_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "keys.custom_signing.delete.0"
    client = get_client(test_id)
    client.keys.custom_signing.delete()
    verify_request_count(test_id, "DELETE", "/keys/custom-signing", None, 1)
