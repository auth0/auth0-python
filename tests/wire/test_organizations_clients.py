from .conftest import get_client, verify_request_count

from auth0.management import CreateOrganizationClientRequestItem


def test_organizations_clients_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.clients.list_.0"
    client = get_client(test_id)
    client.organizations.clients.list(
        id="id",
        from_="from",
        take=1,
    )
    verify_request_count(test_id, "GET", "/organizations/id/clients", {"from": "from", "take": "1"}, 1)


def test_organizations_clients_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organizations.clients.create.0"
    client = get_client(test_id)
    client.organizations.clients.create(
        id="id",
        clients=[
            CreateOrganizationClientRequestItem(
                client_id="client_id",
                use_for_member_access=True,
            )
        ],
    )
    verify_request_count(test_id, "POST", "/organizations/id/clients", None, 1)


def test_organizations_clients_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organizations.clients.delete.0"
    client = get_client(test_id)
    client.organizations.clients.delete(
        id="id",
        clients=["clients"],
    )
    verify_request_count(test_id, "DELETE", "/organizations/id/clients", None, 1)


def test_organizations_clients_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organizations.clients.get.0"
    client = get_client(test_id)
    client.organizations.clients.get(
        id="id",
        client_id="client_id",
    )
    verify_request_count(test_id, "GET", "/organizations/id/clients/client_id", None, 1)


def test_organizations_clients_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "organizations.clients.update.0"
    client = get_client(test_id)
    client.organizations.clients.update(
        id="id",
        client_id="client_id",
    )
    verify_request_count(test_id, "PATCH", "/organizations/id/clients/client_id", None, 1)
