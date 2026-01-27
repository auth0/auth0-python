from .conftest import get_client, verify_request_count


def test_selfServiceProfiles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "self_service_profiles.list_.0"
    client = get_client(test_id)
    client.self_service_profiles.list(page=1, per_page=1, include_totals=True)
    verify_request_count(
        test_id, "GET", "/self-service-profiles", {"page": "1", "per_page": "1", "include_totals": "true"}, 1
    )


def test_selfServiceProfiles_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "self_service_profiles.create.0"
    client = get_client(test_id)
    client.self_service_profiles.create(name="name")
    verify_request_count(test_id, "POST", "/self-service-profiles", None, 1)


def test_selfServiceProfiles_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "self_service_profiles.get.0"
    client = get_client(test_id)
    client.self_service_profiles.get(id="id")
    verify_request_count(test_id, "GET", "/self-service-profiles/id", None, 1)


def test_selfServiceProfiles_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "self_service_profiles.delete.0"
    client = get_client(test_id)
    client.self_service_profiles.delete(id="id")
    verify_request_count(test_id, "DELETE", "/self-service-profiles/id", None, 1)


def test_selfServiceProfiles_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "self_service_profiles.update.0"
    client = get_client(test_id)
    client.self_service_profiles.update(id="id")
    verify_request_count(test_id, "PATCH", "/self-service-profiles/id", None, 1)
