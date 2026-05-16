from typing import Any, Optional, Union, List, Dict

from .base import AuthenticationBase

import json


class BackChannelLogin(AuthenticationBase):
    """Back-Channel Login endpoint"""

    def back_channel_login(
        self,
        binding_message: str,
        login_hint: str,
        scope: str,
        authorization_details: Optional[Union[str, List[Dict]]] = None,
        **kwargs
    ) -> Any:
        """Send a Back-Channel Login.

        Args:
             binding_message (str): Human-readable string displayed on both the device calling /bc-authorize and the user’s 
             authentication device to ensure the user is approves the correct request.

             login_hint (str):  JSON string containing user details for authentication in the iss_sub format.Ensure 
             serialization before passing.

             scope(str): "openid" is a required scope.Multiple scopes are separated 
             with whitespace.

             authorization_details (str, list of dict, optional): JSON string or a list of dictionaries representing
             Rich Authorization Requests (RAR) details to include in the CIBA request.

             **kwargs: Other fields to send along with the request.

        Returns:
            auth_req_id, expires_in, interval
        """

        data = {
                "client_id": self.client_id,
                "binding_message": binding_message,
                "login_hint": login_hint,
                "scope": scope,
                **kwargs,
            }

        if authorization_details is not None:
            if isinstance(authorization_details, str):
                data["authorization_details"] = authorization_details
            elif isinstance(authorization_details, list):
                data["authorization_details"] = json.dumps(authorization_details)
                
        data.update(kwargs)

        return self.authenticated_post(
            f"{self.protocol}://{self.domain}/bc-authorize",
            data = data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
