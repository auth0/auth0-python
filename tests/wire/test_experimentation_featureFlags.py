from .conftest import get_client, verify_request_count


def test_experimentation_featureFlags_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "experimentation.feature_flags.list_.0"
    client = get_client(test_id)
    client.experimentation.feature_flags.list(
        from_="from",
        take=1,
        type="auth0",
        status="draft",
    )
    verify_request_count(
        test_id,
        "GET",
        "/experimentation/feature-flags",
        {"from": "from", "take": "1", "type": "auth0", "status": "draft"},
        1,
    )


def test_experimentation_featureFlags_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "experimentation.feature_flags.create.0"
    client = get_client(test_id)
    client.experimentation.feature_flags.create(
        name="name",
        parameters={},
    )
    verify_request_count(test_id, "POST", "/experimentation/feature-flags", None, 1)


def test_experimentation_featureFlags_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "experimentation.feature_flags.get.0"
    client = get_client(test_id)
    client.experimentation.feature_flags.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/experimentation/feature-flags/id", None, 1)


def test_experimentation_featureFlags_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "experimentation.feature_flags.delete.0"
    client = get_client(test_id)
    client.experimentation.feature_flags.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/experimentation/feature-flags/id", None, 1)


def test_experimentation_featureFlags_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "experimentation.feature_flags.update.0"
    client = get_client(test_id)
    client.experimentation.feature_flags.update(
        id="id",
    )
    verify_request_count(test_id, "PATCH", "/experimentation/feature-flags/id", None, 1)


def test_experimentation_featureFlags_update_status() -> None:
    """Test updateStatus endpoint with WireMock"""
    test_id = "experimentation.feature_flags.update_status.0"
    client = get_client(test_id)
    client.experimentation.feature_flags.update_status(
        id="id",
        status="draft",
    )
    verify_request_count(test_id, "POST", "/experimentation/feature-flags/id/status", None, 1)
