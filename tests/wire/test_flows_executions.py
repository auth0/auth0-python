from .conftest import get_client, verify_request_count


def test_flows_executions_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "flows.executions.list_.0"
    client = get_client(test_id)
    client.flows.executions.list(flow_id="flow_id", from_="from", take=1)
    verify_request_count(test_id, "GET", "/flows/flow_id/executions", {"from": "from", "take": "1"}, 1)


def test_flows_executions_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "flows.executions.get.0"
    client = get_client(test_id)
    client.flows.executions.get(flow_id="flow_id", execution_id="execution_id")
    verify_request_count(test_id, "GET", "/flows/flow_id/executions/execution_id", None, 1)


def test_flows_executions_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "flows.executions.delete.0"
    client = get_client(test_id)
    client.flows.executions.delete(flow_id="flow_id", execution_id="execution_id")
    verify_request_count(test_id, "DELETE", "/flows/flow_id/executions/execution_id", None, 1)
