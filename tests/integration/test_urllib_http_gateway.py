"""@file test_urllib_http_gateway.py
@brief Integration tests of UrllibHttpGateway against a local server only.
"""

import socket

import pytest

from exercise_tracker import get_exercises
from exercise_tracker.application.errors.api_error import ApiError
from exercise_tracker.application.errors.gateway_unreachable_error import (
    GatewayUnreachableError,
)
from exercise_tracker.domain.value_objects.exercise import Exercise
from exercise_tracker.domain.value_objects.exercise_query import ExerciseQuery
from exercise_tracker.domain.value_objects.nutritionix_credentials import (
    NutritionixCredentials,
)
from exercise_tracker.infrastructure.http.urllib_http_gateway import UrllibHttpGateway
from tests.integration.local_server import LOCAL_HOST, json_payload, serve

CREDENTIALS = NutritionixCredentials("test-app-id", "test-api-key")


def test_post_sends_headers_and_json_body_and_decodes_answer() -> None:
    answer = {"exercises": [{"name": "running", "duration_min": 30, "nf_calories": 3}]}
    with serve(200, json_payload(answer)) as server:
        exercises = get_exercises(
            UrllibHttpGateway(), CREDENTIALS, ExerciseQuery("ran 5k"), url=server.url
        )
    assert exercises == [Exercise("running", 30.0, 3.0)]
    request = server.requests[0]
    assert request.method == "POST"
    assert request.path == "/v1/nutrition/natural/exercise"
    assert request.headers["x-app-id"] == "test-app-id"
    assert request.headers["x-app-key"] == "test-api-key"
    assert request.headers["content-type"] == "application/json"
    assert request.body == b'{"query": "ran 5k"}'


def test_client_error_is_returned_not_raised() -> None:
    with serve(401, json_payload({"message": "bad key"})) as server:
        response = UrllibHttpGateway().post_json(server.url, {}, {"query": "x"})
    assert response.status_code == 401
    assert response.body == {"message": "bad key"}


def test_server_error_with_non_json_body_gives_empty_body() -> None:
    with serve(500, b"<html>oops</html>") as server:
        response = UrllibHttpGateway().post_json(server.url, {}, {})
    assert (response.status_code, response.body) == (500, {})


def test_use_case_raises_api_error_on_client_error() -> None:
    with (
        serve(400, json_payload({"message": "bad"})) as server,
        pytest.raises(ApiError) as caught,
    ):
        get_exercises(
            UrllibHttpGateway(), CREDENTIALS, ExerciseQuery("x"), url=server.url
        )
    assert caught.value.status_code == 400


def test_unreachable_port_raises_gateway_unreachable_error() -> None:
    with socket.socket() as probe:
        probe.bind((LOCAL_HOST, 0))
        port = probe.getsockname()[1]
    with pytest.raises(GatewayUnreachableError) as caught:
        UrllibHttpGateway(timeout=2).post_json(f"http://{LOCAL_HOST}:{port}/", {}, {})
    assert caught.value.__cause__ is not None
