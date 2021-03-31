import unittest

from ...management.auth0 import Auth0
from ...management.blacklists import Blacklists
from ...management.client_grants import ClientGrants
from ...management.clients import Clients
from ...management.connections import Connections
from ...management.custom_domains import CustomDomains
from ...management.device_credentials import DeviceCredentials
from ...management.email_templates import EmailTemplates
from ...management.emails import Emails
from ...management.grants import Grants
from ...management.guardian import Guardian
from ...management.hooks import Hooks
from ...management.jobs import Jobs
from ...management.log_streams import LogStreams
from ...management.logs import Logs
from ...management.organizations import Organizations
from ...management.resource_servers import ResourceServers
from ...management.roles import Roles
from ...management.rules import Rules
from ...management.rules_configs import RulesConfigs
from ...management.stats import Stats
from ...management.tenants import Tenants
from ...management.tickets import Tickets
from ...management.user_blocks import UserBlocks
from ...management.users import Users
from ...management.users_by_email import UsersByEmail


class TestAuth0(unittest.TestCase):

    def setUp(self):
        self.domain = 'user.some.domain'
        self.token = 'a-token'
        self.a0 = Auth0(self.domain, self.token)

    def test_blacklists(self):
        self.assertIsInstance(self.a0.blacklists, Blacklists)

    def test_clients(self):
        self.assertIsInstance(self.a0.clients, Clients)

    def test_client_grants(self):
        self.assertIsInstance(self.a0.client_grants, ClientGrants)

    def test_custom_domains(self):
        self.assertIsInstance(self.a0.custom_domains, CustomDomains)

    def test_connections(self):
        self.assertIsInstance(self.a0.connections, Connections)

    def test_device_credentials(self):
        self.assertIsInstance(self.a0.device_credentials, DeviceCredentials)

    def test_emails(self):
        self.assertIsInstance(self.a0.emails, Emails)

    def test_email_templates(self):
        self.assertIsInstance(self.a0.email_templates, EmailTemplates)

    def test_grants(self):
        self.assertIsInstance(self.a0.grants, Grants)

    def test_guardian(self):
        self.assertIsInstance(self.a0.guardian, Guardian)

    def test_hooks(self):
        self.assertIsInstance(self.a0.hooks, Hooks)

    def test_jobs(self):
        self.assertIsInstance(self.a0.jobs, Jobs)

    def test_logs(self):
        self.assertIsInstance(self.a0.logs, Logs)

    def test_log_streams(self):
        self.assertIsInstance(self.a0.log_streams, LogStreams)

    def test_organizations(self):
        self.assertIsInstance(self.a0.organizations, Organizations)

    def test_resource_servers(self):
        self.assertIsInstance(self.a0.resource_servers, ResourceServers)

    def test_roles(self):
        self.assertIsInstance(self.a0.roles, Roles)

    def test_rules(self):
        self.assertIsInstance(self.a0.rules, Rules)

    def test_rules_configs(self):
        self.assertIsInstance(self.a0.rules_configs, RulesConfigs)

    def test_stats(self):
        self.assertIsInstance(self.a0.stats, Stats)

    def test_tenants(self):
        self.assertIsInstance(self.a0.tenants, Tenants)

    def test_tickets(self):
        self.assertIsInstance(self.a0.tickets, Tickets)

    def test_user_blocks(self):
        self.assertIsInstance(self.a0.user_blocks, UserBlocks)

    def test_users(self):
        self.assertIsInstance(self.a0.users, Users)

    def test_users_by_email(self):
        self.assertIsInstance(self.a0.users_by_email, UsersByEmail)
