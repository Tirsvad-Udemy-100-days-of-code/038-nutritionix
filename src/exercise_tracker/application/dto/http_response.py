"""@file http_response.py
@brief The answer of an HTTP server as plain data.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HttpResponse:
    """@brief The status code and the decoded JSON body of an answer."""

    ## @brief The HTTP status code.
    status_code: int

    ## @brief The decoded JSON object; empty when the body was not JSON.
    body: dict[str, object]
