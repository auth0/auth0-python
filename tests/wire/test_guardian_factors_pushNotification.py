from .conftest import get_client, verify_request_count


def test_guardian_factors_pushNotification_get_apns_provider() -> None:
    """Test getApnsProvider endpoint with WireMock"""
    test_id = "guardian.factors.push_notification.get_apns_provider.0"
    client = get_client(test_id)
    client.guardian.factors.push_notification.get_apns_provider()
    verify_request_count(test_id, "GET", "/guardian/factors/push-notification/providers/apns", None, 1)


def test_guardian_factors_pushNotification_set_apns_provider() -> None:
    """Test setApnsProvider endpoint with WireMock"""
    test_id = "guardian.factors.push_notification.set_apns_provider.0"
    client = get_client(test_id)
    client.guardian.factors.push_notification.set_apns_provider()
    verify_request_count(test_id, "PATCH", "/guardian/factors/push-notification/providers/apns", None, 1)


def test_guardian_factors_pushNotification_set_fcm_provider() -> None:
    """Test setFcmProvider endpoint with WireMock"""
    test_id = "guardian.factors.push_notification.set_fcm_provider.0"
    client = get_client(test_id)
    client.guardian.factors.push_notification.set_fcm_provider()
    verify_request_count(test_id, "PATCH", "/guardian/factors/push-notification/providers/fcm", None, 1)


def test_guardian_factors_pushNotification_set_fcmv_1_provider() -> None:
    """Test setFcmv1Provider endpoint with WireMock"""
    test_id = "guardian.factors.push_notification.set_fcmv_1_provider.0"
    client = get_client(test_id)
    client.guardian.factors.push_notification.set_fcmv_1_provider()
    verify_request_count(test_id, "PATCH", "/guardian/factors/push-notification/providers/fcmv1", None, 1)


def test_guardian_factors_pushNotification_get_sns_provider() -> None:
    """Test getSnsProvider endpoint with WireMock"""
    test_id = "guardian.factors.push_notification.get_sns_provider.0"
    client = get_client(test_id)
    client.guardian.factors.push_notification.get_sns_provider()
    verify_request_count(test_id, "GET", "/guardian/factors/push-notification/providers/sns", None, 1)


def test_guardian_factors_pushNotification_set_sns_provider() -> None:
    """Test setSnsProvider endpoint with WireMock"""
    test_id = "guardian.factors.push_notification.set_sns_provider.0"
    client = get_client(test_id)
    client.guardian.factors.push_notification.set_sns_provider()
    verify_request_count(test_id, "PUT", "/guardian/factors/push-notification/providers/sns", None, 1)


def test_guardian_factors_pushNotification_update_sns_provider() -> None:
    """Test updateSnsProvider endpoint with WireMock"""
    test_id = "guardian.factors.push_notification.update_sns_provider.0"
    client = get_client(test_id)
    client.guardian.factors.push_notification.update_sns_provider()
    verify_request_count(test_id, "PATCH", "/guardian/factors/push-notification/providers/sns", None, 1)


def test_guardian_factors_pushNotification_get_selected_provider() -> None:
    """Test getSelectedProvider endpoint with WireMock"""
    test_id = "guardian.factors.push_notification.get_selected_provider.0"
    client = get_client(test_id)
    client.guardian.factors.push_notification.get_selected_provider()
    verify_request_count(test_id, "GET", "/guardian/factors/push-notification/selected-provider", None, 1)


def test_guardian_factors_pushNotification_set_provider() -> None:
    """Test setProvider endpoint with WireMock"""
    test_id = "guardian.factors.push_notification.set_provider.0"
    client = get_client(test_id)
    client.guardian.factors.push_notification.set_provider(provider="guardian")
    verify_request_count(test_id, "PUT", "/guardian/factors/push-notification/selected-provider", None, 1)
