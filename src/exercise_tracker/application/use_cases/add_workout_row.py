"""@file add_workout_row.py
@brief Use case: add one row to the workout sheet.
"""

from exercise_tracker import constants
from exercise_tracker.application.dto.http_response import HttpResponse
from exercise_tracker.application.errors.api_error import ApiError
from exercise_tracker.application.ports.http_gateway import HttpGateway
from exercise_tracker.application.use_cases.error_message import short_message
from exercise_tracker.domain.value_objects.sheet_authorization import (
    SheetAuthorization,
)
from exercise_tracker.domain.value_objects.sheet_endpoint import SheetEndpoint
from exercise_tracker.domain.value_objects.workout_row import WorkoutRow


def add_workout_row(
    gateway: HttpGateway,
    endpoint: SheetEndpoint,
    authorization: SheetAuthorization,
    row: WorkoutRow,
) -> HttpResponse:
    """@brief Post one row to the Sheety endpoint.

    @param gateway The port used to send the request.
    @param endpoint The Sheety endpoint of the sheet.
    @param authorization The Authorization header value.
    @param row The row to add.
    @return The answer of Sheety.
    @throws ApiError Sheety answered with a status of 400 or more.
    @throws GatewayUnreachableError Sheety could not be reached.
    """
    headers = {
        constants.HEADER_AUTHORIZATION: authorization.header_value,
        constants.HEADER_CONTENT_TYPE: constants.CONTENT_TYPE_JSON,
    }
    body: dict[str, object] = {
        constants.FIELD_WORKOUT: {
            constants.FIELD_DATE: row.date,
            constants.FIELD_TIME: row.time,
            constants.FIELD_EXERCISE: row.exercise,
            constants.FIELD_DURATION: row.duration,
            constants.FIELD_CALORIES: row.calories,
        }
    }
    response = gateway.post_json(endpoint.url, headers, body)
    if response.status_code >= constants.HTTP_ERROR_STATUS_MIN:
        raise ApiError(response.status_code, short_message(response))
    return response
