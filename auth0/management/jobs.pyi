from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from typing import Any

class Jobs:
    def get_async(self, id: str) -> dict[str, Any]: ...
    def get_failed_job_async(self, id: str) -> dict[str, Any]: ...
    def export_users_async(self, body: dict[str, Any]): ...
    def import_users_async(self, connection_id: str, file_obj: Any, upsert: bool = False, send_completion_email: bool = True, external_id: str | None = None) -> dict[str, Any]: ...
    def send_verification_email_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
