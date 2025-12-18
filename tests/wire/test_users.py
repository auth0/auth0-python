from .conftest import get_client, verify_request_count


def test_users_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "users.list_.0"
    client = get_client(test_id)
    client.users.list(
        page=1,
        per_page=1,
        include_totals=True,
        sort="sort",
        connection="connection",
        fields="fields",
        include_fields=True,
        q="q",
        search_engine="v1",
        primary_order=True,
    )
    verify_request_count(
        test_id,
        "GET",
        "/users",
        {
            "page": "1",
            "per_page": "1",
            "include_totals": "true",
            "sort": "sort",
            "connection": "connection",
            "fields": "fields",
            "include_fields": "true",
            "q": "q",
            "search_engine": "v1",
            "primary_order": "true",
        },
        1,
    )


def test_users_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "users.create.0"
    client = get_client(test_id)
    client.users.create(connection="connection")
    verify_request_count(test_id, "POST", "/users", None, 1)


def test_users_list_users_by_email() -> None:
    """Test listUsersByEmail endpoint with WireMock"""
    test_id = "users.list_users_by_email.0"
    client = get_client(test_id)
    client.users.list_users_by_email(fields="fields", include_fields=True, email="email")
    verify_request_count(
        test_id, "GET", "/users-by-email", {"fields": "fields", "include_fields": "true", "email": "email"}, 1
    )


def test_users_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "users.get.0"
    client = get_client(test_id)
    client.users.get(id="id", fields="fields", include_fields=True)
    verify_request_count(test_id, "GET", "/users/id", {"fields": "fields", "include_fields": "true"}, 1)


def test_users_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "users.delete.0"
    client = get_client(test_id)
    client.users.delete(id="id")
    verify_request_count(test_id, "DELETE", "/users/id", None, 1)


def test_users_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "users.update.0"
    client = get_client(test_id)
    client.users.update(id="id")
    verify_request_count(test_id, "PATCH", "/users/id", None, 1)


def test_users_regenerate_recovery_code() -> None:
    """Test regenerateRecoveryCode endpoint with WireMock"""
    test_id = "users.regenerate_recovery_code.0"
    client = get_client(test_id)
    client.users.regenerate_recovery_code(id="id")
    verify_request_count(test_id, "POST", "/users/id/recovery-code-regeneration", None, 1)


def test_users_revoke_access() -> None:
    """Test revokeAccess endpoint with WireMock"""
    test_id = "users.revoke_access.0"
    client = get_client(test_id)
    client.users.revoke_access(id="id")
    verify_request_count(test_id, "POST", "/users/id/revoke-access", None, 1)
