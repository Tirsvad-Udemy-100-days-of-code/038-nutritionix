"""@file urllib_http_gateway.py
@brief An HTTP gateway built on the standard library `urllib`.
"""

import json
import logging
import urllib.error
import urllib.request
from collections.abc import Mapping

from exercise_tracker import constants
from exercise_tracker.application.dto.http_response import HttpResponse
from exercise_tracker.application.errors.gateway_unreachable_error import (
    GatewayUnreachableError,
)
from exercise_tracker.infrastructure.http.json_body import decode_json_object

_LOGGER = logging.getLogger(__name__)


def _with_user_agent(headers: Mapping[str, str]) -> dict[str, str]:
    """@brief Copy the headers and add the User-Agent unless the caller set one.

    The header name is compared without regard to case.

    @param headers The headers of the caller.
    @return The headers to send.
    """
    result = dict(headers)
    wanted = constants.HEADER_USER_AGENT.lower()
    if not any(name.lower() == wanted for name in result):
        result[constants.HEADER_USER_AGENT] = constants.USER_AGENT
    return result


class UrllibHttpGateway:
    """@brief Sends JSON POST requests with `urllib.request`."""

    def __init__(self, timeout: float = constants.REQUEST_TIMEOUT_SECONDS) -> None:
        """@brief Create the gateway.

        @param timeout Seconds to wait for the server.
        """
        self._timeout = timeout

    def post_json(
        self, url: str, headers: Mapping[str, str], body: Mapping[str, object]
    ) -> HttpResponse:
        """@brief Send a POST request with a JSON body.

        An error status (4xx, 5xx) is returned as a response, not raised.

        @param url The full URL.
        @param headers The HTTP headers.
        @param body The JSON body.
        @return The answer of the server.
        @throws GatewayUnreachableError The server could not be reached.
        """
        request = urllib.request.Request(
            url,
            data=json.dumps(body).encode("utf-8"),
            headers=_with_user_agent(headers),
            method=constants.HTTP_METHOD_POST,
        )
        try:
            with urllib.request.urlopen(request, timeout=self._timeout) as answer:
                return HttpResponse(answer.status, decode_json_object(answer.read()))
        except urllib.error.HTTPError as error:
            with error:
                return HttpResponse(error.code, decode_json_object(error.read()))
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            _LOGGER.warning("Request to %s failed: %s", url, type(error).__name__)
            raise GatewayUnreachableError(
                f"Could not reach the server: {type(error).__name__}"
            ) from error
