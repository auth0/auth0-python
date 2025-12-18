from .conftest import get_client, verify_request_count


def test_organizations_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.list_.0"
    client = get_client(test_id)
    client.organizations.list(from_="from", take=1, sort="sort")
    verify_request_count(test_id, "GET", "/organizations", {"from": "from", "take": "1", "sort": "sort"}, 1)


def test_organizations_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organizations.create.0"
    client = get_client(test_id)
    client.organizations.create(name="name")
    verify_request_count(test_id, "POST", "/organizations", None, 1)


def test_organizations_get_by_name() -> None:
    """Test getByName endpoint with WireMock"""
    test_id = "organizations.get_by_name.0"
    client = get_client(test_id)
    client.organizations.get_by_name(name="name")
    verify_request_count(test_id, "GET", "/organizations/name/name", None, 1)


def test_organizations_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organizations.get.0"
    client = get_client(test_id)
    client.organizations.get(id="id")
    verify_request_count(test_id, "GET", "/organizations/id", None, 1)


def test_organizations_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organizations.delete.0"
    client = get_client(test_id)
    client.organizations.delete(id="id")
    verify_request_count(test_id, "DELETE", "/organizations/id", None, 1)


def test_organizations_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "organizations.update.0"
    client = get_client(test_id)
    client.organizations.update(id="id")
    verify_request_count(test_id, "PATCH", "/organizations/id", None, 1)
