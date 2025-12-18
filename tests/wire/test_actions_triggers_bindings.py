from .conftest import get_client, verify_request_count


def test_actions_triggers_bindings_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "actions.triggers.bindings.list_.0"
    client = get_client(test_id)
    client.actions.triggers.bindings.list(trigger_id="triggerId", page=1, per_page=1)
    verify_request_count(test_id, "GET", "/actions/triggers/triggerId/bindings", {"page": "1", "per_page": "1"}, 1)


def test_actions_triggers_bindings_update_many() -> None:
    """Test updateMany endpoint with WireMock"""
    test_id = "actions.triggers.bindings.update_many.0"
    client = get_client(test_id)
    client.actions.triggers.bindings.update_many(trigger_id="triggerId")
    verify_request_count(test_id, "PATCH", "/actions/triggers/triggerId/bindings", None, 1)
