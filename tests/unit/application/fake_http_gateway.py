"""@file fake_http_gateway.py
@brief A fake of the HttpGateway port that records requests.
"""

from collections.abc import Mapping

from exercise_tracker.application.dto.http_response import HttpResponse


class FakeHttpGateway:
    """@brief Answers with a canned response and records every request."""

    def __init__(self, response: HttpResponse) -> None:
        """@brief Create the fake.

        @param response The answer returned for every request.
        """
        self._response = response
        ## @brief The recorded requests as (url, headers, body).
        self.requests: list[tuple[str, dict[str, str], dict[str, object]]] = []

    def post_json(
        self, url: str, headers: Mapping[str, str], body: Mapping[str, object]
    ) -> HttpResponse:
        """@brief Record the request and return the canned answer.

        @param url The full URL.
        @param headers The HTTP headers.
        @param body The JSON body.
        @return The canned answer.
        """
        self.requests.append((url, dict(headers), dict(body)))
        return self._response
