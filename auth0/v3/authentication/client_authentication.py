import datetime
import uuid

import jwt


def create_client_assertion_jwt(
    domain, client_id, client_assertion_signing_key, client_assertion_signing_alg
):
    client_assertion_signing_alg = client_assertion_signing_alg or "RS256"
    now = datetime.datetime.utcnow()
    return jwt.encode(
        {
            "iss": client_id,
            "sub": client_id,
            "aud": "https://{}/".format(domain),
            "iat": now,
            "exp": now + datetime.timedelta(seconds=180),
            "jti": str(uuid.uuid4()),
        },
        client_assertion_signing_key,
        client_assertion_signing_alg,
    )


def add_client_authentication(
    payload,
    domain,
    client_id,
    client_secret,
    client_assertion_signing_key,
    client_assertion_signing_alg,
):
    authenticated_payload = payload.copy()
    if client_assertion_signing_key:
        authenticated_payload["client_assertion"] = create_client_assertion_jwt(
            domain,
            client_id,
            client_assertion_signing_key,
            client_assertion_signing_alg,
        )
        authenticated_payload[
            "client_assertion_type"
        ] = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
    elif client_secret:
        authenticated_payload["client_secret"] = client_secret
    return authenticated_payload
