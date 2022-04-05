from ..utils import is_async_available
from .actions import Actions
from .attack_protection import AttackProtection
from .blacklists import Blacklists
from .client_grants import ClientGrants
from .clients import Clients
from .connections import Connections
from .custom_domains import CustomDomains
from .device_credentials import DeviceCredentials
from .email_templates import EmailTemplates
from .emails import Emails
from .grants import Grants
from .guardian import Guardian
from .hooks import Hooks
from .jobs import Jobs
from .log_streams import LogStreams
from .logs import Logs
from .organizations import Organizations
from .prompts import Prompts
from .resource_servers import ResourceServers
from .roles import Roles
from .rules import Rules
from .rules_configs import RulesConfigs
from .stats import Stats
from .tenants import Tenants
from .tickets import Tickets
from .user_blocks import UserBlocks
from .users import Users
from .users_by_email import UsersByEmail

modules = {
    "actions": Actions,
    "attack_protection": AttackProtection,
    "blacklists": Blacklists,
    "client_grants": ClientGrants,
    "clients": Clients,
    "connections": Connections,
    "custom_domains": CustomDomains,
    "device_credentials": DeviceCredentials,
    "email_templates": EmailTemplates,
    "emails": Emails,
    "grants": Grants,
    "guardian": Guardian,
    "hooks": Hooks,
    "jobs": Jobs,
    "log_streams": LogStreams,
    "logs": Logs,
    "organizations": Organizations,
    "prompts": Prompts,
    "resource_servers": ResourceServers,
    "roles": Roles,
    "rules_configs": RulesConfigs,
    "rules": Rules,
    "stats": Stats,
    "tenants": Tenants,
    "tickets": Tickets,
    "user_blocks": UserBlocks,
    "users_by_email": UsersByEmail,
    "users": Users,
}


class Auth0(object):
    """Provides easy access to all endpoint classes

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token

        rest_options (RestClientOptions): Pass an instance of
            RestClientOptions to configure additional RestClient
            options, such as rate-limit retries.
            (defaults to None)
    """

    def __init__(self, domain, token, rest_options=None):
        if is_async_available():
            from ..asyncify import asyncify

            for name, cls in modules.items():
                cls = asyncify(cls)
                setattr(self, name, cls(domain=domain, token=token, rest_options=None))
        else:
            for name, cls in modules.items():
                setattr(self, name, cls(domain=domain, token=token, rest_options=None))
