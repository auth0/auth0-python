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
        self.actions = Actions(domain=domain, token=token, rest_options=rest_options)
        self.attack_protection = AttackProtection(domain=domain, token=token, rest_options=rest_options)
        self.blacklists = Blacklists(domain=domain, token=token, rest_options=rest_options)
        self.client_grants = ClientGrants(domain=domain, token=token, rest_options=rest_options)
        self.clients = Clients(domain=domain, token=token, rest_options=rest_options)
        self.connections = Connections(domain=domain, token=token, rest_options=rest_options)
        self.custom_domains = CustomDomains(domain=domain, token=token, rest_options=rest_options)
        self.device_credentials = DeviceCredentials(domain=domain, token=token, rest_options=rest_options)
        self.email_templates = EmailTemplates(domain=domain, token=token, rest_options=rest_options)
        self.emails = Emails(domain=domain, token=token, rest_options=rest_options)
        self.grants = Grants(domain=domain, token=token, rest_options=rest_options)
        self.guardian = Guardian(domain=domain, token=token, rest_options=rest_options)
        self.hooks = Hooks(domain=domain, token=token, rest_options=rest_options)
        self.jobs = Jobs(domain=domain, token=token, rest_options=rest_options)
        self.log_streams = LogStreams(domain=domain, token=token, rest_options=rest_options)
        self.logs = Logs(domain=domain, token=token, rest_options=rest_options)
        self.organizations = Organizations(domain=domain, token=token, rest_options=rest_options)
        self.prompts = Prompts(domain=domain, token=token, rest_options=rest_options)
        self.resource_servers = ResourceServers(domain=domain, token=token, rest_options=rest_options)
        self.roles = Roles(domain=domain, token=token, rest_options=rest_options)
        self.rules_configs = RulesConfigs(domain=domain, token=token, rest_options=rest_options)
        self.rules = Rules(domain=domain, token=token, rest_options=rest_options)
        self.stats = Stats(domain=domain, token=token, rest_options=rest_options)
        self.tenants = Tenants(domain=domain, token=token, rest_options=rest_options)
        self.tickets = Tickets(domain=domain, token=token, rest_options=rest_options)
        self.user_blocks = UserBlocks(domain=domain, token=token, rest_options=rest_options)
        self.users_by_email = UsersByEmail(domain=domain, token=token, rest_options=rest_options)
        self.users = Users(domain=domain, token=token, rest_options=rest_options)
