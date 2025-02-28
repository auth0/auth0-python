from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from typing import Any

class CustomDomains:
    def all(self) -> list[dict[str, Any]]: ...
    def get_async(self, id: str) -> dict[str, Any]: ...
    def delete_async(self, id: str) -> Any: ...
    def create_new_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    def verify_async(self, id: str) -> dict[str, Any]: ...
