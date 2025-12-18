from .conftest import get_client, verify_request_count


def test_actions_versions_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "actions.versions.list_.0"
    client = get_client(test_id)
    client.actions.versions.list(action_id="actionId", page=1, per_page=1)
    verify_request_count(test_id, "GET", "/actions/actions/actionId/versions", {"page": "1", "per_page": "1"}, 1)


def test_actions_versions_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "actions.versions.get.0"
    client = get_client(test_id)
    client.actions.versions.get(action_id="actionId", id="id")
    verify_request_count(test_id, "GET", "/actions/actions/actionId/versions/id", None, 1)


def test_actions_versions_deploy() -> None:
    """Test deploy endpoint with WireMock"""
    test_id = "actions.versions.deploy.0"
    client = get_client(test_id)
    client.actions.versions.deploy(action_id="actionId", id="id", request={})
    verify_request_count(test_id, "POST", "/actions/actions/actionId/versions/id/deploy", None, 1)
