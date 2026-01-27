from .conftest import get_client, verify_request_count


def test_userBlocks_list_by_identifier() -> None:
    """Test listByIdentifier endpoint with WireMock"""
    test_id = "user_blocks.list_by_identifier.0"
    client = get_client(test_id)
    client.user_blocks.list_by_identifier(identifier="identifier", consider_brute_force_enablement=True)
    verify_request_count(
        test_id, "GET", "/user-blocks", {"identifier": "identifier", "consider_brute_force_enablement": "true"}, 1
    )


def test_userBlocks_delete_by_identifier() -> None:
    """Test deleteByIdentifier endpoint with WireMock"""
    test_id = "user_blocks.delete_by_identifier.0"
    client = get_client(test_id)
    client.user_blocks.delete_by_identifier(identifier="identifier")
    verify_request_count(test_id, "DELETE", "/user-blocks", {"identifier": "identifier"}, 1)


def test_userBlocks_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "user_blocks.list_.0"
    client = get_client(test_id)
    client.user_blocks.list(id="id", consider_brute_force_enablement=True)
    verify_request_count(test_id, "GET", "/user-blocks/id", {"consider_brute_force_enablement": "true"}, 1)


def test_userBlocks_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "user_blocks.delete.0"
    client = get_client(test_id)
    client.user_blocks.delete(id="id")
    verify_request_count(test_id, "DELETE", "/user-blocks/id", None, 1)
