"""@file command_context.py
@brief What the composition root hands to a command.
"""

from collections.abc import Callable
from dataclasses import dataclass
from typing import TextIO

from exercise_tracker.application.ports.clock import Clock
from exercise_tracker.application.ports.http_gateway import HttpGateway
from exercise_tracker.domain.value_objects.nutritionix_credentials import (
    NutritionixCredentials,
)
from exercise_tracker.infrastructure.config.sheet_configuration import (
    SheetConfiguration,
)


@dataclass(frozen=True, slots=True)
class CommandContext:
    """@brief The ports, the credentials and the output stream of one run."""

    ## @brief The port used to send requests.
    gateway: HttpGateway

    ## @brief The Nutritionix credentials.
    credentials: NutritionixCredentials

    ## @brief The port that tells the time.
    clock: Clock

    ## @brief Reads the Sheety configuration when a command needs it.
    load_sheet: Callable[[], SheetConfiguration]

    ## @brief The stream the result is written to.
    out: TextIO
