from .conftest import get_client, verify_request_count


def test_connectionProfiles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "connection_profiles.list_.0"
    client = get_client(test_id)
    client.connection_profiles.list(from_="from", take=1)
    verify_request_count(test_id, "GET", "/connection-profiles", {"from": "from", "take": "1"}, 1)


def test_connectionProfiles_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "connection_profiles.create.0"
    client = get_client(test_id)
    client.connection_profiles.create(name="name")
    verify_request_count(test_id, "POST", "/connection-profiles", None, 1)


def test_connectionProfiles_list_templates() -> None:
    """Test listTemplates endpoint with WireMock"""
    test_id = "connection_profiles.list_templates.0"
    client = get_client(test_id)
    client.connection_profiles.list_templates()
    verify_request_count(test_id, "GET", "/connection-profiles/templates", None, 1)


def test_connectionProfiles_get_template() -> None:
    """Test getTemplate endpoint with WireMock"""
    test_id = "connection_profiles.get_template.0"
    client = get_client(test_id)
    client.connection_profiles.get_template(id="id")
    verify_request_count(test_id, "GET", "/connection-profiles/templates/id", None, 1)


def test_connectionProfiles_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "connection_profiles.get.0"
    client = get_client(test_id)
    client.connection_profiles.get(id="id")
    verify_request_count(test_id, "GET", "/connection-profiles/id", None, 1)


def test_connectionProfiles_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "connection_profiles.delete.0"
    client = get_client(test_id)
    client.connection_profiles.delete(id="id")
    verify_request_count(test_id, "DELETE", "/connection-profiles/id", None, 1)


def test_connectionProfiles_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "connection_profiles.update.0"
    client = get_client(test_id)
    client.connection_profiles.update(id="id")
    verify_request_count(test_id, "PATCH", "/connection-profiles/id", None, 1)
