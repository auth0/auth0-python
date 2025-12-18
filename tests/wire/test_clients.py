from .conftest import get_client, verify_request_count


def test_clients_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "clients.list_.0"
    client = get_client(test_id)
    client.clients.list(
        fields="fields",
        include_fields=True,
        page=1,
        per_page=1,
        include_totals=True,
        is_global=True,
        is_first_party=True,
        app_type="app_type",
        q="q",
    )
    verify_request_count(
        test_id,
        "GET",
        "/clients",
        {
            "fields": "fields",
            "include_fields": "true",
            "page": "1",
            "per_page": "1",
            "include_totals": "true",
            "is_global": "true",
            "is_first_party": "true",
            "app_type": "app_type",
            "q": "q",
        },
        1,
    )


def test_clients_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "clients.create.0"
    client = get_client(test_id)
    client.clients.create(name="name")
    verify_request_count(test_id, "POST", "/clients", None, 1)


def test_clients_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "clients.get.0"
    client = get_client(test_id)
    client.clients.get(id="id", fields="fields", include_fields=True)
    verify_request_count(test_id, "GET", "/clients/id", {"fields": "fields", "include_fields": "true"}, 1)


def test_clients_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "clients.delete.0"
    client = get_client(test_id)
    client.clients.delete(id="id")
    verify_request_count(test_id, "DELETE", "/clients/id", None, 1)


def test_clients_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "clients.update.0"
    client = get_client(test_id)
    client.clients.update(id="id")
    verify_request_count(test_id, "PATCH", "/clients/id", None, 1)


def test_clients_rotate_secret() -> None:
    """Test rotateSecret endpoint with WireMock"""
    test_id = "clients.rotate_secret.0"
    client = get_client(test_id)
    client.clients.rotate_secret(id="id")
    verify_request_count(test_id, "POST", "/clients/id/rotate-secret", None, 1)
