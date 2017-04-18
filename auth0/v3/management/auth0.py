from .connections import Connections
from .clients import Clients
from .device_credentials import DeviceCredentials
from .blacklists import Blacklists
from .emails import Emails
from .jobs import Jobs
from .rules import Rules
from .stats import Stats
from .tickets import Tickets
from .users import Users
from .tenants import Tenants
from .client_grants import ClientGrants
from .guardian import Guardian
from .logs import Logs
from .resource_servers import ResourceServers
from .user_blocks import UserBlocks

class Auth0(object):
    """Provides easy access to all endpoint classes

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        token (str): Management API v2 Token
    """

    def __init__(self, domain, token):
        self.clients = Clients(domain, token)
        self.connections = Connections(domain, token)
        self.device_credentials = DeviceCredentials(domain, token)
        self.blacklists = Blacklists(domain, token)
        self.emails = Emails(domain, token)
        self.jobs = Jobs(domain, token)
        self.rules = Rules(domain, token)
        self.stats = Stats(domain, token)
        self.tickets = Tickets(domain, token)
        self.users = Users(domain, token)
        self.tenants = Tenants(domain, token)
        self.client_grants = ClientGrants(domain, token)
        self.guardian = Guardian(domain, token)
        self.logs = Logs(domain, token)
        self.resource_servers = ResourceServers(domain, token)
        self.user_blocks = UserBlocks
