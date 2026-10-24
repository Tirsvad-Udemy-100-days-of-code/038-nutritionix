"""@file test_sheet_configuration.py
@brief Unit tests of the Sheety configuration and the system clock.
"""

from datetime import datetime, timedelta

import pytest

from exercise_tracker.domain.value_objects.sheet_authorization import (
    SheetAuthorization,
)
from exercise_tracker.infrastructure.clock.system_clock import SystemClock
from exercise_tracker.infrastructure.config.configuration_error import (
    ConfigurationError,
)
from exercise_tracker.infrastructure.config.sheet_configuration import (
    load_sheet_configuration,
)

URL = "https://api.example.test/sheet/workouts"


def test_token_selects_bearer() -> None:
    config = load_sheet_configuration({"SHEET_ENDPOINT": URL, "TOKEN": "test-token"})
    assert config.endpoint.url == URL
    assert config.authorization == SheetAuthorization.bearer("test-token")


def test_username_and_password_select_basic() -> None:
    config = load_sheet_configuration(
        {"SHEET_ENDPOINT": URL, "USERNAME": "test-user", "PASSWORD": "test-pass"}
    )
    assert config.authorization == SheetAuthorization.basic("test-user", "test-pass")


def test_bearer_wins_when_both_are_set() -> None:
    config = load_sheet_configuration(
        {
            "SHEET_ENDPOINT": URL,
            "TOKEN": "test-token",
            "USERNAME": "test-user",
            "PASSWORD": "test-pass",
        }
    )
    assert config.authorization.header_value == "Bearer test-token"


def test_blank_token_falls_back_to_basic() -> None:
    config = load_sheet_configuration(
        {
            "SHEET_ENDPOINT": URL,
            "TOKEN": "  ",
            "USERNAME": "test-user",
            "PASSWORD": "test-pass",
        }
    )
    assert config.authorization.header_value.startswith("Basic ")


def test_username_alone_is_not_basic_authentication() -> None:
    with pytest.raises(ConfigurationError) as caught:
        load_sheet_configuration({"SHEET_ENDPOINT": URL, "USERNAME": "test-user"})
    message = str(caught.value)
    assert "TOKEN" in message
    assert "PASSWORD" in message
    assert "test-user" not in message


def test_missing_authorization_names_the_variables() -> None:
    with pytest.raises(ConfigurationError) as caught:
        load_sheet_configuration({"SHEET_ENDPOINT": URL})
    message = str(caught.value)
    assert "TOKEN" in message
    assert "USERNAME" in message
    assert "PASSWORD" in message


@pytest.mark.parametrize("environ", [{}, {"SHEET_ENDPOINT": "  "}])
def test_missing_endpoint_names_the_variable_and_shows_no_value(
    environ: dict[str, str],
) -> None:
    with pytest.raises(ConfigurationError) as caught:
        load_sheet_configuration({**environ, "TOKEN": "test-token"})
    message = str(caught.value)
    assert "SHEET_ENDPOINT" in message
    assert "test-token" not in message


def test_endpoint_that_is_not_http_is_a_configuration_error() -> None:
    with pytest.raises(ConfigurationError) as caught:
        load_sheet_configuration({"SHEET_ENDPOINT": "ftp://secret.test", "TOKEN": "t"})
    assert "SHEET_ENDPOINT" in str(caught.value)
    assert "secret.test" not in str(caught.value)
    assert caught.value.__cause__ is not None


def test_configuration_repr_hides_the_secret() -> None:
    config = load_sheet_configuration({"SHEET_ENDPOINT": URL, "TOKEN": "test-token"})
    assert "test-token" not in repr(config)


def test_system_clock_tells_a_moment_close_to_now() -> None:
    assert abs(datetime.now() - SystemClock().now()) < timedelta(seconds=5)
