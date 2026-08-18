from .conftest import get_client, verify_request_count


def test_keys_networkAcls_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "keys.network_acls.list_.0"
    client = get_client(test_id)
    client.keys.network_acls.list()
    verify_request_count(test_id, "GET", "/keys/network-acls", None, 1)


def test_keys_networkAcls_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "keys.network_acls.create.0"
    client = get_client(test_id)
    client.keys.network_acls.create(
        name="name",
        alg="hmac-sha256",
        value="value",
    )
    verify_request_count(test_id, "POST", "/keys/network-acls", None, 1)


def test_keys_networkAcls_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "keys.network_acls.get.0"
    client = get_client(test_id)
    client.keys.network_acls.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/keys/network-acls/id", None, 1)
