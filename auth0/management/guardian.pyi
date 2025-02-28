from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from typing import Any

class Guardian:
    def all_factors(self) -> list[dict[str, Any]]: ...
    def update_factor_async(self, name: str, body: dict[str, Any]) -> dict[str, Any]: ...
    def update_templates_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    def get_templates(self) -> dict[str, Any]: ...
    def get_enrollment_async(self, id: str) -> dict[str, Any]: ...
    def delete_enrollment_async(self, id: str) -> Any: ...
    def create_enrollment_ticket_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    def get_factor_providers_async(self, factor_name: str, name: str) -> dict[str, Any]: ...
    def update_factor_providers_async(self, factor_name: str, name: str, body: dict[str, Any]) -> dict[str, Any]: ...
