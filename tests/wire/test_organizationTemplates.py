from .conftest import get_client, verify_request_count


def test_organizationTemplates_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organization_templates.list_.0"
    client = get_client(test_id)
    client.organization_templates.list(
        from_="from",
        take=1,
    )
    verify_request_count(test_id, "GET", "/organization-templates", {"from": "from", "take": "1"}, 1)


def test_organizationTemplates_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organization_templates.create.0"
    client = get_client(test_id)
    client.organization_templates.create(
        name="name",
        organization_deletion_behavior="allow",
        enforce_permission_ceiling=True,
        enforce_self_assignment_restriction=True,
    )
    verify_request_count(test_id, "POST", "/organization-templates", None, 1)


def test_organizationTemplates_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organization_templates.get.0"
    client = get_client(test_id)
    client.organization_templates.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/organization-templates/id", None, 1)


def test_organizationTemplates_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "organization_templates.update.0"
    client = get_client(test_id)
    client.organization_templates.update(
        id="id",
    )
    verify_request_count(test_id, "PATCH", "/organization-templates/id", None, 1)


def test_organizationTemplates_list_organizations() -> None:
    """Test listOrganizations endpoint with WireMock"""
    test_id = "organization_templates.list_organizations.0"
    client = get_client(test_id)
    client.organization_templates.list_organizations(
        id="id",
        from_="from",
        take=1,
    )
    verify_request_count(test_id, "GET", "/organization-templates/id/organizations", {"from": "from", "take": "1"}, 1)
