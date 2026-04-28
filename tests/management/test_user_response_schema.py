import pytest

from auth0.management.types.user_response_schema import UserResponseSchema


class TestEmailVerifiedStrBool:
    """Tests that email_verified accepts both bool and string values."""

    def test_bool_true(self):
        user = UserResponseSchema(email_verified=True)
        assert user.email_verified is True

    def test_bool_false(self):
        user = UserResponseSchema(email_verified=False)
        assert user.email_verified is False

    def test_none(self):
        user = UserResponseSchema(email_verified=None)
        assert user.email_verified is None

    def test_default_none(self):
        user = UserResponseSchema()
        assert user.email_verified is None

    def test_nonempty_string_is_true(self):
        user = UserResponseSchema(email_verified="user@example.com")
        assert user.email_verified is True

    def test_empty_string_is_false(self):
        user = UserResponseSchema(email_verified="")
        assert user.email_verified is False

    def test_whitespace_only_string_is_false(self):
        user = UserResponseSchema(email_verified="   ")
        assert user.email_verified is False

    def test_serialization_true_to_int(self):
        user = UserResponseSchema(email_verified=True)
        data = user.dict()
        assert data["email_verified"] == 1

    def test_serialization_false_to_int(self):
        user = UserResponseSchema(email_verified=False)
        data = user.dict()
        assert data["email_verified"] == 0

    def test_serialization_string_true_to_int(self):
        user = UserResponseSchema(email_verified="verified")
        data = user.dict()
        assert data["email_verified"] == 1

    def test_serialization_empty_string_to_int(self):
        user = UserResponseSchema(email_verified="")
        data = user.dict()
        assert data["email_verified"] == 0
