"""@file environment_credentials.py
@brief Reads the Nutritionix credentials from the process environment.

The project never reads or imports a `.env` file.
"""

from collections.abc import Mapping

from exercise_tracker import constants
from exercise_tracker.domain.value_objects.nutritionix_credentials import (
    NutritionixCredentials,
)
from exercise_tracker.infrastructure.config.configuration_error import (
    ConfigurationError,
)


def _required(environ: Mapping[str, str], name: str) -> str:
    """@brief Read one required variable.

    @param environ The environment.
    @param name The name of the variable.
    @return The value.
    @throws ConfigurationError The variable is missing or blank.
    """
    value = environ.get(name, "")
    if not value.strip():
        raise ConfigurationError(f"Environment variable {name} is missing or blank.")
    return value


def load_nutritionix_credentials(environ: Mapping[str, str]) -> NutritionixCredentials:
    """@brief Build the Nutritionix credentials from the environment.

    @param environ The environment, for example `os.environ`.
    @return The credentials.
    @throws ConfigurationError APP_ID or API_KEY is missing or blank.
    """
    return NutritionixCredentials(
        _required(environ, constants.ENV_APP_ID),
        _required(environ, constants.ENV_API_KEY),
    )
