from .conftest import get_client, verify_request_count


def test_guardian_factors_duo_settings_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "guardian.factors.duo.settings.get.0"
    client = get_client(test_id)
    client.guardian.factors.duo.settings.get()
    verify_request_count(test_id, "GET", "/guardian/factors/duo/settings", None, 1)


def test_guardian_factors_duo_settings_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "guardian.factors.duo.settings.set_.0"
    client = get_client(test_id)
    client.guardian.factors.duo.settings.set()
    verify_request_count(test_id, "PUT", "/guardian/factors/duo/settings", None, 1)


def test_guardian_factors_duo_settings_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "guardian.factors.duo.settings.update.0"
    client = get_client(test_id)
    client.guardian.factors.duo.settings.update()
    verify_request_count(test_id, "PATCH", "/guardian/factors/duo/settings", None, 1)
