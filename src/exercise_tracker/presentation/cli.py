"""@file cli.py
@brief The command line: composition root of the program.

This is the one place that builds the adapters and hands them to the commands.
"""

import argparse
import os
import sys
from collections.abc import Mapping, Sequence
from typing import TextIO

from exercise_tracker import constants
from exercise_tracker.application.errors.api_error import ApiError
from exercise_tracker.application.errors.gateway_unreachable_error import (
    GatewayUnreachableError,
)
from exercise_tracker.application.errors.malformed_response_error import (
    MalformedResponseError,
)
from exercise_tracker.application.ports.http_gateway import HttpGateway
from exercise_tracker.domain.errors.invalid_input_error import InvalidInputError
from exercise_tracker.infrastructure.config.configuration_error import (
    ConfigurationError,
)
from exercise_tracker.infrastructure.config.environment_credentials import (
    load_nutritionix_credentials,
)
from exercise_tracker.infrastructure.http.dry_run_http_gateway import (
    DryRunHttpGateway,
)
from exercise_tracker.infrastructure.http.urllib_http_gateway import UrllibHttpGateway
from exercise_tracker.presentation.commands.command import Command
from exercise_tracker.presentation.commands.exercises_command import ExercisesCommand

## @brief The commands of the program, one per use case.
COMMANDS: tuple[Command, ...] = (ExercisesCommand(),)


def build_parser(commands: Sequence[Command]) -> argparse.ArgumentParser:
    """@brief Build the argument parser.

    @param commands The commands to offer.
    @return The parser, with one sub command per command.
    """
    parser = argparse.ArgumentParser(
        prog=constants.PROGRAM_NAME,
        description="Log workouts from plain English with Nutritionix.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the request with the secrets hidden and send nothing",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in commands:
        command.configure(subparsers.add_parser(command.name, help=command.help))
    return parser


def _build_gateway(dry_run: bool, out: TextIO) -> HttpGateway:
    """@brief Choose the gateway.

    @param dry_run True to print the request and send nothing.
    @param out The stream the dry-run gateway prints to.
    @return The dry-run gateway or the real one.
    """
    if dry_run:
        return DryRunHttpGateway(out)
    return UrllibHttpGateway()


def _report(error: Exception) -> None:
    """@brief Write an error message to standard error.

    @param error The error; its message never holds a secret.
    """
    sys.stderr.write(f"Error: {error}\n")


def main(
    argv: Sequence[str] | None = None,
    environ: Mapping[str, str] | None = None,
    stdout: TextIO | None = None,
) -> int:
    """@brief Run the program.

    @param argv The arguments; `sys.argv` when omitted.
    @param environ The environment; `os.environ` when omitted.
    @param stdout The output stream; standard output when omitted.
    @return One of the EXIT_* codes.
    """
    out = stdout if stdout is not None else sys.stdout
    env = environ if environ is not None else os.environ
    args = build_parser(COMMANDS).parse_args(argv)
    command = next(c for c in COMMANDS if c.name == args.command)
    gateway = _build_gateway(args.dry_run, out)
    try:
        credentials = load_nutritionix_credentials(env)
        command.execute(args, gateway, credentials, out)
    except (InvalidInputError, ConfigurationError) as error:
        _report(error)
        return constants.EXIT_INVALID
    except (ApiError, MalformedResponseError) as error:
        _report(error)
        return constants.EXIT_REJECTED
    except GatewayUnreachableError as error:
        _report(error)
        return constants.EXIT_UNREACHABLE
    return constants.EXIT_OK
