from .conftest import get_client, verify_request_count


def test_jobs_usersExports_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "jobs.users_exports.create.0"
    client = get_client(test_id)
    client.jobs.users_exports.create()
    verify_request_count(test_id, "POST", "/jobs/users-exports", None, 1)
