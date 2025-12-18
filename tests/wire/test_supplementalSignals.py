from .conftest import get_client, verify_request_count


def test_supplementalSignals_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "supplemental_signals.get.0"
    client = get_client(test_id)
    client.supplemental_signals.get()
    verify_request_count(test_id, "GET", "/supplemental-signals", None, 1)


def test_supplementalSignals_patch() -> None:
    """Test patch endpoint with WireMock"""
    test_id = "supplemental_signals.patch.0"
    client = get_client(test_id)
    client.supplemental_signals.patch(akamai_enabled=True)
    verify_request_count(test_id, "PATCH", "/supplemental-signals", None, 1)
