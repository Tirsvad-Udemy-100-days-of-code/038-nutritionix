"""@file test_dry_run_sheety.py
@brief Unit tests that the dry-run gateway hides the Sheety secrets.
"""

import io

from exercise_tracker import add_workout_row
from exercise_tracker.constants import HIDDEN_SECRET
from exercise_tracker.domain.value_objects.sheet_authorization import (
    SheetAuthorization,
)
from exercise_tracker.domain.value_objects.sheet_endpoint import SheetEndpoint
from exercise_tracker.domain.value_objects.workout_row import WorkoutRow
from exercise_tracker.infrastructure.http.dry_run_http_gateway import (
    DryRunHttpGateway,
)

ROW = WorkoutRow("05/03/2026", "07:08:09", "Running", 30.0, 300.0)


def test_sheety_request_is_printed_without_the_authorization_value() -> None:
    out = io.StringIO()
    for authorization in (
        SheetAuthorization.bearer("test-token"),
        SheetAuthorization.basic("test-user", "test-pass"),
    ):
        add_workout_row(
            DryRunHttpGateway(out),
            SheetEndpoint("https://api.example.test/sheet/workouts"),
            authorization,
            ROW,
        )
    text = out.getvalue()
    assert "POST https://api.example.test/sheet/workouts" in text
    assert f"Authorization: {HIDDEN_SECRET}" in text
    assert '"exercise": "Running"' in text
    for secret in ("test-token", "test-user", "test-pass", "Bearer", "Basic"):
        assert secret not in text
