import time
from unittest.mock import MagicMock, patch

import pytest

from auth0.management import AsyncManagementClient, AsyncTokenProvider, ManagementClient, TokenProvider


class TestManagementClientInit:
    """Tests for ManagementClient initialization."""

    def test_init_with_token_string(self):
        """Should initialize with a static token string."""
        client = ManagementClient(
            domain="test.auth0.com",
            token="my-test-token",
        )
        assert client._api is not None

    def test_init_with_token_callable(self):
        """Should initialize with a token callable."""
        token_fn = lambda: "dynamic-token"
        client = ManagementClient(
            domain="test.auth0.com",
            token=token_fn,
        )
        assert client._api is not None

    def test_init_with_client_credentials(self):
        """Should initialize with client_id and client_secret."""
        client = ManagementClient(
            domain="test.auth0.com",
            client_id="my-client-id",
            client_secret="my-client-secret",
        )
        assert client._api is not None

    def test_init_with_custom_audience(self):
        """Should initialize with a custom audience."""
        client = ManagementClient(
            domain="test.auth0.com",
            client_id="my-client-id",
            client_secret="my-client-secret",
            audience="https://custom-api.example.com/",
        )
        assert client._api is not None

    def test_init_requires_auth(self):
        """Should raise ValueError when no auth is provided."""
        with pytest.raises(ValueError) as exc_info:
            ManagementClient(domain="test.auth0.com")
        assert "token" in str(exc_info.value)
        assert "client_id" in str(exc_info.value)

    def test_init_requires_both_credentials(self):
        """Should raise ValueError when only client_id is provided."""
        with pytest.raises(ValueError):
            ManagementClient(
                domain="test.auth0.com",
                client_id="my-client-id",
            )

    def test_init_with_custom_timeout(self):
        """Should initialize with custom timeout."""
        client = ManagementClient(
            domain="test.auth0.com",
            token="my-token",
            timeout=30.0,
        )
        assert client._api is not None

    def test_init_with_custom_headers(self):
        """Should initialize with custom headers."""
        client = ManagementClient(
            domain="test.auth0.com",
            token="my-token",
            headers={"X-Custom-Header": "custom-value"},
        )
        assert client._api is not None


class TestManagementClientProperties:
    """Tests for ManagementClient sub-client properties."""

    @pytest.fixture
    def client(self):
        return ManagementClient(
            domain="test.auth0.com",
            token="test-token",
        )

    def test_has_users_property(self, client):
        """Should have users property."""
        assert hasattr(client, "users")

    def test_has_organizations_property(self, client):
        """Should have organizations property."""
        assert hasattr(client, "organizations")

    def test_has_actions_property(self, client):
        """Should have actions property."""
        assert hasattr(client, "actions")

    def test_has_all_expected_properties(self, client):
        """Should have all expected sub-client properties."""
        expected_properties = [
            "actions",
            "anomaly",
            "attack_protection",
            "branding",
            "client_grants",
            "clients",
            "connections",
            "custom_domains",
            "device_credentials",
            "email_templates",
            "emails",
            "event_streams",
            "flows",
            "forms",
            "guardian",
            "hooks",
            "jobs",
            "keys",
            "log_streams",
            "logs",
            "network_acls",
            "organizations",
            "prompts",
            "refresh_tokens",
            "resource_servers",
            "roles",
            "rules",
            "rules_configs",
            "self_service_profiles",
            "sessions",
            "stats",
            "supplemental_signals",
            "tenants",
            "tickets",
            "token_exchange_profiles",
            "user_blocks",
            "user_grants",
            "users",
            "verifiable_credentials",
        ]
        for prop in expected_properties:
            assert hasattr(client, prop), f"Missing property: {prop}"


class TestAsyncManagementClientInit:
    """Tests for AsyncManagementClient initialization."""

    def test_init_with_token_string(self):
        """Should initialize with a static token string."""
        client = AsyncManagementClient(
            domain="test.auth0.com",
            token="my-test-token",
        )
        assert client._api is not None

    def test_init_with_client_credentials(self):
        """Should initialize with client_id and client_secret."""
        client = AsyncManagementClient(
            domain="test.auth0.com",
            client_id="my-client-id",
            client_secret="my-client-secret",
        )
        assert client._api is not None

    def test_init_requires_auth(self):
        """Should raise ValueError when no auth is provided."""
        with pytest.raises(ValueError):
            AsyncManagementClient(domain="test.auth0.com")


class TestTokenProvider:
    """Tests for TokenProvider."""

    def test_init_with_defaults(self):
        """Should initialize with default audience."""
        provider = TokenProvider(
            domain="test.auth0.com",
            client_id="client-id",
            client_secret="client-secret",
        )
        assert provider._audience == "https://test.auth0.com/api/v2/"

    def test_init_with_custom_audience(self):
        """Should initialize with custom audience."""
        provider = TokenProvider(
            domain="test.auth0.com",
            client_id="client-id",
            client_secret="client-secret",
            audience="https://custom.api.com/",
        )
        assert provider._audience == "https://custom.api.com/"

    @patch("auth0.management.token_provider.httpx.Client")
    def test_get_token_fetches_on_first_call(self, mock_client_class):
        """Should fetch token on first call."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "access_token": "new-token",
            "expires_in": 86400,
        }
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.post.return_value = mock_response
        mock_client_class.return_value = mock_client

        provider = TokenProvider(
            domain="test.auth0.com",
            client_id="client-id",
            client_secret="client-secret",
        )
        token = provider.get_token()

        assert token == "new-token"
        mock_client.post.assert_called_once()

    @patch("auth0.management.token_provider.httpx.Client")
    def test_get_token_returns_cached_token(self, mock_client_class):
        """Should return cached token on subsequent calls."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "access_token": "cached-token",
            "expires_in": 86400,
        }
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.post.return_value = mock_response
        mock_client_class.return_value = mock_client

        provider = TokenProvider(
            domain="test.auth0.com",
            client_id="client-id",
            client_secret="client-secret",
        )

        # First call fetches
        token1 = provider.get_token()
        # Second call returns cached
        token2 = provider.get_token()

        assert token1 == token2 == "cached-token"
        # Should only fetch once
        assert mock_client.post.call_count == 1

    @patch("auth0.management.token_provider.httpx.Client")
    def test_get_token_refreshes_expired_token(self, mock_client_class):
        """Should refresh token when expired (with 10s leeway)."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "access_token": "refreshed-token",
            "expires_in": 86400,
        }
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.post.return_value = mock_response
        mock_client_class.return_value = mock_client

        provider = TokenProvider(
            domain="test.auth0.com",
            client_id="client-id",
            client_secret="client-secret",
        )

        # First call
        provider.get_token()

        # Simulate token being close to expiration (within leeway)
        provider._expires_at = time.time() + 5  # 5 seconds left, less than 10s leeway

        # This should trigger a refresh
        token = provider.get_token()

        assert token == "refreshed-token"
        assert mock_client.post.call_count == 2

    @patch("auth0.management.token_provider.httpx.Client")
    def test_token_request_payload(self, mock_client_class):
        """Should send correct payload to token endpoint."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "access_token": "token",
            "expires_in": 86400,
        }
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.post.return_value = mock_response
        mock_client_class.return_value = mock_client

        provider = TokenProvider(
            domain="test.auth0.com",
            client_id="my-client",
            client_secret="my-secret",
            audience="https://api.example.com/",
        )
        provider.get_token()

        mock_client.post.assert_called_once_with(
            "https://test.auth0.com/oauth/token",
            data={
                "grant_type": "client_credentials",
                "client_id": "my-client",
                "client_secret": "my-secret",
                "audience": "https://api.example.com/",
            },
        )


class TestAsyncTokenProvider:
    """Tests for AsyncTokenProvider."""

    def test_init_with_defaults(self):
        """Should initialize with default audience."""
        provider = AsyncTokenProvider(
            domain="test.auth0.com",
            client_id="client-id",
            client_secret="client-secret",
        )
        assert provider._audience == "https://test.auth0.com/api/v2/"

    def test_init_with_custom_audience(self):
        """Should initialize with custom audience."""
        provider = AsyncTokenProvider(
            domain="test.auth0.com",
            client_id="client-id",
            client_secret="client-secret",
            audience="https://custom.api.com/",
        )
        assert provider._audience == "https://custom.api.com/"


class TestImports:
    """Tests for module imports."""

    def test_import_from_management(self):
        """Should be able to import from auth0.management."""
        from auth0.management import (
            AsyncManagementClient,
            AsyncTokenProvider,
            ManagementClient,
            TokenProvider,
        )

        assert ManagementClient is not None
        assert AsyncManagementClient is not None
        assert TokenProvider is not None
        assert AsyncTokenProvider is not None
