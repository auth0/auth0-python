from .conftest import get_client, verify_request_count


def test_flows_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "flows.list_.0"
    client = get_client(test_id)
    client.flows.list(page=1, per_page=1, include_totals=True, synchronous=True)
    verify_request_count(
        test_id, "GET", "/flows", {"page": "1", "per_page": "1", "include_totals": "true", "synchronous": "true"}, 1
    )


def test_flows_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "flows.create.0"
    client = get_client(test_id)
    client.flows.create(name="name")
    verify_request_count(test_id, "POST", "/flows", None, 1)


def test_flows_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "flows.get.0"
    client = get_client(test_id)
    client.flows.get(id="id")
    verify_request_count(test_id, "GET", "/flows/id", None, 1)


def test_flows_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "flows.delete.0"
    client = get_client(test_id)
    client.flows.delete(id="id")
    verify_request_count(test_id, "DELETE", "/flows/id", None, 1)


def test_flows_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "flows.update.0"
    client = get_client(test_id)
    client.flows.update(id="id")
    verify_request_count(test_id, "PATCH", "/flows/id", None, 1)
