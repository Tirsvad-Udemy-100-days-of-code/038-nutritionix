"""@file log_command.py
@brief The `log` command.
"""

from argparse import ArgumentParser, Namespace

from exercise_tracker.application.use_cases.log_workout import log_workout
from exercise_tracker.domain.value_objects.exercise_query import ExerciseQuery
from exercise_tracker.domain.value_objects.workout_row import WorkoutRow
from exercise_tracker.presentation.commands.command_context import CommandContext


def format_row(row: WorkoutRow) -> str:
    """@brief Format one logged row as a line of text.

    @param row The row.
    @return For example `24/10/2026 09:30:00 Running 30 300`.
    """
    return f"{row.date} {row.time} {row.exercise} " f"{row.duration:g} {row.calories:g}"


class LogCommand:
    """@brief Logs the exercises of a plain English sentence in the sheet."""

    name = "log"
    help = "Find the exercises of a sentence and add one row each to the sheet"

    def configure(self, parser: ArgumentParser) -> None:
        """@brief Add the sentence argument.

        @param parser The parser of the command.
        """
        parser.add_argument("sentence", help="what you did, in plain English")

    def execute(self, args: Namespace, context: CommandContext) -> None:
        """@brief Run the log workout use case and print one line per row.

        @param args The parsed arguments.
        @param context The ports, credentials and output stream of the run.
        @throws InvalidInputError The sentence is blank.
        @throws ConfigurationError The Sheety configuration is incomplete.
        """
        query = ExerciseQuery(args.sentence)
        sheet = context.load_sheet()
        rows = log_workout(
            context.gateway,
            context.credentials,
            sheet.endpoint,
            sheet.authorization,
            context.clock,
            query,
        )
        for row in rows:
            context.out.write(format_row(row) + "\n")
