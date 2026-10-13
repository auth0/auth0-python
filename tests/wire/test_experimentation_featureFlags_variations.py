from .conftest import get_client, verify_request_count


def test_experimentation_featureFlags_variations_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "experimentation.feature_flags.variations.list_.0"
    client = get_client(test_id)
    client.experimentation.feature_flags.variations.list(
        id="id",
    )
    verify_request_count(test_id, "GET", "/experimentation/feature-flags/id/variations", None, 1)


def test_experimentation_featureFlags_variations_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "experimentation.feature_flags.variations.create.0"
    client = get_client(test_id)
    client.experimentation.feature_flags.variations.create(
        id="id",
        name="name",
        overrides={"key": "value"},
    )
    verify_request_count(test_id, "POST", "/experimentation/feature-flags/id/variations", None, 1)


def test_experimentation_featureFlags_variations_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "experimentation.feature_flags.variations.get.0"
    client = get_client(test_id)
    client.experimentation.feature_flags.variations.get(
        id="id",
        vid="vid",
    )
    verify_request_count(test_id, "GET", "/experimentation/feature-flags/id/variations/vid", None, 1)


def test_experimentation_featureFlags_variations_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "experimentation.feature_flags.variations.delete.0"
    client = get_client(test_id)
    client.experimentation.feature_flags.variations.delete(
        id="id",
        vid="vid",
    )
    verify_request_count(test_id, "DELETE", "/experimentation/feature-flags/id/variations/vid", None, 1)


def test_experimentation_featureFlags_variations_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "experimentation.feature_flags.variations.update.0"
    client = get_client(test_id)
    client.experimentation.feature_flags.variations.update(
        id="id",
        vid="vid",
    )
    verify_request_count(test_id, "PATCH", "/experimentation/feature-flags/id/variations/vid", None, 1)
