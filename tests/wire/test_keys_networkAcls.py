from .conftest import get_client, verify_request_count


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
