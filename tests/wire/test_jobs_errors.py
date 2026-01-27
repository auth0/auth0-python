from .conftest import get_client, verify_request_count


def test_jobs_errors_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "jobs.errors.get.0"
    client = get_client(test_id)
    client.jobs.errors.get(id="id")
    verify_request_count(test_id, "GET", "/jobs/id/errors", None, 1)
