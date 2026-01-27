from .conftest import get_client, verify_request_count


def test_logs_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "logs.list_.0"
    client = get_client(test_id)
    client.logs.list(
        page=1, per_page=1, sort="sort", fields="fields", include_fields=True, include_totals=True, search="search"
    )
    verify_request_count(
        test_id,
        "GET",
        "/logs",
        {
            "page": "1",
            "per_page": "1",
            "sort": "sort",
            "fields": "fields",
            "include_fields": "true",
            "include_totals": "true",
            "search": "search",
        },
        1,
    )


def test_logs_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "logs.get.0"
    client = get_client(test_id)
    client.logs.get(id="id")
    verify_request_count(test_id, "GET", "/logs/id", None, 1)
