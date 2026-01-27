from .conftest import get_client, verify_request_count


def test_connections_users_delete_by_email() -> None:
    """Test deleteByEmail endpoint with WireMock"""
    test_id = "connections.users.delete_by_email.0"
    client = get_client(test_id)
    client.connections.users.delete_by_email(id="id", email="email")
    verify_request_count(test_id, "DELETE", "/connections/id/users", {"email": "email"}, 1)
