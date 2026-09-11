from .conftest import get_client, verify_request_count

from auth0.management import PatchRateLimitPolicyConfigurationRequestContentZero, RateLimitPolicyConfigurationZero


def test_rateLimitPolicies_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "rate_limit_policies.list_.0"
    client = get_client(test_id)
    client.rate_limit_policies.list(
        resource="oauth_authentication_api",
        consumer="client",
        consumer_selector="consumer_selector",
        take=1,
        from_="from",
    )
    verify_request_count(
        test_id,
        "GET",
        "/rate-limit-policies",
        {
            "resource": "oauth_authentication_api",
            "consumer": "client",
            "consumer_selector": "consumer_selector",
            "take": "1",
            "from": "from",
        },
        1,
    )


def test_rateLimitPolicies_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "rate_limit_policies.create.0"
    client = get_client(test_id)
    client.rate_limit_policies.create(
        resource="oauth_authentication_api",
        consumer="client",
        consumer_selector="consumer_selector",
        configuration=RateLimitPolicyConfigurationZero(
            action="allow",
        ),
    )
    verify_request_count(test_id, "POST", "/rate-limit-policies", None, 1)


def test_rateLimitPolicies_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "rate_limit_policies.get.0"
    client = get_client(test_id)
    client.rate_limit_policies.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/rate-limit-policies/id", None, 1)


def test_rateLimitPolicies_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "rate_limit_policies.delete.0"
    client = get_client(test_id)
    client.rate_limit_policies.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/rate-limit-policies/id", None, 1)


def test_rateLimitPolicies_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "rate_limit_policies.update.0"
    client = get_client(test_id)
    client.rate_limit_policies.update(
        id="id",
        configuration=PatchRateLimitPolicyConfigurationRequestContentZero(
            action="allow",
        ),
    )
    verify_request_count(test_id, "PATCH", "/rate-limit-policies/id", None, 1)
