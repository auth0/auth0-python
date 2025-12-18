from .conftest import get_client, verify_request_count


def test_organizations_clientGrants_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.client_grants.list_.0"
    client = get_client(test_id)
    client.organizations.client_grants.list(
        id="id", audience="audience", client_id="client_id", page=1, per_page=1, include_totals=True
    )
    verify_request_count(
        test_id,
        "GET",
        "/organizations/id/client-grants",
        {"audience": "audience", "client_id": "client_id", "page": "1", "per_page": "1", "include_totals": "true"},
        1,
    )


def test_organizations_clientGrants_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organizations.client_grants.create.0"
    client = get_client(test_id)
    client.organizations.client_grants.create(id="id", grant_id="grant_id")
    verify_request_count(test_id, "POST", "/organizations/id/client-grants", None, 1)


def test_organizations_clientGrants_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organizations.client_grants.delete.0"
    client = get_client(test_id)
    client.organizations.client_grants.delete(id="id", grant_id="grant_id")
    verify_request_count(test_id, "DELETE", "/organizations/id/client-grants/grant_id", None, 1)
