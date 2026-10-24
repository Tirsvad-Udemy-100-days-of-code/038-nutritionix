"""@file error_message.py
@brief Takes the short message of an API error answer.
"""

from exercise_tracker import constants
from exercise_tracker.application.dto.http_response import HttpResponse


def _text_of(value: object) -> str | None:
    """@brief Return the stripped text of a non-blank string, else None."""
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def short_message(response: HttpResponse) -> str:
    """@brief Take the short message of an error answer.

    The message is the top-level `message`, else the `message` inside the
    `error` object.

    @param response The error answer.
    @return The message of the API, shortened; or a generic text.
    """
    message = _text_of(response.body.get(constants.FIELD_MESSAGE))
    if message is None:
        error = response.body.get(constants.FIELD_ERROR)
        if isinstance(error, dict):
            message = _text_of(error.get(constants.FIELD_MESSAGE))
    if message is None:
        return "no message"
    return message[: constants.MAX_API_MESSAGE_LENGTH]
