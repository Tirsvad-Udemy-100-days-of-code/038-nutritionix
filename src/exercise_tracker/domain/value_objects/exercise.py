"""@file exercise.py
@brief One exercise found by Nutritionix.
"""

import math
from dataclasses import dataclass

from exercise_tracker.domain.errors.invalid_input_error import InvalidInputError


@dataclass(frozen=True, slots=True)
class Exercise:
    """@brief An exercise with its duration and the calories it burned."""

    ## @brief The name of the exercise, for example `running`.
    name: str

    ## @brief The duration in minutes; not negative.
    duration_min: float

    ## @brief The calories burned; not negative.
    calories: float

    def __post_init__(self) -> None:
        """@brief Check the rules of an exercise.

        @throws InvalidInputError The name is blank or a number is negative.
        """
        if not self.name.strip():
            raise InvalidInputError("The exercise name must not be blank.")
        for label, value in (
            ("duration", self.duration_min),
            ("calories", self.calories),
        ):
            if math.isnan(value) or value < 0:
                raise InvalidInputError(f"The exercise {label} must not be negative.")
