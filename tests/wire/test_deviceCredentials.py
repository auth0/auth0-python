from .conftest import get_client, verify_request_count


def test_deviceCredentials_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "device_credentials.list_.0"
    client = get_client(test_id)
    client.device_credentials.list(
        page=1,
        per_page=1,
        include_totals=True,
        fields="fields",
        include_fields=True,
        user_id="user_id",
        client_id="client_id",
        type="public_key",
    )
    verify_request_count(
        test_id,
        "GET",
        "/device-credentials",
        {
            "page": "1",
            "per_page": "1",
            "include_totals": "true",
            "fields": "fields",
            "include_fields": "true",
            "user_id": "user_id",
            "client_id": "client_id",
            "type": "public_key",
        },
        1,
    )


def test_deviceCredentials_create_public_key() -> None:
    """Test createPublicKey endpoint with WireMock"""
    test_id = "device_credentials.create_public_key.0"
    client = get_client(test_id)
    client.device_credentials.create_public_key(
        device_name="device_name", type="public_key", value="value", device_id="device_id"
    )
    verify_request_count(test_id, "POST", "/device-credentials", None, 1)


def test_deviceCredentials_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "device_credentials.delete.0"
    client = get_client(test_id)
    client.device_credentials.delete(id="id")
    verify_request_count(test_id, "DELETE", "/device-credentials/id", None, 1)
