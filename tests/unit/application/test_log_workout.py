"""@file test_log_workout.py
@brief Unit tests of the log_workout use case, with a fake gateway and clock.
"""

from collections.abc import Mapping

import pytest

from exercise_tracker import log_workout
from exercise_tracker.application.dto.http_response import HttpResponse
from exercise_tracker.application.errors.api_error import ApiError
from exercise_tracker.constants import NUTRITIONIX_EXERCISE_URL
from exercise_tracker.domain.value_objects.exercise_query import ExerciseQuery
from exercise_tracker.domain.value_objects.nutritionix_credentials import (
    NutritionixCredentials,
)
from exercise_tracker.domain.value_objects.sheet_authorization import (
    SheetAuthorization,
)
from exercise_tracker.domain.value_objects.sheet_endpoint import SheetEndpoint
from exercise_tracker.domain.value_objects.workout_row import WorkoutRow
from tests.unit.application.fake_http_gateway import FakeHttpGateway
from tests.unit.application.fixed_clock import FixedClock

CREDENTIALS = NutritionixCredentials("test-app-id", "test-api-key")
SHEET_URL = "https://api.example.test/sheet/workouts"
ENDPOINT = SheetEndpoint(SHEET_URL)
AUTHORIZATION = SheetAuthorization.bearer("test-token")
TWO_EXERCISES: dict[str, object] = {
    "exercises": [
        {"name": "running", "duration_min": 30, "nf_calories": 300.5},
        {"name": "weight lifting", "duration_min": 20, "nf_calories": 90},
    ]
}


def _log(gateway: FakeHttpGateway, clock: FixedClock) -> list[WorkoutRow]:
    return log_workout(
        gateway, CREDENTIALS, ENDPOINT, AUTHORIZATION, clock, ExerciseQuery("ran 5k")
    )


def test_one_query_and_one_post_per_exercise() -> None:
    gateway = FakeHttpGateway(HttpResponse(200, TWO_EXERCISES))
    rows = _log(gateway, FixedClock())
    assert [request[0] for request in gateway.requests] == [
        NUTRITIONIX_EXERCISE_URL,
        SHEET_URL,
        SHEET_URL,
    ]
    assert gateway.requests[0][2] == {"query": "ran 5k"}
    assert [request[2] for request in gateway.requests[1:]] == [
        {
            "workout": {
                "date": "05/03/2026",
                "time": "07:08:09",
                "exercise": "Running",
                "duration": 30.0,
                "calories": 300.5,
            }
        },
        {
            "workout": {
                "date": "05/03/2026",
                "time": "07:08:09",
                "exercise": "Weight Lifting",
                "duration": 20.0,
                "calories": 90.0,
            }
        },
    ]
    assert [row.exercise for row in rows] == ["Running", "Weight Lifting"]


def test_sheet_requests_carry_the_authorization_header() -> None:
    gateway = FakeHttpGateway(HttpResponse(200, TWO_EXERCISES))
    _log(gateway, FixedClock())
    assert gateway.requests[1][1]["Authorization"] == "Bearer test-token"
    assert "Authorization" not in gateway.requests[0][1]


def test_no_exercise_means_no_post() -> None:
    gateway = FakeHttpGateway(HttpResponse(200, {"exercises": []}))
    assert _log(gateway, FixedClock()) == []
    assert len(gateway.requests) == 1


def test_clock_is_read_once_for_all_rows() -> None:
    clock = FixedClock()
    _log(FakeHttpGateway(HttpResponse(200, TWO_EXERCISES)), clock)
    assert clock.calls == 1


def test_sheet_refusal_raises_api_error() -> None:
    class Refusing(FakeHttpGateway):
        def post_json(
            self, url: str, headers: Mapping[str, str], body: Mapping[str, object]
        ) -> HttpResponse:
            if url == SHEET_URL:
                return HttpResponse(401, {"message": "unauthorized"})
            return HttpResponse(200, TWO_EXERCISES)

    with pytest.raises(ApiError) as caught:
        _log(Refusing(HttpResponse(200, {})), FixedClock())
    assert caught.value.status_code == 401
