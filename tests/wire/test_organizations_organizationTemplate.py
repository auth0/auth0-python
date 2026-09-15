from .conftest import get_client, verify_request_count


def test_organizations_organizationTemplate_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organizations.organization_template.get.0"
    client = get_client(test_id)
    client.organizations.organization_template.get(
        id="id",
    )
    verify_request_count(test_id, "GET", "/organizations/id/organization-templates", None, 1)


def test_organizations_organizationTemplate_assign_organization_template() -> None:
    """Test assignOrganizationTemplate endpoint with WireMock"""
    test_id = "organizations.organization_template.assign_organization_template.0"
    client = get_client(test_id)
    client.organizations.organization_template.assign_organization_template(
        id="id",
        template_id="template_id",
    )
    verify_request_count(test_id, "PUT", "/organizations/id/organization-templates/template_id", None, 1)


def test_organizations_organizationTemplate_unassign_organization_template() -> None:
    """Test unassignOrganizationTemplate endpoint with WireMock"""
    test_id = "organizations.organization_template.unassign_organization_template.0"
    client = get_client(test_id)
    client.organizations.organization_template.unassign_organization_template(
        id="id",
        template_id="template_id",
    )
    verify_request_count(test_id, "DELETE", "/organizations/id/organization-templates/template_id", None, 1)
