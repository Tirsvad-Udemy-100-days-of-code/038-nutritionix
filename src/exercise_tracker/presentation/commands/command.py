"""@file command.py
@brief The contract of a command line command.
"""

from argparse import ArgumentParser, Namespace
from typing import Protocol

from exercise_tracker.presentation.commands.command_context import CommandContext


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

    def execute(self, args: Namespace, context: CommandContext) -> None:
        """@brief Run the use case and print its result.

        @param args The parsed arguments.
        @param context The ports, credentials and output stream of the run.
        """
        ...
