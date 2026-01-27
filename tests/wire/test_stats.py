from .conftest import get_client, verify_request_count


def test_stats_get_active_users_count() -> None:
    """Test getActiveUsersCount endpoint with WireMock"""
    test_id = "stats.get_active_users_count.0"
    client = get_client(test_id)
    client.stats.get_active_users_count()
    verify_request_count(test_id, "GET", "/stats/active-users", None, 1)


def test_stats_get_daily() -> None:
    """Test getDaily endpoint with WireMock"""
    test_id = "stats.get_daily.0"
    client = get_client(test_id)
    client.stats.get_daily(from_="from", to="to")
    verify_request_count(test_id, "GET", "/stats/daily", {"from": "from", "to": "to"}, 1)
