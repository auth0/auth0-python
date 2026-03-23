import time
from unittest.mock import MagicMock, patch

import httpx
import pytest

from auth0.management import (
    AsyncManagementClient,
    AsyncTokenProvider,
    CustomDomainHeader,
    ManagementClient,
    TokenProvider,
)
from auth0.management.management_client import (
    CUSTOM_DOMAIN_HEADER as _CUSTOM_DOMAIN_HEADER,
)
from auth0.management.management_client import (
    _enforce_custom_domain_whitelist,
    _is_path_whitelisted,
)


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


class TestCustomDomainHeader:
    """Tests for Auth0-Custom-Domain header support."""

    def test_init_with_custom_domain(self):
        """Should set Auth0-Custom-Domain header when custom_domain is provided."""
        client = ManagementClient(
            domain="test.auth0.com",
            token="my-token",
            custom_domain="login.mycompany.com",
        )
        custom_headers = client._api._client_wrapper.get_custom_headers()
        assert custom_headers is not None
        assert custom_headers[_CUSTOM_DOMAIN_HEADER] == "login.mycompany.com"

    def test_init_custom_domain_with_existing_headers(self):
        """Should merge custom_domain with other custom headers."""
        client = ManagementClient(
            domain="test.auth0.com",
            token="my-token",
            headers={"X-Custom": "value"},
            custom_domain="login.mycompany.com",
        )
        custom_headers = client._api._client_wrapper.get_custom_headers()
        assert custom_headers is not None
        assert custom_headers["X-Custom"] == "value"
        assert custom_headers[_CUSTOM_DOMAIN_HEADER] == "login.mycompany.com"

    def test_init_without_custom_domain(self):
        """Should not set Auth0-Custom-Domain header when custom_domain is not provided."""
        client = ManagementClient(
            domain="test.auth0.com",
            token="my-token",
        )
        custom_headers = client._api._client_wrapper.get_custom_headers()
        assert custom_headers is None or _CUSTOM_DOMAIN_HEADER not in custom_headers

    def test_custom_domain_header_helper(self):
        """Should return correct request options dict."""
        result = CustomDomainHeader("login.mycompany.com")
        assert result == {
            "additional_headers": {
                _CUSTOM_DOMAIN_HEADER: "login.mycompany.com",
            }
        }

    def test_async_init_with_custom_domain(self):
        """Should set Auth0-Custom-Domain header on async client."""
        client = AsyncManagementClient(
            domain="test.auth0.com",
            token="my-token",
            custom_domain="login.mycompany.com",
        )
        custom_headers = client._api._client_wrapper.get_custom_headers()
        assert custom_headers is not None
        assert custom_headers[_CUSTOM_DOMAIN_HEADER] == "login.mycompany.com"

    def test_whitelist_strips_header_on_non_whitelisted_path(self):
        """Should strip Auth0-Custom-Domain header on non-whitelisted paths."""
        request = httpx.Request(
            "GET",
            "https://test.auth0.com/api/v2/clients",
            headers={_CUSTOM_DOMAIN_HEADER: "login.mycompany.com"},
        )
        _enforce_custom_domain_whitelist(request)
        assert _CUSTOM_DOMAIN_HEADER not in request.headers

    def test_whitelist_keeps_header_on_whitelisted_path(self):
        """Should keep Auth0-Custom-Domain header on whitelisted paths."""
        request = httpx.Request(
            "POST",
            "https://test.auth0.com/api/v2/users",
            headers={_CUSTOM_DOMAIN_HEADER: "login.mycompany.com"},
        )
        _enforce_custom_domain_whitelist(request)
        assert request.headers[_CUSTOM_DOMAIN_HEADER] == "login.mycompany.com"

    @pytest.mark.parametrize(
        "path",
        [
            "/api/v2/jobs/verification-email",
            "/api/v2/tickets/email-verification",
            "/api/v2/tickets/password-change",
            "/api/v2/organizations/org_abc123/invitations",
            "/api/v2/users",
            "/api/v2/users/auth0|abc123",
            "/api/v2/guardian/enrollments/ticket",
            "/api/v2/self-service-profiles/ssp_abc123/sso-ticket",
        ],
    )
    def test_whitelisted_paths_match(self, path):
        """Should match all 8 whitelisted path patterns."""
        assert _is_path_whitelisted(path) is True

    @pytest.mark.parametrize(
        "path",
        [
            "/api/v2/clients",
            "/api/v2/connections",
            "/api/v2/roles",
            "/api/v2/users/auth0|abc123/roles",
            "/api/v2/jobs/users-imports",
            "/api/v2/tenants/settings",
        ],
    )
    def test_non_whitelisted_paths_do_not_match(self, path):
        """Should not match non-whitelisted paths."""
        assert _is_path_whitelisted(path) is False


class TestImports:
    """Tests for module imports."""

    def test_import_from_management(self):
        """Should be able to import from auth0.management."""
        from auth0.management import (
            AsyncManagementClient,
            AsyncTokenProvider,
            CustomDomainHeader,
            ManagementClient,
            TokenProvider,
        )

        assert ManagementClient is not None
        assert AsyncManagementClient is not None
        assert TokenProvider is not None
        assert AsyncTokenProvider is not None
        assert CustomDomainHeader is not None
