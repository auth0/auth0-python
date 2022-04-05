import base64
import json
import platform
import sys

import requests

from auth0.v3.rest import RestClient, RestClientOptions

from ..exceptions import Auth0Error, RateLimitError

UNKNOWN_ERROR = "a0.sdk.internal.unknown"


class AuthenticationBase(object):
    """Base authentication object providing simple REST methods.

    Args:
        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)
        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)
    """

    def __init__(self, domain, telemetry=True, timeout=5.0, protocol="https"):
        self.domain = domain
        self.protocol = protocol
        self.client = RestClient(
            None,
            options=RestClientOptions(telemetry=telemetry, timeout=timeout, retries=0),
        )

    def post(self, url, data=None, headers=None):
        return self.client.post(url, data, headers)

    def get(self, url, params=None, headers=None):
        return self.client.get(url, params, headers)
