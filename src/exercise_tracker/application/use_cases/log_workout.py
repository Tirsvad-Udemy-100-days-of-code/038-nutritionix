"""@file log_workout.py
@brief Use case: find the exercises of a sentence and log each in the sheet.
"""

from exercise_tracker.application.ports.clock import Clock
from exercise_tracker.application.ports.http_gateway import HttpGateway
from exercise_tracker.application.use_cases.add_workout_row import add_workout_row
from exercise_tracker.application.use_cases.get_exercises import get_exercises
from exercise_tracker.domain.value_objects.exercise_query import ExerciseQuery
from exercise_tracker.domain.value_objects.nutritionix_credentials import (
    NutritionixCredentials,
)
from exercise_tracker.domain.value_objects.sheet_authorization import (
    SheetAuthorization,
)
from exercise_tracker.domain.value_objects.sheet_endpoint import SheetEndpoint
from exercise_tracker.domain.value_objects.workout_row import WorkoutRow


def log_workout(
    gateway: HttpGateway,
    credentials: NutritionixCredentials,
    endpoint: SheetEndpoint,
    authorization: SheetAuthorization,
    clock: Clock,
    query: ExerciseQuery,
) -> list[WorkoutRow]:
    """@brief Query Nutritionix once, then post one row per exercise.

    @param gateway The port used to send requests.
    @param credentials The Nutritionix credentials.
    @param endpoint The Sheety endpoint of the sheet.
    @param authorization The Sheety Authorization header value.
    @param clock The port that tells the date and time of the rows.
    @param query The sentence, for example `ran 3 miles`.
    @return The rows that were posted, in the order of the exercises.
    @throws ApiError An API answered with a status of 400 or more.
    @throws MalformedResponseError The Nutritionix answer cannot be understood.
    @throws GatewayUnreachableError An API could not be reached.
    """
    moment = clock.now()
    rows = [
        WorkoutRow.from_exercise(exercise, moment)
        for exercise in get_exercises(gateway, credentials, query)
    ]
    for row in rows:
        add_workout_row(gateway, endpoint, authorization, row)
    return rows
