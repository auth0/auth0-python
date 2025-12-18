from .conftest import get_client, verify_request_count


def test_userGrants_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "user_grants.list_.0"
    client = get_client(test_id)
    client.user_grants.list(
        per_page=1, page=1, include_totals=True, user_id="user_id", client_id="client_id", audience="audience"
    )
    verify_request_count(
        test_id,
        "GET",
        "/grants",
        {
            "per_page": "1",
            "page": "1",
            "include_totals": "true",
            "user_id": "user_id",
            "client_id": "client_id",
            "audience": "audience",
        },
        1,
    )


def test_userGrants_delete_by_user_id() -> None:
    """Test deleteByUserId endpoint with WireMock"""
    test_id = "user_grants.delete_by_user_id.0"
    client = get_client(test_id)
    client.user_grants.delete_by_user_id(user_id="user_id")
    verify_request_count(test_id, "DELETE", "/grants", {"user_id": "user_id"}, 1)


def test_userGrants_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "user_grants.delete.0"
    client = get_client(test_id)
    client.user_grants.delete(id="id")
    verify_request_count(test_id, "DELETE", "/grants/id", None, 1)
