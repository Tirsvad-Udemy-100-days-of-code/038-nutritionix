"""@file test_get_exercises.py
@brief Unit tests of the get_exercises use case, with a fake gateway.
"""

import pytest

from exercise_tracker import get_exercises
from exercise_tracker.application.dto.http_response import HttpResponse
from exercise_tracker.application.errors.api_error import ApiError
from exercise_tracker.application.errors.malformed_response_error import (
    MalformedResponseError,
)
from exercise_tracker.constants import NUTRITIONIX_EXERCISE_URL
from exercise_tracker.domain.errors.invalid_input_error import InvalidInputError
from exercise_tracker.domain.value_objects.exercise import Exercise
from exercise_tracker.domain.value_objects.exercise_query import ExerciseQuery
from exercise_tracker.domain.value_objects.nutritionix_credentials import (
    NutritionixCredentials,
)
from tests.unit.application.fake_http_gateway import FakeHttpGateway

CREDENTIALS = NutritionixCredentials("test-app-id", "test-api-key")


def _ok(body: dict[str, object]) -> FakeHttpGateway:
    return FakeHttpGateway(HttpResponse(200, body))


def test_sends_post_to_nutritionix_with_headers_and_query() -> None:
    gateway = _ok({"exercises": []})
    get_exercises(gateway, CREDENTIALS, ExerciseQuery("  ran 5k "))
    assert gateway.requests == [
        (
            NUTRITIONIX_EXERCISE_URL,
            {
                "x-app-id": "test-app-id",
                "x-app-key": "test-api-key",
                "Content-Type": "application/json",
            },
            {"query": "ran 5k"},
        )
    ]


def test_uses_the_given_url() -> None:
    gateway = _ok({"exercises": []})
    get_exercises(gateway, CREDENTIALS, ExerciseQuery("x"), url="http://127.0.0.1/x")
    assert gateway.requests[0][0] == "http://127.0.0.1/x"


def test_parses_exercises_and_ignores_extra_fields() -> None:
    gateway = _ok(
        {
            "exercises": [
                {
                    "name": "running",
                    "duration_min": 30,
                    "nf_calories": 300.5,
                    "tag_id": 1,
                },
                {"name": "walking", "duration_min": 10.0, "nf_calories": 40.0},
            ],
            "other": 1,
        }
    )
    assert get_exercises(gateway, CREDENTIALS, ExerciseQuery("x")) == [
        Exercise("running", 30.0, 300.5),
        Exercise("walking", 10.0, 40.0),
    ]


def test_empty_query_is_rejected_before_any_request() -> None:
    gateway = _ok({"exercises": []})
    with pytest.raises(InvalidInputError):
        get_exercises(gateway, CREDENTIALS, ExerciseQuery("   "))
    assert gateway.requests == []


@pytest.mark.parametrize("status", [400, 401, 404, 500])
def test_error_status_raises_api_error(status: int) -> None:
    gateway = FakeHttpGateway(HttpResponse(status, {"message": "nope"}))
    with pytest.raises(ApiError) as caught:
        get_exercises(gateway, CREDENTIALS, ExerciseQuery("x"))
    assert caught.value.status_code == status
    assert caught.value.message == "nope"
    assert "test-api-key" not in str(caught.value)


def test_error_status_without_message_still_raises_api_error() -> None:
    gateway = FakeHttpGateway(HttpResponse(500, {}))
    with pytest.raises(ApiError) as caught:
        get_exercises(gateway, CREDENTIALS, ExerciseQuery("x"))
    assert caught.value.message == "no message"


@pytest.mark.parametrize(
    "body",
    [
        {},
        {"exercises": "running"},
        {"exercises": ["running"]},
        {"exercises": [{"duration_min": 1, "nf_calories": 1}]},
        {"exercises": [{"name": "a", "duration_min": "1", "nf_calories": 1}]},
        {"exercises": [{"name": "a", "duration_min": True, "nf_calories": 1}]},
        {"exercises": [{"name": "a", "duration_min": 1}]},
        {"exercises": [{"name": "a", "duration_min": -1, "nf_calories": 1}]},
    ],
)
def test_malformed_answer_raises_specific_error(body: dict[str, object]) -> None:
    with pytest.raises(MalformedResponseError):
        get_exercises(_ok(body), CREDENTIALS, ExerciseQuery("x"))
