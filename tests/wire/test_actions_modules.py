from .conftest import get_client, verify_request_count


def test_actions_modules_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "actions.modules.list_.0"
    client = get_client(test_id)
    client.actions.modules.list(page=1, per_page=1)
    verify_request_count(test_id, "GET", "/actions/modules", {"page": "1", "per_page": "1"}, 1)


def test_actions_modules_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "actions.modules.create.0"
    client = get_client(test_id)
    client.actions.modules.create(name="name", code="code")
    verify_request_count(test_id, "POST", "/actions/modules", None, 1)


def test_actions_modules_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "actions.modules.get.0"
    client = get_client(test_id)
    client.actions.modules.get(id="id")
    verify_request_count(test_id, "GET", "/actions/modules/id", None, 1)


def test_actions_modules_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "actions.modules.delete.0"
    client = get_client(test_id)
    client.actions.modules.delete(id="id")
    verify_request_count(test_id, "DELETE", "/actions/modules/id", None, 1)


def test_actions_modules_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "actions.modules.update.0"
    client = get_client(test_id)
    client.actions.modules.update(id="id")
    verify_request_count(test_id, "PATCH", "/actions/modules/id", None, 1)


def test_actions_modules_list_actions() -> None:
    """Test listActions endpoint with WireMock"""
    test_id = "actions.modules.list_actions.0"
    client = get_client(test_id)
    client.actions.modules.list_actions(id="id", page=1, per_page=1)
    verify_request_count(test_id, "GET", "/actions/modules/id/actions", {"page": "1", "per_page": "1"}, 1)


def test_actions_modules_rollback() -> None:
    """Test rollback endpoint with WireMock"""
    test_id = "actions.modules.rollback.0"
    client = get_client(test_id)
    client.actions.modules.rollback(id="id", module_version_id="module_version_id")
    verify_request_count(test_id, "POST", "/actions/modules/id/rollback", None, 1)
