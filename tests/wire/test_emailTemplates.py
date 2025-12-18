from .conftest import get_client, verify_request_count


def test_emailTemplates_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "email_templates.create.0"
    client = get_client(test_id)
    client.email_templates.create(template="verify_email")
    verify_request_count(test_id, "POST", "/email-templates", None, 1)


def test_emailTemplates_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "email_templates.get.0"
    client = get_client(test_id)
    client.email_templates.get(template_name="verify_email")
    verify_request_count(test_id, "GET", "/email-templates/verify_email", None, 1)


def test_emailTemplates_set_() -> None:
    """Test set endpoint with WireMock"""
    test_id = "email_templates.set_.0"
    client = get_client(test_id)
    client.email_templates.set(template_name="verify_email", template="verify_email")
    verify_request_count(test_id, "PUT", "/email-templates/verify_email", None, 1)


def test_emailTemplates_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "email_templates.update.0"
    client = get_client(test_id)
    client.email_templates.update(template_name="verify_email")
    verify_request_count(test_id, "PATCH", "/email-templates/verify_email", None, 1)
