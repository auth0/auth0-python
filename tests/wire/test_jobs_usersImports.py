from .conftest import get_client, verify_request_count


def test_jobs_usersImports_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "jobs.users_imports.create.0"
    client = get_client(test_id)
    client.jobs.users_imports.create(users="example_users", connection_id="connection_id")
    verify_request_count(test_id, "POST", "/jobs/users-imports", None, 1)
