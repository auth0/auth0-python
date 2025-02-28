from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from typing import Any

class UsersByEmail:
    def search_users_by_email_async(self, email: str, fields: list[str] | None = None, include_fields: bool = True) -> list[dict[str, Any]]: ...
