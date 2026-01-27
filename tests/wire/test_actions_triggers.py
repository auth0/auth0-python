from .conftest import get_client, verify_request_count


def test_actions_triggers_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "actions.triggers.list_.0"
    client = get_client(test_id)
    client.actions.triggers.list()
    verify_request_count(test_id, "GET", "/actions/triggers", None, 1)
