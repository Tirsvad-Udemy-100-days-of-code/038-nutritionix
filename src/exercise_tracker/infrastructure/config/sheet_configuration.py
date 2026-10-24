"""@file sheet_configuration.py
@brief Reads the Sheety endpoint and authorization from the environment.

The choice between bearer and basic authentication is made here, so the use
cases do not know it. The project never reads or imports a `.env` file.
"""

from collections.abc import Mapping
from dataclasses import dataclass

from exercise_tracker import constants
from exercise_tracker.domain.errors.invalid_input_error import InvalidInputError
from exercise_tracker.domain.value_objects.sheet_authorization import (
    SheetAuthorization,
)
from exercise_tracker.domain.value_objects.sheet_endpoint import SheetEndpoint
from exercise_tracker.infrastructure.config.configuration_error import (
    ConfigurationError,
)


@dataclass(frozen=True, slots=True)
class SheetConfiguration:
    """@brief Where the rows go and how the request is authorized."""

    ## @brief The Sheety endpoint.
    endpoint: SheetEndpoint

    ## @brief The Authorization header value; never shown in `repr`.
    authorization: SheetAuthorization


def _value(environ: Mapping[str, str], name: str) -> str:
    """@brief Read one optional variable.

    @param environ The environment.
    @param name The name of the variable.
    @return The value, or an empty string when it is missing or blank.
    """
    value = environ.get(name, "")
    return value if value.strip() else ""


def _load_endpoint(environ: Mapping[str, str]) -> SheetEndpoint:
    """@brief Build the endpoint.

    @param environ The environment.
    @return The endpoint.
    @throws ConfigurationError SHEET_ENDPOINT is missing, blank or not a URL.
    """
    value = _value(environ, constants.ENV_SHEET_ENDPOINT)
    if not value:
        raise ConfigurationError(
            f"Environment variable {constants.ENV_SHEET_ENDPOINT} is missing or blank."
        )
    try:
        return SheetEndpoint(value)
    except InvalidInputError as error:
        raise ConfigurationError(
            f"Environment variable {constants.ENV_SHEET_ENDPOINT} "
            "must be an http or https URL."
        ) from error


def _load_authorization(environ: Mapping[str, str]) -> SheetAuthorization:
    """@brief Choose the authorization: bearer first, then basic.

    @param environ The environment.
    @return The authorization.
    @throws ConfigurationError No complete authorization is configured.
    """
    token = _value(environ, constants.ENV_TOKEN)
    if token:
        return SheetAuthorization.bearer(token)
    username = _value(environ, constants.ENV_USERNAME)
    password = _value(environ, constants.ENV_PASSWORD)
    if username and password:
        return SheetAuthorization.basic(username, password)
    raise ConfigurationError(
        f"Set environment variable {constants.ENV_TOKEN} (bearer), or both "
        f"{constants.ENV_USERNAME} and {constants.ENV_PASSWORD} (basic)."
    )


def load_sheet_configuration(environ: Mapping[str, str]) -> SheetConfiguration:
    """@brief Build the Sheety configuration from the environment.

    @param environ The environment, for example `os.environ`.
    @return The endpoint and the authorization; the bearer token wins.
    @throws ConfigurationError A variable is missing, blank or invalid.
    """
    return SheetConfiguration(_load_endpoint(environ), _load_authorization(environ))
