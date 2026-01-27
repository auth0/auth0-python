from .conftest import get_client, verify_request_count


def test_organizations_discoveryDomains_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organizations.discovery_domains.list_.0"
    client = get_client(test_id)
    client.organizations.discovery_domains.list(id="id", from_="from", take=1)
    verify_request_count(test_id, "GET", "/organizations/id/discovery-domains", {"from": "from", "take": "1"}, 1)


def test_organizations_discoveryDomains_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organizations.discovery_domains.create.0"
    client = get_client(test_id)
    client.organizations.discovery_domains.create(id="id", domain="domain")
    verify_request_count(test_id, "POST", "/organizations/id/discovery-domains", None, 1)


def test_organizations_discoveryDomains_get_by_name() -> None:
    """Test getByName endpoint with WireMock"""
    test_id = "organizations.discovery_domains.get_by_name.0"
    client = get_client(test_id)
    client.organizations.discovery_domains.get_by_name(id="id", discovery_domain="discovery_domain")
    verify_request_count(test_id, "GET", "/organizations/id/discovery-domains/name/discovery_domain", None, 1)


def test_organizations_discoveryDomains_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organizations.discovery_domains.get.0"
    client = get_client(test_id)
    client.organizations.discovery_domains.get(id="id", discovery_domain_id="discovery_domain_id")
    verify_request_count(test_id, "GET", "/organizations/id/discovery-domains/discovery_domain_id", None, 1)


def test_organizations_discoveryDomains_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organizations.discovery_domains.delete.0"
    client = get_client(test_id)
    client.organizations.discovery_domains.delete(id="id", discovery_domain_id="discovery_domain_id")
    verify_request_count(test_id, "DELETE", "/organizations/id/discovery-domains/discovery_domain_id", None, 1)


def test_organizations_discoveryDomains_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "organizations.discovery_domains.update.0"
    client = get_client(test_id)
    client.organizations.discovery_domains.update(id="id", discovery_domain_id="discovery_domain_id")
    verify_request_count(test_id, "PATCH", "/organizations/id/discovery-domains/discovery_domain_id", None, 1)
