"""@file get_exercises.py
@brief Use case: turn a plain English sentence into exercises.
"""

from collections.abc import Mapping

from exercise_tracker import constants
from exercise_tracker.application.errors.api_error import ApiError
from exercise_tracker.application.errors.malformed_response_error import (
    MalformedResponseError,
)
from exercise_tracker.application.ports.http_gateway import HttpGateway
from exercise_tracker.application.use_cases.error_message import short_message
from exercise_tracker.domain.errors.invalid_input_error import InvalidInputError
from exercise_tracker.domain.value_objects.exercise import Exercise
from exercise_tracker.domain.value_objects.exercise_query import ExerciseQuery
from exercise_tracker.domain.value_objects.nutritionix_credentials import (
    NutritionixCredentials,
)


def _number(item: Mapping[str, object], field_name: str) -> float:
    """@brief Read a number field of an exercise item.

    @param item The JSON object of one exercise.
    @param field_name The name of the field.
    @return The number.
    @throws MalformedResponseError The field is missing or not a number.
    """
    value = item.get(field_name)
    if isinstance(value, bool) or not isinstance(value, int | float):
        raise MalformedResponseError(f"The field '{field_name}' is not a number.")
    return float(value)


def _parse_exercise(item: object) -> Exercise:
    """@brief Build an exercise from one JSON item.

    @param item One element of the `exercises` list.
    @return The exercise.
    @throws MalformedResponseError The item has the wrong shape.
    """
    if not isinstance(item, dict):
        raise MalformedResponseError("An exercise is not a JSON object.")
    name = item.get(constants.FIELD_NAME)
    if not isinstance(name, str):
        raise MalformedResponseError(f"The field '{constants.FIELD_NAME}' is missing.")
    try:
        return Exercise(
            name,
            _number(item, constants.FIELD_DURATION_MIN),
            _number(item, constants.FIELD_CALORIES_NF),
        )
    except InvalidInputError as error:
        raise MalformedResponseError(str(error)) from error


def get_exercises(
    gateway: HttpGateway,
    credentials: NutritionixCredentials,
    query: ExerciseQuery,
    url: str = constants.NUTRITIONIX_EXERCISE_URL,
) -> list[Exercise]:
    """@brief Ask Nutritionix which exercises a sentence describes.

    @param gateway The port used to send the request.
    @param credentials The Nutritionix application id and API key.
    @param query The sentence, for example `ran 3 miles`.
    @param url The endpoint; the Nutritionix exercise endpoint by default.
    @return The exercises found, in the order of the answer.
    @throws ApiError The API answered with a status of 400 or more.
    @throws MalformedResponseError The answer cannot be understood.
    @throws GatewayUnreachableError The API could not be reached.
    """
    headers = {
        constants.HEADER_APP_ID: credentials.app_id,
        constants.HEADER_APP_KEY: credentials.api_key,
        constants.HEADER_CONTENT_TYPE: constants.CONTENT_TYPE_JSON,
    }
    response = gateway.post_json(url, headers, {constants.FIELD_QUERY: query.text})
    if response.status_code >= constants.HTTP_ERROR_STATUS_MIN:
        raise ApiError(response.status_code, short_message(response))
    items = response.body.get(constants.FIELD_EXERCISES)
    if not isinstance(items, list):
        raise MalformedResponseError(
            f"The answer has no '{constants.FIELD_EXERCISES}' list."
        )
    return [_parse_exercise(item) for item in items]
