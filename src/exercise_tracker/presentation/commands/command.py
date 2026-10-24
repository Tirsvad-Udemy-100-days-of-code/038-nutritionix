"""@file command.py
@brief The contract of a command line command.
"""

from argparse import ArgumentParser, Namespace
from typing import Protocol, TextIO

from exercise_tracker.application.ports.http_gateway import HttpGateway
from exercise_tracker.domain.value_objects.nutritionix_credentials import (
    NutritionixCredentials,
)


class Command(Protocol):
    """@brief One command of the program; it calls one use case."""

    ## @brief The name typed on the command line.
    name: str

    ## @brief The one line help text.
    help: str

    def configure(self, parser: ArgumentParser) -> None:
        """@brief Add the arguments of the command.

        @param parser The parser of the command.
        """
        ...

    def execute(
        self,
        args: Namespace,
        gateway: HttpGateway,
        credentials: NutritionixCredentials,
        out: TextIO,
    ) -> None:
        """@brief Run the use case and print its result.

        @param args The parsed arguments.
        @param gateway The port used to send requests.
        @param credentials The Nutritionix credentials.
        @param out The stream the result is written to.
        """
        ...
