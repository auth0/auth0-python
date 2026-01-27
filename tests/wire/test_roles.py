from .conftest import get_client, verify_request_count


def test_roles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "roles.list_.0"
    client = get_client(test_id)
    client.roles.list(per_page=1, page=1, include_totals=True, name_filter="name_filter")
    verify_request_count(
        test_id,
        "GET",
        "/roles",
        {"per_page": "1", "page": "1", "include_totals": "true", "name_filter": "name_filter"},
        1,
    )


def test_roles_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "roles.create.0"
    client = get_client(test_id)
    client.roles.create(name="name")
    verify_request_count(test_id, "POST", "/roles", None, 1)


def test_roles_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "roles.get.0"
    client = get_client(test_id)
    client.roles.get(id="id")
    verify_request_count(test_id, "GET", "/roles/id", None, 1)


def test_roles_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "roles.delete.0"
    client = get_client(test_id)
    client.roles.delete(id="id")
    verify_request_count(test_id, "DELETE", "/roles/id", None, 1)


def test_roles_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "roles.update.0"
    client = get_client(test_id)
    client.roles.update(id="id")
    verify_request_count(test_id, "PATCH", "/roles/id", None, 1)
