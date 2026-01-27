from .conftest import get_client, verify_request_count


def test_users_authenticationMethods_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "users.authentication_methods.list_.0"
    client = get_client(test_id)
    client.users.authentication_methods.list(id="id", page=1, per_page=1, include_totals=True)
    verify_request_count(
        test_id, "GET", "/users/id/authentication-methods", {"page": "1", "per_page": "1", "include_totals": "true"}, 1
    )


def test_users_authenticationMethods_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "users.authentication_methods.create.0"
    client = get_client(test_id)
    client.users.authentication_methods.create(id="id", type="phone")
    verify_request_count(test_id, "POST", "/users/id/authentication-methods", None, 1)


def test_users_authenticationMethods_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "users.authentication_methods.set_.0"
    client = get_client(test_id)
    client.users.authentication_methods.set(id="id", request=[{"type": "phone"}])
    verify_request_count(test_id, "PUT", "/users/id/authentication-methods", None, 1)


def test_users_authenticationMethods_delete_all() -> None:
    """Test deleteAll endpoint with WireMock"""
    test_id = "users.authentication_methods.delete_all.0"
    client = get_client(test_id)
    client.users.authentication_methods.delete_all(id="id")
    verify_request_count(test_id, "DELETE", "/users/id/authentication-methods", None, 1)


def test_users_authenticationMethods_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "users.authentication_methods.get.0"
    client = get_client(test_id)
    client.users.authentication_methods.get(id="id", authentication_method_id="authentication_method_id")
    verify_request_count(test_id, "GET", "/users/id/authentication-methods/authentication_method_id", None, 1)


def test_users_authenticationMethods_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "users.authentication_methods.delete.0"
    client = get_client(test_id)
    client.users.authentication_methods.delete(id="id", authentication_method_id="authentication_method_id")
    verify_request_count(test_id, "DELETE", "/users/id/authentication-methods/authentication_method_id", None, 1)


def test_users_authenticationMethods_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "users.authentication_methods.update.0"
    client = get_client(test_id)
    client.users.authentication_methods.update(id="id", authentication_method_id="authentication_method_id")
    verify_request_count(test_id, "PATCH", "/users/id/authentication-methods/authentication_method_id", None, 1)
