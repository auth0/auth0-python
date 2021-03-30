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
    """

    def __init__(self, domain, token):
        self.blacklists = Blacklists(domain, token)
        self.clients = Clients(domain, token)
        self.client_grants = ClientGrants(domain, token)
        self.custom_domains = CustomDomains(domain, token)
        self.connections = Connections(domain, token)
        self.device_credentials = DeviceCredentials(domain, token)
        self.emails = Emails(domain, token)
        self.email_templates = EmailTemplates(domain, token)
        self.grants = Grants(domain, token)
        self.guardian = Guardian(domain, token)
        self.hooks = Hooks(domain, token)
        self.jobs = Jobs(domain, token)
        self.logs = Logs(domain, token)
        self.log_streams = LogStreams(domain, token)
        self.organizations = Organizations(domain, token)
        self.resource_servers = ResourceServers(domain, token)
        self.roles = Roles(domain, token)
        self.rules = Rules(domain, token)
        self.rules_configs = RulesConfigs(domain, token)
        self.stats = Stats(domain, token)
        self.tenants = Tenants(domain, token)
        self.tickets = Tickets(domain, token)
        self.user_blocks = UserBlocks(domain, token)
        self.users = Users(domain, token)
        self.users_by_email = UsersByEmail(domain, token)
