"""@file workout_row.py
@brief One row of the workout sheet.
"""

from dataclasses import dataclass
from datetime import datetime

from exercise_tracker import constants
from exercise_tracker.domain.value_objects.exercise import Exercise


@dataclass(frozen=True, slots=True)
class WorkoutRow:
    """@brief The five columns of the sheet, ready to be posted."""

    ## @brief The date as day/month/year.
    date: str

    ## @brief The time as hours:minutes:seconds.
    time: str

    ## @brief The exercise name in title case.
    exercise: str

    ## @brief The duration in minutes.
    duration: float

    ## @brief The calories burned.
    calories: float

    @classmethod
    def from_exercise(cls, exercise: Exercise, moment: datetime) -> "WorkoutRow":
        """@brief Build the row of an exercise done at a moment.

        @param exercise The exercise found by Nutritionix.
        @param moment The date and time to record.
        @return The row; the numbers are kept unchanged.
        """
        return cls(
            moment.strftime(constants.DATE_FORMAT),
            moment.strftime(constants.TIME_FORMAT),
            exercise.name.title(),
            exercise.duration_min,
            exercise.calories,
        )
