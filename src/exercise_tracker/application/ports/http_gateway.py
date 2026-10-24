"""@file http_gateway.py
@brief The port through which the use cases send JSON over HTTP.
"""

from collections.abc import Mapping
from typing import Protocol

from exercise_tracker.application.dto.http_response import HttpResponse


class HttpGateway(Protocol):
    """@brief Sends one JSON POST request."""

    def post_json(
        self, url: str, headers: Mapping[str, str], body: Mapping[str, object]
    ) -> HttpResponse:
        """@brief Send a POST request with a JSON body.

        An error status of the server is returned, not raised.

        @param url The full URL.
        @param headers The HTTP headers.
        @param body The JSON body.
        @return The answer of the server.
        @throws GatewayUnreachableError The server could not be reached.
        """
        ...
