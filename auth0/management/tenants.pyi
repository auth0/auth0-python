from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from typing import Any

class Tenants:
    def get_async(self, fields: list[str] | None = None, include_fields: bool = True) -> dict[str, Any]: ...
    def update_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
