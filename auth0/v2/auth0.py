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


class Auth0(object):
    """Docstring for Auth0. """

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
