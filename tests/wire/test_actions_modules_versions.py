from .conftest import get_client, verify_request_count


def test_actions_modules_versions_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "actions.modules.versions.list_.0"
    client = get_client(test_id)
    client.actions.modules.versions.list(id="id")
    verify_request_count(test_id, "GET", "/actions/modules/id/versions", None, 1)


def test_actions_modules_versions_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "actions.modules.versions.create.0"
    client = get_client(test_id)
    client.actions.modules.versions.create(id="id")
    verify_request_count(test_id, "POST", "/actions/modules/id/versions", None, 1)


def test_actions_modules_versions_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "actions.modules.versions.get.0"
    client = get_client(test_id)
    client.actions.modules.versions.get(id="id", version_id="versionId")
    verify_request_count(test_id, "GET", "/actions/modules/id/versions/versionId", None, 1)
