from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from typing import Any

class Tickets:
    def create_email_verification_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    def create_pswd_change_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
