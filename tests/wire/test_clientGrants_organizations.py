from .conftest import get_client, verify_request_count


def test_clientGrants_organizations_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "client_grants.organizations.list_.0"
    client = get_client(test_id)
    client.client_grants.organizations.list(id="id", from_="from", take=1)
    verify_request_count(test_id, "GET", "/client-grants/id/organizations", {"from": "from", "take": "1"}, 1)
