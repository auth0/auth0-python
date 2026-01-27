from .conftest import get_client, verify_request_count


def test_customDomains_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "custom_domains.list_.0"
    client = get_client(test_id)
    client.custom_domains.list(take=1, from_="from", q="q", fields="fields", include_fields=True, sort="sort")
    verify_request_count(
        test_id,
        "GET",
        "/custom-domains",
        {"take": "1", "from": "from", "q": "q", "fields": "fields", "include_fields": "true", "sort": "sort"},
        1,
    )


def test_customDomains_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "custom_domains.create.0"
    client = get_client(test_id)
    client.custom_domains.create(domain="domain", type="auth0_managed_certs")
    verify_request_count(test_id, "POST", "/custom-domains", None, 1)


def test_customDomains_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "custom_domains.get.0"
    client = get_client(test_id)
    client.custom_domains.get(id="id")
    verify_request_count(test_id, "GET", "/custom-domains/id", None, 1)


def test_customDomains_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "custom_domains.delete.0"
    client = get_client(test_id)
    client.custom_domains.delete(id="id")
    verify_request_count(test_id, "DELETE", "/custom-domains/id", None, 1)


def test_customDomains_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "custom_domains.update.0"
    client = get_client(test_id)
    client.custom_domains.update(id="id")
    verify_request_count(test_id, "PATCH", "/custom-domains/id", None, 1)


def test_customDomains_test() -> None:
    """Test test endpoint with WireMock"""
    test_id = "custom_domains.test.0"
    client = get_client(test_id)
    client.custom_domains.test(id="id")
    verify_request_count(test_id, "POST", "/custom-domains/id/test", None, 1)


def test_customDomains_verify() -> None:
    """Test verify endpoint with WireMock"""
    test_id = "custom_domains.verify.0"
    client = get_client(test_id)
    client.custom_domains.verify(id="id")
    verify_request_count(test_id, "POST", "/custom-domains/id/verify", None, 1)
