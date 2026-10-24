"""@file exercises_command.py
@brief The `exercises` command.
"""

from argparse import ArgumentParser, Namespace

from exercise_tracker.application.use_cases.get_exercises import get_exercises
from exercise_tracker.domain.value_objects.exercise import Exercise
from exercise_tracker.domain.value_objects.exercise_query import ExerciseQuery
from exercise_tracker.presentation.commands.command_context import CommandContext


def format_exercise(exercise: Exercise) -> str:
    """@brief Format one exercise as a line of text.

    @param exercise The exercise.
    @return For example `Running: 30 min, 300 kcal`.
    """
    return (
        f"{exercise.name.title()}: {exercise.duration_min:g} min, "
        f"{exercise.calories:g} kcal"
    )


class ExercisesCommand:
    """@brief Finds the exercises of a plain English sentence."""

    name = "exercises"
    help = "Find the exercises and calories of a sentence such as 'ran 3 miles'"

    def configure(self, parser: ArgumentParser) -> None:
        """@brief Add the sentence argument.

        @param parser The parser of the command.
        """
        parser.add_argument("sentence", help="what you did, in plain English")

    def execute(self, args: Namespace, context: CommandContext) -> None:
        """@brief Run the get exercises use case and print one line each.

        @param args The parsed arguments.
        @param context The ports, credentials and output stream of the run.
        @throws InvalidInputError The sentence is blank.
        """
        query = ExerciseQuery(args.sentence)
        for exercise in get_exercises(context.gateway, context.credentials, query):
            context.out.write(format_exercise(exercise) + "\n")
