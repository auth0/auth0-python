from .conftest import get_client, verify_request_count


def test_groups_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "groups.list_.0"
    client = get_client(test_id)
    client.groups.list(
        connection_id="connection_id",
        name="name",
        external_id="external_id",
        fields="fields",
        include_fields=True,
        from_="from",
        take=1,
    )
    verify_request_count(
        test_id,
        "GET",
        "/groups",
        {
            "connection_id": "connection_id",
            "name": "name",
            "external_id": "external_id",
            "fields": "fields",
            "include_fields": "true",
            "from": "from",
            "take": "1",
        },
        1,
    )


def test_groups_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "groups.get.0"
    client = get_client(test_id)
    client.groups.get(id="id")
    verify_request_count(test_id, "GET", "/groups/id", None, 1)
