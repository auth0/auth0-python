from .conftest import get_client, verify_request_count


def test_experimentation_experiments_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "experimentation.experiments.list_.0"
    client = get_client(test_id)
    client.experimentation.experiments.list(
        from_="from",
        take=1,
        status="draft",
        authentication_flow="authentication_flow",
        feature_flag_id="feature_flag_id",
    )
    verify_request_count(
        test_id,
        "GET",
        "/experimentation/experiments",
        {
            "from": "from",
            "take": "1",
            "status": "draft",
            "authentication_flow": "authentication_flow",
            "feature_flag_id": "feature_flag_id",
        },
        1,
    )


def test_experimentation_experiments_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "experimentation.experiments.create.0"
    client = get_client(test_id)
    client.experimentation.experiments.create(
        name="name",
        feature_flag_id="feature_flag_id",
        authentication_flow="authentication",
    )
    verify_request_count(test_id, "POST", "/experimentation/experiments", None, 1)


def test_experimentation_experiments_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "experimentation.experiments.get.0"
    client = get_client(test_id)
    client.experimentation.experiments.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/experimentation/experiments/id", None, 1)


def test_experimentation_experiments_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "experimentation.experiments.delete.0"
    client = get_client(test_id)
    client.experimentation.experiments.delete(
        id="id",
    )
    verify_request_count(test_id, "DELETE", "/experimentation/experiments/id", None, 1)


def test_experimentation_experiments_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "experimentation.experiments.update.0"
    client = get_client(test_id)
    client.experimentation.experiments.update(
        id="id",
    )
    verify_request_count(test_id, "PATCH", "/experimentation/experiments/id", None, 1)


def test_experimentation_experiments_advance_ramp() -> None:
    """Test advanceRamp endpoint with WireMock"""
    test_id = "experimentation.experiments.advance_ramp.0"
    client = get_client(test_id)
    client.experimentation.experiments.advance_ramp(
        id="id",
        target_level=1,
    )
    verify_request_count(test_id, "POST", "/experimentation/experiments/id/advance-ramp", None, 1)


def test_experimentation_experiments_update_status() -> None:
    """Test updateStatus endpoint with WireMock"""
    test_id = "experimentation.experiments.update_status.0"
    client = get_client(test_id)
    client.experimentation.experiments.update_status(
        id="id",
        status="active",
    )
    verify_request_count(test_id, "POST", "/experimentation/experiments/id/status", None, 1)


def test_experimentation_experiments_validate() -> None:
    """Test validate endpoint with WireMock"""
    test_id = "experimentation.experiments.validate.0"
    client = get_client(test_id)
    client.experimentation.experiments.validate(
        id="id",
    )
    verify_request_count(test_id, "POST", "/experimentation/experiments/id/validate", None, 1)
