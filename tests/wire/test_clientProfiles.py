from .conftest import get_client, verify_request_count

from auth0.management import ClientProfileApplyPolicy, ClientProfileClientConfiguration


def test_clientProfiles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "client_profiles.list_.0"
    client = get_client(test_id)
    client.client_profiles.list(
        from_="from",
        take=1,
    )
    verify_request_count(test_id, "GET", "/client-profiles", {"from": "from", "take": "1"}, 1)


def test_clientProfiles_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "client_profiles.create.0"
    client = get_client(test_id)
    client.client_profiles.create(
        name="name",
        client_configuration=ClientProfileClientConfiguration(),
        apply_policy=ClientProfileApplyPolicy(
            external_metadata_type="cimd",
            external_metadata_created_by="client",
        ),
    )
    verify_request_count(test_id, "POST", "/client-profiles", None, 1)


def test_clientProfiles_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "client_profiles.get.0"
    client = get_client(test_id)
    client.client_profiles.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/client-profiles/id", None, 1)


def test_clientProfiles_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "client_profiles.delete.0"
    client = get_client(test_id)
    client.client_profiles.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/client-profiles/id", None, 1)


def test_clientProfiles_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "client_profiles.update.0"
    client = get_client(test_id)
    client.client_profiles.update(
        id="id",
    )
    verify_request_count(test_id, "PATCH", "/client-profiles/id", None, 1)
