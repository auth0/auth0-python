from .conftest import get_client, verify_request_count


def test_tokenExchangeProfiles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "token_exchange_profiles.list_.0"
    client = get_client(test_id)
    client.token_exchange_profiles.list(from_="from", take=1)
    verify_request_count(test_id, "GET", "/token-exchange-profiles", {"from": "from", "take": "1"}, 1)


def test_tokenExchangeProfiles_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "token_exchange_profiles.create.0"
    client = get_client(test_id)
    client.token_exchange_profiles.create(name="name", subject_token_type="subject_token_type", action_id="action_id")
    verify_request_count(test_id, "POST", "/token-exchange-profiles", None, 1)


def test_tokenExchangeProfiles_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "token_exchange_profiles.get.0"
    client = get_client(test_id)
    client.token_exchange_profiles.get(id="id")
    verify_request_count(test_id, "GET", "/token-exchange-profiles/id", None, 1)


def test_tokenExchangeProfiles_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "token_exchange_profiles.delete.0"
    client = get_client(test_id)
    client.token_exchange_profiles.delete(id="id")
    verify_request_count(test_id, "DELETE", "/token-exchange-profiles/id", None, 1)


def test_tokenExchangeProfiles_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "token_exchange_profiles.update.0"
    client = get_client(test_id)
    client.token_exchange_profiles.update(id="id")
    verify_request_count(test_id, "PATCH", "/token-exchange-profiles/id", None, 1)
