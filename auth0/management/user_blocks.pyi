from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from typing import Any

class UserBlocks:
    def get_by_identifier_async(self, identifier: str) -> dict[str, Any]: ...
    def unblock_by_identifier_async(self, identifier: dict[str, Any]) -> Any: ...
    def get_async(self, id: str) -> dict[str, Any]: ...
    def unblock_async(self, id: str) -> Any: ...
