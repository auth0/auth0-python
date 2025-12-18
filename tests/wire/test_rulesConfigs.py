from .conftest import get_client, verify_request_count


def test_rulesConfigs_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "rules_configs.list_.0"
    client = get_client(test_id)
    client.rules_configs.list()
    verify_request_count(test_id, "GET", "/rules-configs", None, 1)


def test_rulesConfigs_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "rules_configs.set_.0"
    client = get_client(test_id)
    client.rules_configs.set(key="key", value="value")
    verify_request_count(test_id, "PUT", "/rules-configs/key", None, 1)


def test_rulesConfigs_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "rules_configs.delete.0"
    client = get_client(test_id)
    client.rules_configs.delete(key="key")
    verify_request_count(test_id, "DELETE", "/rules-configs/key", None, 1)
