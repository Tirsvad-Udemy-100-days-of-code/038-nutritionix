"""@file test_sheet_value_objects.py
@brief Unit tests of WorkoutRow, SheetEndpoint and SheetAuthorization.
"""

import base64
from dataclasses import FrozenInstanceError
from datetime import datetime

import pytest

from exercise_tracker.domain.errors.invalid_input_error import InvalidInputError
from exercise_tracker.domain.value_objects.exercise import Exercise
from exercise_tracker.domain.value_objects.sheet_authorization import (
    SheetAuthorization,
)
from exercise_tracker.domain.value_objects.sheet_endpoint import SheetEndpoint
from exercise_tracker.domain.value_objects.workout_row import WorkoutRow


@pytest.mark.parametrize(
    ("name", "expected"),
    [("running", "Running"), ("weight lifting", "Weight Lifting")],
)
def test_row_formats_date_time_and_title_case_name(name: str, expected: str) -> None:
    row = WorkoutRow.from_exercise(
        Exercise(name, 30.0, 300.5), datetime(2026, 3, 5, 7, 8, 9)
    )
    assert row == WorkoutRow("05/03/2026", "07:08:09", expected, 30.0, 300.5)


def test_row_is_immutable() -> None:
    row = WorkoutRow("05/03/2026", "07:08:09", "Running", 1.0, 2.0)
    with pytest.raises(FrozenInstanceError):
        row.exercise = "x"  # type: ignore[misc]


def test_endpoint_is_stripped_and_accepts_http_and_https() -> None:
    assert SheetEndpoint(" https://a.test/x ").url == "https://a.test/x"
    assert SheetEndpoint("http://127.0.0.1:1/x").url == "http://127.0.0.1:1/x"


@pytest.mark.parametrize("url", ["", "   ", "ftp://a.test", "a.test/x"])
def test_endpoint_rejects_blank_or_other_scheme(url: str) -> None:
    with pytest.raises(InvalidInputError):
        SheetEndpoint(url)


def test_bearer_header_value() -> None:
    assert SheetAuthorization.bearer("test-token").header_value == "Bearer test-token"


def test_basic_header_value_is_base64_of_user_and_password() -> None:
    value = SheetAuthorization.basic("test-user", "test-pass").header_value
    scheme, encoded = value.split(" ")
    assert scheme == "Basic"
    assert base64.b64decode(encoded) == b"test-user:test-pass"


@pytest.mark.parametrize("secret", ["test-token", "test-user", "test-pass"])
def test_authorization_repr_and_str_hide_secrets(secret: str) -> None:
    for authorization in (
        SheetAuthorization.bearer("test-token"),
        SheetAuthorization.basic("test-user", "test-pass"),
    ):
        assert secret not in repr(authorization)
        assert secret not in str(authorization)
        assert "dGVzdC11c2VyOnRlc3QtcGFzcw" not in repr(authorization)


def test_authorization_rejects_blank_values() -> None:
    with pytest.raises(InvalidInputError):
        SheetAuthorization.bearer(" ")
    with pytest.raises(InvalidInputError):
        SheetAuthorization.basic(" ", "p")
    with pytest.raises(InvalidInputError):
        SheetAuthorization.basic("u", " ")
