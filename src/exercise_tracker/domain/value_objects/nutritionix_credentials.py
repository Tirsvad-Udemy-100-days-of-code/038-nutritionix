"""@file nutritionix_credentials.py
@brief The application id and API key of a Nutritionix account.
"""

from dataclasses import dataclass, field

from exercise_tracker.constants import HIDDEN_SECRET
from exercise_tracker.domain.errors.invalid_input_error import InvalidInputError


@dataclass(frozen=True, slots=True)
class NutritionixCredentials:
    """@brief The two secrets that identify a Nutritionix account.

    The values never appear in `repr` or `str`.
    """

    ## @brief The application id.
    app_id: str = field(repr=False)

    ## @brief The API key.
    api_key: str = field(repr=False)

    def __post_init__(self) -> None:
        """@brief Check that both secrets are present.

        @throws InvalidInputError A value is blank.
        """
        if not self.app_id.strip():
            raise InvalidInputError("The application id must not be blank.")
        if not self.api_key.strip():
            raise InvalidInputError("The API key must not be blank.")

    def __repr__(self) -> str:
        """@brief Show the class with the secrets hidden.

        @return The masked text.
        """
        return (
            f"NutritionixCredentials(app_id={HIDDEN_SECRET}, api_key={HIDDEN_SECRET})"
        )

    def __str__(self) -> str:
        """@brief Show the class with the secrets hidden.

        @return The masked text.
        """
        return self.__repr__()
