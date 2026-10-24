"""@file test_constants.py
@brief Unit tests of the constants module.
"""

from datetime import datetime

from exercise_tracker import constants


def test_nutritionix_url_is_the_natural_exercise_endpoint() -> None:
    assert constants.NUTRITIONIX_EXERCISE_URL.endswith("/v1/nutrition/natural/exercise")


def test_environment_names_follow_the_assignment() -> None:
    assert {
        constants.ENV_APP_ID,
        constants.ENV_API_KEY,
        constants.ENV_SHEET_ENDPOINT,
        constants.ENV_USERNAME,
        constants.ENV_PASSWORD,
        constants.ENV_TOKEN,
    } == {"APP_ID", "API_KEY", "SHEET_ENDPOINT", "USERNAME", "PASSWORD", "TOKEN"}


def test_date_and_time_formats_match_the_sheet_columns() -> None:
    moment = datetime(2026, 10, 24, 9, 5, 7)
    assert moment.strftime(constants.DATE_FORMAT) == "24/10/2026"
    assert moment.strftime(constants.TIME_FORMAT) == "09:05:07"


def test_sheet_row_is_wrapped_in_a_camel_case_singular_name() -> None:
    assert constants.FIELD_WORKOUT == "workout"
