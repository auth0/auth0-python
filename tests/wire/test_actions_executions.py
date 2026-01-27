from .conftest import get_client, verify_request_count


def test_actions_executions_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "actions.executions.get.0"
    client = get_client(test_id)
    client.actions.executions.get(id="id")
    verify_request_count(test_id, "GET", "/actions/executions/id", None, 1)
