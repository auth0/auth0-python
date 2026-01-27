from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Dict, Optional, Union

import httpx
from .client import AsyncAuth0, Auth0
from .token_provider import TokenProvider

if TYPE_CHECKING:
    from .actions.client import ActionsClient, AsyncActionsClient
    from .anomaly.client import AnomalyClient, AsyncAnomalyClient
    from .attack_protection.client import AsyncAttackProtectionClient, AttackProtectionClient
    from .branding.client import AsyncBrandingClient, BrandingClient
    from .client_grants.client import AsyncClientGrantsClient, ClientGrantsClient
    from .clients.client import AsyncClientsClient, ClientsClient
    from .connections.client import AsyncConnectionsClient, ConnectionsClient
    from .custom_domains.client import AsyncCustomDomainsClient, CustomDomainsClient
    from .device_credentials.client import AsyncDeviceCredentialsClient, DeviceCredentialsClient
    from .email_templates.client import AsyncEmailTemplatesClient, EmailTemplatesClient
    from .emails.client import AsyncEmailsClient, EmailsClient
    from .event_streams.client import AsyncEventStreamsClient, EventStreamsClient
    from .flows.client import AsyncFlowsClient, FlowsClient
    from .forms.client import AsyncFormsClient, FormsClient
    from .guardian.client import AsyncGuardianClient, GuardianClient
    from .hooks.client import AsyncHooksClient, HooksClient
    from .jobs.client import AsyncJobsClient, JobsClient
    from .keys.client import AsyncKeysClient, KeysClient
    from .log_streams.client import AsyncLogStreamsClient, LogStreamsClient
    from .logs.client import AsyncLogsClient, LogsClient
    from .network_acls.client import AsyncNetworkAclsClient, NetworkAclsClient
    from .organizations.client import AsyncOrganizationsClient, OrganizationsClient
    from .prompts.client import AsyncPromptsClient, PromptsClient
    from .refresh_tokens.client import AsyncRefreshTokensClient, RefreshTokensClient
    from .resource_servers.client import AsyncResourceServersClient, ResourceServersClient
    from .roles.client import AsyncRolesClient, RolesClient
    from .rules.client import AsyncRulesClient, RulesClient
    from .rules_configs.client import AsyncRulesConfigsClient, RulesConfigsClient
    from .self_service_profiles.client import AsyncSelfServiceProfilesClient, SelfServiceProfilesClient
    from .sessions.client import AsyncSessionsClient, SessionsClient
    from .stats.client import AsyncStatsClient, StatsClient
    from .supplemental_signals.client import AsyncSupplementalSignalsClient, SupplementalSignalsClient
    from .tenants.client import AsyncTenantsClient, TenantsClient
    from .tickets.client import AsyncTicketsClient, TicketsClient
    from .token_exchange_profiles.client import AsyncTokenExchangeProfilesClient, TokenExchangeProfilesClient
    from .user_blocks.client import AsyncUserBlocksClient, UserBlocksClient
    from .user_grants.client import AsyncUserGrantsClient, UserGrantsClient
    from .users.client import AsyncUsersClient, UsersClient
    from .verifiable_credentials.client import AsyncVerifiableCredentialsClient, VerifiableCredentialsClient


class ManagementClient:
    """
    Auth0 Management API client with automatic token management.

    Supports two initialization patterns:

    1. With an existing token:

        client = ManagementClient(
            domain="tenant.auth0.com",
            token="your_token"
        )

    2. With client credentials (automatic token acquisition and refresh):

        client = ManagementClient(
            domain="tenant.auth0.com",
            client_id="your_client_id",
            client_secret="your_client_secret"
        )

    Parameters
    ----------
    domain : str
        Your Auth0 domain (e.g., "your-tenant.auth0.com").
    token : Optional[Union[str, Callable[[], str]]]
        A static token string or a callable that returns a token.
        Required if client_id/client_secret are not provided.
    client_id : Optional[str]
        Your Auth0 application client ID.
        Required along with client_secret for automatic token acquisition.
    client_secret : Optional[str]
        Your Auth0 application client secret.
        Required along with client_id for automatic token acquisition.
    audience : Optional[str]
        The API audience. Defaults to https://{domain}/api/v2/
    headers : Optional[Dict[str, str]]
        Additional headers to send with requests.
    timeout : Optional[float]
        Request timeout in seconds. Defaults to 60.
    httpx_client : Optional[httpx.Client]
        Custom httpx client for requests.

    Raises
    ------
    ValueError
        If neither token nor client_id/client_secret are provided.
    """

    def __init__(
        self,
        *,
        domain: str,
        token: Optional[Union[str, Callable[[], str]]] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        audience: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        httpx_client: Optional[httpx.Client] = None,
    ):
        # Validate auth options
        has_token = token is not None
        has_credentials = client_id is not None and client_secret is not None

        if not has_token and not has_credentials:
            raise ValueError("Either 'token' or both 'client_id' and 'client_secret' must be provided")

        # Create token supplier
        if has_credentials and not has_token:
            provider = TokenProvider(
                domain=domain,
                client_id=client_id,  # type: ignore[arg-type]
                client_secret=client_secret,  # type: ignore[arg-type]
                audience=audience,
            )
            resolved_token: Union[str, Callable[[], str]] = provider.get_token
        else:
            resolved_token = token  # type: ignore[assignment]

        # Create underlying client
        self._api = Auth0(
            base_url=f"https://{domain}/api/v2",
            token=resolved_token,
            headers=headers,
            timeout=timeout,
            httpx_client=httpx_client,
        )

    # Forward all sub-client properties
    @property
    def actions(self) -> "ActionsClient":
        return self._api.actions

    @property
    def anomaly(self) -> "AnomalyClient":
        return self._api.anomaly

    @property
    def attack_protection(self) -> "AttackProtectionClient":
        return self._api.attack_protection

    @property
    def branding(self) -> "BrandingClient":
        return self._api.branding

    @property
    def client_grants(self) -> "ClientGrantsClient":
        return self._api.client_grants

    @property
    def clients(self) -> "ClientsClient":
        return self._api.clients

    @property
    def connections(self) -> "ConnectionsClient":
        return self._api.connections

    @property
    def custom_domains(self) -> "CustomDomainsClient":
        return self._api.custom_domains

    @property
    def device_credentials(self) -> "DeviceCredentialsClient":
        return self._api.device_credentials

    @property
    def email_templates(self) -> "EmailTemplatesClient":
        return self._api.email_templates

    @property
    def emails(self) -> "EmailsClient":
        return self._api.emails

    @property
    def event_streams(self) -> "EventStreamsClient":
        return self._api.event_streams

    @property
    def flows(self) -> "FlowsClient":
        return self._api.flows

    @property
    def forms(self) -> "FormsClient":
        return self._api.forms

    @property
    def guardian(self) -> "GuardianClient":
        return self._api.guardian

    @property
    def hooks(self) -> "HooksClient":
        return self._api.hooks

    @property
    def jobs(self) -> "JobsClient":
        return self._api.jobs

    @property
    def keys(self) -> "KeysClient":
        return self._api.keys

    @property
    def log_streams(self) -> "LogStreamsClient":
        return self._api.log_streams

    @property
    def logs(self) -> "LogsClient":
        return self._api.logs

    @property
    def network_acls(self) -> "NetworkAclsClient":
        return self._api.network_acls

    @property
    def organizations(self) -> "OrganizationsClient":
        return self._api.organizations

    @property
    def prompts(self) -> "PromptsClient":
        return self._api.prompts

    @property
    def refresh_tokens(self) -> "RefreshTokensClient":
        return self._api.refresh_tokens

    @property
    def resource_servers(self) -> "ResourceServersClient":
        return self._api.resource_servers

    @property
    def roles(self) -> "RolesClient":
        return self._api.roles

    @property
    def rules(self) -> "RulesClient":
        return self._api.rules

    @property
    def rules_configs(self) -> "RulesConfigsClient":
        return self._api.rules_configs

    @property
    def self_service_profiles(self) -> "SelfServiceProfilesClient":
        return self._api.self_service_profiles

    @property
    def sessions(self) -> "SessionsClient":
        return self._api.sessions

    @property
    def stats(self) -> "StatsClient":
        return self._api.stats

    @property
    def supplemental_signals(self) -> "SupplementalSignalsClient":
        return self._api.supplemental_signals

    @property
    def tenants(self) -> "TenantsClient":
        return self._api.tenants

    @property
    def tickets(self) -> "TicketsClient":
        return self._api.tickets

    @property
    def token_exchange_profiles(self) -> "TokenExchangeProfilesClient":
        return self._api.token_exchange_profiles

    @property
    def user_blocks(self) -> "UserBlocksClient":
        return self._api.user_blocks

    @property
    def user_grants(self) -> "UserGrantsClient":
        return self._api.user_grants

    @property
    def users(self) -> "UsersClient":
        return self._api.users

    @property
    def verifiable_credentials(self) -> "VerifiableCredentialsClient":
        return self._api.verifiable_credentials


class AsyncManagementClient:
    """
    Async Auth0 Management API client with automatic token management.

    Supports two initialization patterns:

    1. With an existing token:

        client = AsyncManagementClient(
            domain="tenant.auth0.com",
            token="your_token"
        )

    2. With client credentials (automatic token acquisition and refresh):

        client = AsyncManagementClient(
            domain="tenant.auth0.com",
            client_id="your_client_id",
            client_secret="your_client_secret"
        )

    Parameters
    ----------
    domain : str
        Your Auth0 domain (e.g., "your-tenant.auth0.com").
    token : Optional[Union[str, Callable[[], str]]]
        A static token string or a callable that returns a token.
        Required if client_id/client_secret are not provided.
    client_id : Optional[str]
        Your Auth0 application client ID.
        Required along with client_secret for automatic token acquisition.
    client_secret : Optional[str]
        Your Auth0 application client secret.
        Required along with client_id for automatic token acquisition.
    audience : Optional[str]
        The API audience. Defaults to https://{domain}/api/v2/
    headers : Optional[Dict[str, str]]
        Additional headers to send with requests.
    timeout : Optional[float]
        Request timeout in seconds. Defaults to 60.
    httpx_client : Optional[httpx.AsyncClient]
        Custom httpx async client for requests.

    Raises
    ------
    ValueError
        If neither token nor client_id/client_secret are provided.
    """

    def __init__(
        self,
        *,
        domain: str,
        token: Optional[Union[str, Callable[[], str]]] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        audience: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        httpx_client: Optional[httpx.AsyncClient] = None,
    ):
        # Validate auth options
        has_token = token is not None
        has_credentials = client_id is not None and client_secret is not None

        if not has_token and not has_credentials:
            raise ValueError("Either 'token' or both 'client_id' and 'client_secret' must be provided")

        # Create token supplier
        # Note: AsyncAuth0Api expects a sync callable for token, so we use
        # the sync TokenProvider. This is safe because httpx sync calls work
        # in async contexts.
        if has_credentials and not has_token:
            provider = TokenProvider(
                domain=domain,
                client_id=client_id,  # type: ignore[arg-type]
                client_secret=client_secret,  # type: ignore[arg-type]
                audience=audience,
            )
            resolved_token: Union[str, Callable[[], str]] = provider.get_token
        else:
            resolved_token = token  # type: ignore[assignment]

        # Create underlying client
        self._api = AsyncAuth0(
            base_url=f"https://{domain}/api/v2",
            token=resolved_token,
            headers=headers,
            timeout=timeout,
            httpx_client=httpx_client,
        )

    # Forward all sub-client properties
    @property
    def actions(self) -> "AsyncActionsClient":
        return self._api.actions

    @property
    def anomaly(self) -> "AsyncAnomalyClient":
        return self._api.anomaly

    @property
    def attack_protection(self) -> "AsyncAttackProtectionClient":
        return self._api.attack_protection

    @property
    def branding(self) -> "AsyncBrandingClient":
        return self._api.branding

    @property
    def client_grants(self) -> "AsyncClientGrantsClient":
        return self._api.client_grants

    @property
    def clients(self) -> "AsyncClientsClient":
        return self._api.clients

    @property
    def connections(self) -> "AsyncConnectionsClient":
        return self._api.connections

    @property
    def custom_domains(self) -> "AsyncCustomDomainsClient":
        return self._api.custom_domains

    @property
    def device_credentials(self) -> "AsyncDeviceCredentialsClient":
        return self._api.device_credentials

    @property
    def email_templates(self) -> "AsyncEmailTemplatesClient":
        return self._api.email_templates

    @property
    def emails(self) -> "AsyncEmailsClient":
        return self._api.emails

    @property
    def event_streams(self) -> "AsyncEventStreamsClient":
        return self._api.event_streams

    @property
    def flows(self) -> "AsyncFlowsClient":
        return self._api.flows

    @property
    def forms(self) -> "AsyncFormsClient":
        return self._api.forms

    @property
    def guardian(self) -> "AsyncGuardianClient":
        return self._api.guardian

    @property
    def hooks(self) -> "AsyncHooksClient":
        return self._api.hooks

    @property
    def jobs(self) -> "AsyncJobsClient":
        return self._api.jobs

    @property
    def keys(self) -> "AsyncKeysClient":
        return self._api.keys

    @property
    def log_streams(self) -> "AsyncLogStreamsClient":
        return self._api.log_streams

    @property
    def logs(self) -> "AsyncLogsClient":
        return self._api.logs

    @property
    def network_acls(self) -> "AsyncNetworkAclsClient":
        return self._api.network_acls

    @property
    def organizations(self) -> "AsyncOrganizationsClient":
        return self._api.organizations

    @property
    def prompts(self) -> "AsyncPromptsClient":
        return self._api.prompts

    @property
    def refresh_tokens(self) -> "AsyncRefreshTokensClient":
        return self._api.refresh_tokens

    @property
    def resource_servers(self) -> "AsyncResourceServersClient":
        return self._api.resource_servers

    @property
    def roles(self) -> "AsyncRolesClient":
        return self._api.roles

    @property
    def rules(self) -> "AsyncRulesClient":
        return self._api.rules

    @property
    def rules_configs(self) -> "AsyncRulesConfigsClient":
        return self._api.rules_configs

    @property
    def self_service_profiles(self) -> "AsyncSelfServiceProfilesClient":
        return self._api.self_service_profiles

    @property
    def sessions(self) -> "AsyncSessionsClient":
        return self._api.sessions

    @property
    def stats(self) -> "AsyncStatsClient":
        return self._api.stats

    @property
    def supplemental_signals(self) -> "AsyncSupplementalSignalsClient":
        return self._api.supplemental_signals

    @property
    def tenants(self) -> "AsyncTenantsClient":
        return self._api.tenants

    @property
    def tickets(self) -> "AsyncTicketsClient":
        return self._api.tickets

    @property
    def token_exchange_profiles(self) -> "AsyncTokenExchangeProfilesClient":
        return self._api.token_exchange_profiles

    @property
    def user_blocks(self) -> "AsyncUserBlocksClient":
        return self._api.user_blocks

    @property
    def user_grants(self) -> "AsyncUserGrantsClient":
        return self._api.user_grants

    @property
    def users(self) -> "AsyncUsersClient":
        return self._api.users

    @property
    def verifiable_credentials(self) -> "AsyncVerifiableCredentialsClient":
        return self._api.verifiable_credentials
