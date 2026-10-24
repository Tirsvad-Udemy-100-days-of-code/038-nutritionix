"""@file test_environment_credentials.py
@brief Unit tests of the environment configuration.
"""

import pytest

from exercise_tracker.infrastructure.config.configuration_error import (
    ConfigurationError,
)
from exercise_tracker.infrastructure.config.environment_credentials import (
    load_nutritionix_credentials,
)


def test_reads_both_values_from_the_environment() -> None:
    credentials = load_nutritionix_credentials(
        {"APP_ID": "test-app-id", "API_KEY": "test-api-key"}
    )
    assert (credentials.app_id, credentials.api_key) == ("test-app-id", "test-api-key")


@pytest.mark.parametrize(
    ("environ", "missing"),
    [
        ({"API_KEY": "test-api-key"}, "APP_ID"),
        ({"APP_ID": "test-app-id"}, "API_KEY"),
        ({"APP_ID": "  ", "API_KEY": "test-api-key"}, "APP_ID"),
        ({"APP_ID": "test-app-id", "API_KEY": ""}, "API_KEY"),
    ],
)
def test_missing_or_blank_variable_is_named_without_values(
    environ: dict[str, str], missing: str
) -> None:
    with pytest.raises(ConfigurationError) as caught:
        load_nutritionix_credentials(environ)
    message = str(caught.value)
    assert missing in message
    assert "test-app-id" not in message
    assert "test-api-key" not in message
