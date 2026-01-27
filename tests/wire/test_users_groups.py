from .conftest import get_client, verify_request_count


def test_users_groups_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "users.groups.get.0"
    client = get_client(test_id)
    client.users.groups.get(id="id", fields="fields", include_fields=True, from_="from", take=1)
    verify_request_count(
        test_id,
        "GET",
        "/users/id/groups",
        {"fields": "fields", "include_fields": "true", "from": "from", "take": "1"},
        1,
    )
