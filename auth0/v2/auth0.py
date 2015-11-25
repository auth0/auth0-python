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


class Auth0(object):
    """Provides easy access to all endpoint classes

    Args:
        domain (str): Your Auth0 domain, e.g: 'username.auth0.com'

        jwt_token (str): An API token created with your account's global
            keys. You can create one by using the token generator in the
            API Explorer: https://auth0.com/docs/api/v2
    """

    def __init__(self, domain, jwt_token):
        self.clients = Clients(domain, jwt_token)
        self.connections = Connections(domain, jwt_token)
        self.device_credentials = DeviceCredentials(domain, jwt_token)
        self.blacklists = Blacklists(domain, jwt_token)
        self.emails = Emails(domain, jwt_token)
        self.jobs = Jobs(domain, jwt_token)
        self.rules = Rules(domain, jwt_token)
        self.stats = Stats(domain, jwt_token)
        self.tickets = Tickets(domain, jwt_token)
        self.users = Users(domain, jwt_token)
        self.tenants = Tenants(domain, jwt_token)
