"""@file error_message.py
@brief Takes the short message of an API error answer.
"""

from exercise_tracker import constants
from exercise_tracker.application.dto.http_response import HttpResponse


def short_message(response: HttpResponse) -> str:
    """@brief Take the short message of an error answer.

    @param response The error answer.
    @return The message of the API, shortened; or a generic text.
    """
    message = response.body.get(constants.FIELD_MESSAGE)
    if isinstance(message, str) and message.strip():
        return message.strip()[: constants.MAX_API_MESSAGE_LENGTH]
    return "no message"
