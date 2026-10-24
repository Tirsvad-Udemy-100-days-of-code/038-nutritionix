"""@file dry_run_http_gateway.py
@brief An HTTP gateway that prints the request and sends nothing.
"""

import json
from collections.abc import Mapping
from typing import TextIO

from exercise_tracker import constants
from exercise_tracker.application.dto.http_response import HttpResponse


def _hide_secrets(headers: Mapping[str, str]) -> dict[str, str]:
    """@brief Replace the value of every secret header by the mask.

    @param headers The HTTP headers.
    @return A copy in which the secrets are hidden.
    """
    return {
        name: (
            constants.HIDDEN_SECRET
            if name.lower() in constants.SECRET_HEADER_NAMES
            else value
        )
        for name, value in headers.items()
    }


class DryRunHttpGateway:
    """@brief Shows what would be sent. Nothing leaves the computer."""

    def __init__(self, out: TextIO) -> None:
        """@brief Create the gateway.

        @param out The stream the request is printed to.
        """
        self._out = out

    def post_json(
        self, url: str, headers: Mapping[str, str], body: Mapping[str, object]
    ) -> HttpResponse:
        """@brief Print the request with the secrets hidden.

        @param url The full URL.
        @param headers The HTTP headers.
        @param body The JSON body.
        @return A successful response with the dry-run sample body.
        """
        self._out.write(f"{constants.HTTP_METHOD_POST} {url}\n")
        for name, value in _hide_secrets(headers).items():
            self._out.write(f"{name}: {value}\n")
        self._out.write(json.dumps(body, indent=2) + "\n")
        sample: dict[str, object] = json.loads(constants.DRY_RUN_SAMPLE_BODY_JSON)
        return HttpResponse(constants.HTTP_STATUS_OK, sample)
