"""@file test_sheety_log.py
@brief Integration tests of log_workout against a local server only.
"""

import json
from collections.abc import Mapping

from exercise_tracker import log_workout
from exercise_tracker.application.dto.http_response import HttpResponse
from exercise_tracker.domain.value_objects.exercise_query import ExerciseQuery
from exercise_tracker.domain.value_objects.nutritionix_credentials import (
    NutritionixCredentials,
)
from exercise_tracker.domain.value_objects.sheet_authorization import (
    SheetAuthorization,
)
from exercise_tracker.domain.value_objects.sheet_endpoint import SheetEndpoint
from exercise_tracker.infrastructure.http.urllib_http_gateway import UrllibHttpGateway
from tests.integration.local_server import json_payload, serve
from tests.unit.application.fixed_clock import FixedClock

CREDENTIALS = NutritionixCredentials("test-app-id", "test-api-key")
NUTRITIONIX_PATH = "/v2/natural/exercise"
SHEET_PATH = "/sheet/workouts"
ANSWER = {
    "exercises": [
        {"name": "running", "duration_min": 30, "nf_calories": 300},
        {"name": "weight lifting", "duration_min": 20, "nf_calories": 90},
    ]
}


def test_query_then_one_authorized_post_per_exercise() -> None:
    routes = {NUTRITIONIX_PATH: json_payload(ANSWER)}
    with serve(200, json_payload({"workout": {"id": 2}}), routes) as server:
        # Both endpoints live on the one local server; get_exercises uses its
        # default Nutritionix URL, so the query goes through a redirecting gateway.
        rows = log_workout(
            _RedirectingGateway(server.url_for(NUTRITIONIX_PATH)),
            CREDENTIALS,
            SheetEndpoint(server.url_for(SHEET_PATH)),
            SheetAuthorization.bearer("test-token"),
            FixedClock(),
            ExerciseQuery("ran 5k and lifted weights"),
        )
    assert [row.exercise for row in rows] == ["Running", "Weight Lifting"]
    query, *posts = server.requests
    assert query.path == NUTRITIONIX_PATH
    assert query.headers["x-app-id"] == "test-app-id"
    assert "authorization" not in query.headers
    assert [post.path for post in posts] == [SHEET_PATH, SHEET_PATH]
    for post in posts:
        assert post.headers["authorization"] == "Bearer test-token"
        assert post.headers["content-type"] == "application/json"
    assert json.loads(posts[0].body) == {
        "workout": {
            "date": "05/03/2026",
            "time": "07:08:09",
            "exercise": "Running",
            "duration": 30.0,
            "calories": 300.0,
        }
    }
    assert json.loads(posts[1].body)["workout"]["exercise"] == "Weight Lifting"


class _RedirectingGateway:
    """@brief Real urllib gateway that sends the Nutritionix URL to a local one."""

    def __init__(self, nutritionix_url: str) -> None:
        """@brief Create the gateway.

        @param nutritionix_url The local URL that replaces the Nutritionix URL.
        """
        self._nutritionix_url = nutritionix_url
        self._inner = UrllibHttpGateway(timeout=2)

    def post_json(
        self, url: str, headers: Mapping[str, str], body: Mapping[str, object]
    ) -> HttpResponse:
        """@brief Send the request, replacing only the Nutritionix URL.

        @param url The full URL.
        @param headers The HTTP headers.
        @param body The JSON body.
        @return The answer of the local server.
        """
        if url.startswith("https://trackapi.nutritionix.com"):
            url = self._nutritionix_url
        return self._inner.post_json(url, headers, body)
