"""@file test_add_workout_row.py
@brief Unit tests of the add_workout_row use case, with a fake gateway.
"""

import pytest

from exercise_tracker import add_workout_row
from exercise_tracker.application.dto.http_response import HttpResponse
from exercise_tracker.application.errors.api_error import ApiError
from exercise_tracker.domain.value_objects.sheet_authorization import (
    SheetAuthorization,
)
from exercise_tracker.domain.value_objects.sheet_endpoint import SheetEndpoint
from exercise_tracker.domain.value_objects.workout_row import WorkoutRow
from tests.unit.application.fake_http_gateway import FakeHttpGateway

ENDPOINT = SheetEndpoint("https://api.example.test/sheet/workouts")
ROW = WorkoutRow("05/03/2026", "07:08:09", "Running", 30.0, 300.5)


def test_posts_the_camel_case_body_with_headers_to_the_endpoint() -> None:
    gateway = FakeHttpGateway(HttpResponse(200, {"workout": {"id": 2}}))
    response = add_workout_row(
        gateway, ENDPOINT, SheetAuthorization.bearer("test-token"), ROW
    )
    assert response.status_code == 200
    assert gateway.requests == [
        (
            "https://api.example.test/sheet/workouts",
            {
                "Authorization": "Bearer test-token",
                "Content-Type": "application/json",
            },
            {
                "workout": {
                    "date": "05/03/2026",
                    "time": "07:08:09",
                    "exercise": "Running",
                    "duration": 30.0,
                    "calories": 300.5,
                }
            },
        )
    ]


@pytest.mark.parametrize("status", [400, 401, 403, 500])
def test_error_status_raises_api_error_without_secret(status: int) -> None:
    gateway = FakeHttpGateway(HttpResponse(status, {"message": "nope"}))
    with pytest.raises(ApiError) as caught:
        add_workout_row(gateway, ENDPOINT, SheetAuthorization.bearer("test-token"), ROW)
    assert caught.value.status_code == status
    assert "test-token" not in str(caught.value)
