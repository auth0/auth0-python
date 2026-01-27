from .conftest import get_client, verify_request_count


def test_keys_signing_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "keys.signing.list_.0"
    client = get_client(test_id)
    client.keys.signing.list()
    verify_request_count(test_id, "GET", "/keys/signing", None, 1)


def test_keys_signing_rotate() -> None:
    """Test rotate endpoint with WireMock"""
    test_id = "keys.signing.rotate.0"
    client = get_client(test_id)
    client.keys.signing.rotate()
    verify_request_count(test_id, "POST", "/keys/signing/rotate", None, 1)


def test_keys_signing_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "keys.signing.get.0"
    client = get_client(test_id)
    client.keys.signing.get(kid="kid")
    verify_request_count(test_id, "GET", "/keys/signing/kid", None, 1)


def test_keys_signing_revoke() -> None:
    """Test revoke endpoint with WireMock"""
    test_id = "keys.signing.revoke.0"
    client = get_client(test_id)
    client.keys.signing.revoke(kid="kid")
    verify_request_count(test_id, "PUT", "/keys/signing/kid/revoke", None, 1)
