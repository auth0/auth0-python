from .conftest import get_client, verify_request_count


def test_experimentation_experiments_advance_ramp() -> None:
    """Test advanceRamp endpoint with WireMock"""
    test_id = "experimentation.experiments.advance_ramp.0"
    client = get_client(test_id)
    client.experimentation.experiments.advance_ramp(
        id="id",
        target_level=1,
    )
    verify_request_count(test_id, "POST", "/experimentation/experiments/id/advance-ramp", None, 1)
