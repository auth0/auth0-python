from .conftest import get_client, verify_request_count


def test_anomaly_blocks_check_ip() -> None:
    """Test checkIp endpoint with WireMock"""
    test_id = "anomaly.blocks.check_ip.0"
    client = get_client(test_id)
    client.anomaly.blocks.check_ip(id="id")
    verify_request_count(test_id, "GET", "/anomaly/blocks/ips/id", None, 1)


def test_anomaly_blocks_unblock_ip() -> None:
    """Test unblockIp endpoint with WireMock"""
    test_id = "anomaly.blocks.unblock_ip.0"
    client = get_client(test_id)
    client.anomaly.blocks.unblock_ip(id="id")
    verify_request_count(test_id, "DELETE", "/anomaly/blocks/ips/id", None, 1)
