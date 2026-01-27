from .conftest import get_client, verify_request_count


def test_users_authenticators_delete_all() -> None:
    """Test deleteAll endpoint with WireMock"""
    test_id = "users.authenticators.delete_all.0"
    client = get_client(test_id)
    client.users.authenticators.delete_all(id="id")
    verify_request_count(test_id, "DELETE", "/users/id/authenticators", None, 1)
