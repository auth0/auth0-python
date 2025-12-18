from .conftest import get_client, verify_request_count


def test_userAttributeProfiles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "user_attribute_profiles.list_.0"
    client = get_client(test_id)
    client.user_attribute_profiles.list(from_="from", take=1)
    verify_request_count(test_id, "GET", "/user-attribute-profiles", {"from": "from", "take": "1"}, 1)


def test_userAttributeProfiles_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "user_attribute_profiles.create.0"
    client = get_client(test_id)
    client.user_attribute_profiles.create(
        name="name",
        user_attributes={
            "key": {
                "description": "description",
                "label": "label",
                "profile_required": True,
                "auth_0_mapping": "auth0_mapping",
            }
        },
    )
    verify_request_count(test_id, "POST", "/user-attribute-profiles", None, 1)


def test_userAttributeProfiles_list_templates() -> None:
    """Test listTemplates endpoint with WireMock"""
    test_id = "user_attribute_profiles.list_templates.0"
    client = get_client(test_id)
    client.user_attribute_profiles.list_templates()
    verify_request_count(test_id, "GET", "/user-attribute-profiles/templates", None, 1)


def test_userAttributeProfiles_get_template() -> None:
    """Test getTemplate endpoint with WireMock"""
    test_id = "user_attribute_profiles.get_template.0"
    client = get_client(test_id)
    client.user_attribute_profiles.get_template(id="id")
    verify_request_count(test_id, "GET", "/user-attribute-profiles/templates/id", None, 1)


def test_userAttributeProfiles_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "user_attribute_profiles.get.0"
    client = get_client(test_id)
    client.user_attribute_profiles.get(id="id")
    verify_request_count(test_id, "GET", "/user-attribute-profiles/id", None, 1)


def test_userAttributeProfiles_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "user_attribute_profiles.delete.0"
    client = get_client(test_id)
    client.user_attribute_profiles.delete(id="id")
    verify_request_count(test_id, "DELETE", "/user-attribute-profiles/id", None, 1)


def test_userAttributeProfiles_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "user_attribute_profiles.update.0"
    client = get_client(test_id)
    client.user_attribute_profiles.update(id="id")
    verify_request_count(test_id, "PATCH", "/user-attribute-profiles/id", None, 1)
