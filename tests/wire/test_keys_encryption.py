from .conftest import get_client, verify_request_count


def test_keys_encryption_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "keys.encryption.list_.0"
    client = get_client(test_id)
    client.keys.encryption.list(page=1, per_page=1, include_totals=True)
    verify_request_count(
        test_id, "GET", "/keys/encryption", {"page": "1", "per_page": "1", "include_totals": "true"}, 1
    )


def test_keys_encryption_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "keys.encryption.create.0"
    client = get_client(test_id)
    client.keys.encryption.create(type="customer-provided-root-key")
    verify_request_count(test_id, "POST", "/keys/encryption", None, 1)


def test_keys_encryption_rekey() -> None:
    """Test rekey endpoint with WireMock"""
    test_id = "keys.encryption.rekey.0"
    client = get_client(test_id)
    client.keys.encryption.rekey()
    verify_request_count(test_id, "POST", "/keys/encryption/rekey", None, 1)


def test_keys_encryption_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "keys.encryption.get.0"
    client = get_client(test_id)
    client.keys.encryption.get(kid="kid")
    verify_request_count(test_id, "GET", "/keys/encryption/kid", None, 1)


def test_keys_encryption_import_() -> None:
    """Test import endpoint with WireMock"""
    test_id = "keys.encryption.import_.0"
    client = get_client(test_id)
    client.keys.encryption.import_(kid="kid", wrapped_key="wrapped_key")
    verify_request_count(test_id, "POST", "/keys/encryption/kid", None, 1)


def test_keys_encryption_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "keys.encryption.delete.0"
    client = get_client(test_id)
    client.keys.encryption.delete(kid="kid")
    verify_request_count(test_id, "DELETE", "/keys/encryption/kid", None, 1)


def test_keys_encryption_create_public_wrapping_key() -> None:
    """Test createPublicWrappingKey endpoint with WireMock"""
    test_id = "keys.encryption.create_public_wrapping_key.0"
    client = get_client(test_id)
    client.keys.encryption.create_public_wrapping_key(kid="kid")
    verify_request_count(test_id, "POST", "/keys/encryption/kid/wrapping-key", None, 1)
