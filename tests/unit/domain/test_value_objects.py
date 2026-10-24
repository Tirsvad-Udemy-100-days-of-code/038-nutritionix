"""@file test_value_objects.py
@brief Unit tests of the domain value objects.
"""

import dataclasses

import pytest

from exercise_tracker.domain.errors.invalid_input_error import InvalidInputError
from exercise_tracker.domain.value_objects.exercise import Exercise
from exercise_tracker.domain.value_objects.exercise_query import ExerciseQuery
from exercise_tracker.domain.value_objects.nutritionix_credentials import (
    NutritionixCredentials,
)


def test_exercise_keeps_its_values() -> None:
    exercise = Exercise("running", 30.0, 300.0)
    assert (exercise.name, exercise.duration_min, exercise.calories) == (
        "running",
        30.0,
        300.0,
    )


def test_exercise_is_immutable() -> None:
    exercise = Exercise("running", 30.0, 300.0)
    with pytest.raises(dataclasses.FrozenInstanceError):
        exercise.name = "walking"  # type: ignore[misc]


@pytest.mark.parametrize(
    ("name", "duration", "calories"),
    [
        ("  ", 1.0, 1.0),
        ("running", -1.0, 1.0),
        ("running", 1.0, -0.5),
        ("running", float("nan"), 1.0),
    ],
)
def test_exercise_rejects_invalid_values(
    name: str, duration: float, calories: float
) -> None:
    with pytest.raises(InvalidInputError):
        Exercise(name, duration, calories)


def test_exercise_accepts_zero() -> None:
    assert Exercise("rest", 0.0, 0.0).calories == 0.0


def test_query_is_stripped() -> None:
    assert ExerciseQuery("  ran 5k \n").text == "ran 5k"


@pytest.mark.parametrize("text", ["", "   ", "\n\t"])
def test_query_rejects_blank_text(text: str) -> None:
    with pytest.raises(InvalidInputError):
        ExerciseQuery(text)


def test_credentials_hide_values_in_repr_and_str() -> None:
    credentials = NutritionixCredentials("test-app-id", "test-api-key")
    shown = f"{credentials!r} {credentials!s}"
    assert "test-app-id" not in shown
    assert "test-api-key" not in shown


def test_credentials_keep_their_values() -> None:
    credentials = NutritionixCredentials("test-app-id", "test-api-key")
    assert (credentials.app_id, credentials.api_key) == ("test-app-id", "test-api-key")


@pytest.mark.parametrize(("app_id", "api_key"), [("", "key"), ("id", " ")])
def test_credentials_reject_blank_values(app_id: str, api_key: str) -> None:
    with pytest.raises(InvalidInputError) as caught:
        NutritionixCredentials(app_id, api_key)
    assert "key" not in str(caught.value).replace("API key", "")
