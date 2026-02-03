from .conftest import get_client, verify_request_count


def test_groups_members_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "groups.members.get.0"
    client = get_client(test_id)
    client.groups.members.get(id="id", fields="fields", include_fields=True, from_="from", take=1)
    verify_request_count(
        test_id,
        "GET",
        "/groups/id/members",
        {"fields": "fields", "include_fields": "true", "from": "from", "take": "1"},
        1,
    )
