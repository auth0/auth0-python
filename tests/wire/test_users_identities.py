from .conftest import get_client, verify_request_count


def test_users_identities_link() -> None:
    """Test link endpoint with WireMock"""
    test_id = "users.identities.link.0"
    client = get_client(test_id)
    client.users.identities.link(id="id")
    verify_request_count(test_id, "POST", "/users/id/identities", None, 1)


def test_users_identities_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "users.identities.delete.0"
    client = get_client(test_id)
    client.users.identities.delete(id="id", provider="ad", user_id="user_id")
    verify_request_count(test_id, "DELETE", "/users/id/identities/ad/user_id", None, 1)
