from .conftest import get_client, verify_request_count


def test_forms_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "forms.list_.0"
    client = get_client(test_id)
    client.forms.list(page=1, per_page=1, include_totals=True)
    verify_request_count(test_id, "GET", "/forms", {"page": "1", "per_page": "1", "include_totals": "true"}, 1)


def test_forms_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "forms.create.0"
    client = get_client(test_id)
    client.forms.create(name="name")
    verify_request_count(test_id, "POST", "/forms", None, 1)


def test_forms_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "forms.get.0"
    client = get_client(test_id)
    client.forms.get(id="id")
    verify_request_count(test_id, "GET", "/forms/id", None, 1)


def test_forms_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "forms.delete.0"
    client = get_client(test_id)
    client.forms.delete(id="id")
    verify_request_count(test_id, "DELETE", "/forms/id", None, 1)


def test_forms_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "forms.update.0"
    client = get_client(test_id)
    client.forms.update(id="id")
    verify_request_count(test_id, "PATCH", "/forms/id", None, 1)
