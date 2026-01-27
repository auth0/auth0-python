from .conftest import get_client, verify_request_count


def test_clientGrants_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "client_grants.list_.0"
    client = get_client(test_id)
    client.client_grants.list(
        from_="from",
        take=1,
        audience="audience",
        client_id="client_id",
        allow_any_organization=True,
        subject_type="client",
    )
    verify_request_count(
        test_id,
        "GET",
        "/client-grants",
        {
            "from": "from",
            "take": "1",
            "audience": "audience",
            "client_id": "client_id",
            "allow_any_organization": "true",
            "subject_type": "client",
        },
        1,
    )


def test_clientGrants_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "client_grants.create.0"
    client = get_client(test_id)
    client.client_grants.create(client_id="client_id", audience="audience")
    verify_request_count(test_id, "POST", "/client-grants", None, 1)


def test_clientGrants_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "client_grants.delete.0"
    client = get_client(test_id)
    client.client_grants.delete(id="id")
    verify_request_count(test_id, "DELETE", "/client-grants/id", None, 1)


def test_clientGrants_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "client_grants.update.0"
    client = get_client(test_id)
    client.client_grants.update(id="id")
    verify_request_count(test_id, "PATCH", "/client-grants/id", None, 1)
