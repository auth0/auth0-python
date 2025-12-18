from .conftest import get_client, verify_request_count


def test_branding_themes_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "branding.themes.create.0"
    client = get_client(test_id)
    client.branding.themes.create(
        borders={
            "button_border_radius": 1.1,
            "button_border_weight": 1.1,
            "buttons_style": "pill",
            "input_border_radius": 1.1,
            "input_border_weight": 1.1,
            "inputs_style": "pill",
            "show_widget_shadow": True,
            "widget_border_weight": 1.1,
            "widget_corner_radius": 1.1,
        },
        colors={
            "body_text": "body_text",
            "error": "error",
            "header": "header",
            "icons": "icons",
            "input_background": "input_background",
            "input_border": "input_border",
            "input_filled_text": "input_filled_text",
            "input_labels_placeholders": "input_labels_placeholders",
            "links_focused_components": "links_focused_components",
            "primary_button": "primary_button",
            "primary_button_label": "primary_button_label",
            "secondary_button_border": "secondary_button_border",
            "secondary_button_label": "secondary_button_label",
            "success": "success",
            "widget_background": "widget_background",
            "widget_border": "widget_border",
        },
        fonts={
            "body_text": {"bold": True, "size": 1.1},
            "buttons_text": {"bold": True, "size": 1.1},
            "font_url": "font_url",
            "input_labels": {"bold": True, "size": 1.1},
            "links": {"bold": True, "size": 1.1},
            "links_style": "normal",
            "reference_text_size": 1.1,
            "subtitle": {"bold": True, "size": 1.1},
            "title": {"bold": True, "size": 1.1},
        },
        page_background={
            "background_color": "background_color",
            "background_image_url": "background_image_url",
            "page_layout": "center",
        },
        widget={
            "header_text_alignment": "center",
            "logo_height": 1.1,
            "logo_position": "center",
            "logo_url": "logo_url",
            "social_buttons_layout": "bottom",
        },
    )
    verify_request_count(test_id, "POST", "/branding/themes", None, 1)


def test_branding_themes_get_default() -> None:
    """Test getDefault endpoint with WireMock"""
    test_id = "branding.themes.get_default.0"
    client = get_client(test_id)
    client.branding.themes.get_default()
    verify_request_count(test_id, "GET", "/branding/themes/default", None, 1)


def test_branding_themes_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "branding.themes.get.0"
    client = get_client(test_id)
    client.branding.themes.get(theme_id="themeId")
    verify_request_count(test_id, "GET", "/branding/themes/themeId", None, 1)


def test_branding_themes_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "branding.themes.delete.0"
    client = get_client(test_id)
    client.branding.themes.delete(theme_id="themeId")
    verify_request_count(test_id, "DELETE", "/branding/themes/themeId", None, 1)


def test_branding_themes_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "branding.themes.update.0"
    client = get_client(test_id)
    client.branding.themes.update(
        theme_id="themeId",
        borders={
            "button_border_radius": 1.1,
            "button_border_weight": 1.1,
            "buttons_style": "pill",
            "input_border_radius": 1.1,
            "input_border_weight": 1.1,
            "inputs_style": "pill",
            "show_widget_shadow": True,
            "widget_border_weight": 1.1,
            "widget_corner_radius": 1.1,
        },
        colors={
            "body_text": "body_text",
            "error": "error",
            "header": "header",
            "icons": "icons",
            "input_background": "input_background",
            "input_border": "input_border",
            "input_filled_text": "input_filled_text",
            "input_labels_placeholders": "input_labels_placeholders",
            "links_focused_components": "links_focused_components",
            "primary_button": "primary_button",
            "primary_button_label": "primary_button_label",
            "secondary_button_border": "secondary_button_border",
            "secondary_button_label": "secondary_button_label",
            "success": "success",
            "widget_background": "widget_background",
            "widget_border": "widget_border",
        },
        fonts={
            "body_text": {"bold": True, "size": 1.1},
            "buttons_text": {"bold": True, "size": 1.1},
            "font_url": "font_url",
            "input_labels": {"bold": True, "size": 1.1},
            "links": {"bold": True, "size": 1.1},
            "links_style": "normal",
            "reference_text_size": 1.1,
            "subtitle": {"bold": True, "size": 1.1},
            "title": {"bold": True, "size": 1.1},
        },
        page_background={
            "background_color": "background_color",
            "background_image_url": "background_image_url",
            "page_layout": "center",
        },
        widget={
            "header_text_alignment": "center",
            "logo_height": 1.1,
            "logo_position": "center",
            "logo_url": "logo_url",
            "social_buttons_layout": "bottom",
        },
    )
    verify_request_count(test_id, "PATCH", "/branding/themes/themeId", None, 1)
