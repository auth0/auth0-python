from .conftest import get_client, verify_request_count


def test_networkAcls_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "network_acls.list_.0"
    client = get_client(test_id)
    client.network_acls.list(page=1, per_page=1, include_totals=True)
    verify_request_count(test_id, "GET", "/network-acls", {"page": "1", "per_page": "1", "include_totals": "true"}, 1)


def test_networkAcls_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "network_acls.create.0"
    client = get_client(test_id)
    client.network_acls.create(
        description="description", active=True, priority=1.1, rule={"action": {}, "scope": "management"}
    )
    verify_request_count(test_id, "POST", "/network-acls", None, 1)


def test_networkAcls_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "network_acls.get.0"
    client = get_client(test_id)
    client.network_acls.get(id="id")
    verify_request_count(test_id, "GET", "/network-acls/id", None, 1)


def test_networkAcls_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "network_acls.set_.0"
    client = get_client(test_id)
    client.network_acls.set(
        id="id", description="description", active=True, priority=1.1, rule={"action": {}, "scope": "management"}
    )
    verify_request_count(test_id, "PUT", "/network-acls/id", None, 1)


def test_networkAcls_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "network_acls.delete.0"
    client = get_client(test_id)
    client.network_acls.delete(id="id")
    verify_request_count(test_id, "DELETE", "/network-acls/id", None, 1)


def test_networkAcls_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "network_acls.update.0"
    client = get_client(test_id)
    client.network_acls.update(id="id")
    verify_request_count(test_id, "PATCH", "/network-acls/id", None, 1)
