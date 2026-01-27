from .conftest import get_client, verify_request_count


def test_actions_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "actions.list_.0"
    client = get_client(test_id)
    client.actions.list(
        trigger_id="triggerId", action_name="actionName", deployed=True, page=1, per_page=1, installed=True
    )
    verify_request_count(
        test_id,
        "GET",
        "/actions/actions",
        {
            "triggerId": "triggerId",
            "actionName": "actionName",
            "deployed": "true",
            "page": "1",
            "per_page": "1",
            "installed": "true",
        },
        1,
    )


def test_actions_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "actions.create.0"
    client = get_client(test_id)
    client.actions.create(name="name", supported_triggers=[{"id": "id"}])
    verify_request_count(test_id, "POST", "/actions/actions", None, 1)


def test_actions_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "actions.get.0"
    client = get_client(test_id)
    client.actions.get(id="id")
    verify_request_count(test_id, "GET", "/actions/actions/id", None, 1)


def test_actions_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "actions.delete.0"
    client = get_client(test_id)
    client.actions.delete(id="id", force=True)
    verify_request_count(test_id, "DELETE", "/actions/actions/id", {"force": "true"}, 1)


def test_actions_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "actions.update.0"
    client = get_client(test_id)
    client.actions.update(id="id")
    verify_request_count(test_id, "PATCH", "/actions/actions/id", None, 1)


def test_actions_deploy() -> None:
    """Test deploy endpoint with WireMock"""
    test_id = "actions.deploy.0"
    client = get_client(test_id)
    client.actions.deploy(id="id")
    verify_request_count(test_id, "POST", "/actions/actions/id/deploy", None, 1)


def test_actions_test() -> None:
    """Test test endpoint with WireMock"""
    test_id = "actions.test.0"
    client = get_client(test_id)
    client.actions.test(id="id", payload={"key": "value"})
    verify_request_count(test_id, "POST", "/actions/actions/id/test", None, 1)
