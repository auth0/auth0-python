from .conftest import get_client, verify_request_count


def test_agents_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "agents.list_.0"
    client = get_client(test_id)
    client.agents.list(
        from_="from",
        take=1,
    )
    verify_request_count(test_id, "GET", "/agents", {"from": "from", "take": "1"}, 1)


def test_agents_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "agents.create.0"
    client = get_client(test_id)
    client.agents.create(
        name="name",
    )
    verify_request_count(test_id, "POST", "/agents", None, 1)


def test_agents_read() -> None:
    """Test read endpoint with WireMock"""
    test_id = "agents.read.0"
    client = get_client(test_id)
    client.agents.read(
        id="id",
    )
    verify_request_count(test_id, "GET", "/agents/id", None, 1)


def test_agents_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "agents.delete.0"
    client = get_client(test_id)
    client.agents.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/agents/id", None, 1)


def test_agents_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "agents.update.0"
    client = get_client(test_id)
    client.agents.update(
        id="id",
    )
    verify_request_count(test_id, "PATCH", "/agents/id", None, 1)
