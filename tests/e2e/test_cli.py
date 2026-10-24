"""@file test_cli.py
@brief End-to-end tests of the command line, offline.
"""

import io
import os
import subprocess
import sys
from collections.abc import Mapping

import pytest

from exercise_tracker.application.dto.http_response import HttpResponse
from exercise_tracker.constants import (
    EXIT_INVALID,
    EXIT_OK,
    EXIT_REJECTED,
    EXIT_UNREACHABLE,
    HIDDEN_SECRET,
)
from exercise_tracker.infrastructure.http.urllib_http_gateway import UrllibHttpGateway
from exercise_tracker.presentation.cli import main
from tests.integration.local_server import json_payload, serve

ENV = {"APP_ID": "test-app-id", "API_KEY": "test-api-key"}


def test_dry_run_prints_request_and_the_sample_exercise() -> None:
    out = io.StringIO()
    code = main(["--dry-run", "exercises", "ran 5k"], ENV, out)
    text = out.getvalue()
    assert code == EXIT_OK
    assert "POST https://trackapi.nutritionix.com/v2/natural/exercise" in text
    assert f"x-app-key: {HIDDEN_SECRET}" in text
    assert "test-app-id" not in text
    assert "test-api-key" not in text
    assert text.rstrip().endswith("Running: 30 min, 300 kcal")


def test_blank_sentence_is_invalid(capsys: pytest.CaptureFixture[str]) -> None:
    out = io.StringIO()
    assert main(["--dry-run", "exercises", "  "], ENV, out) == EXIT_INVALID
    assert out.getvalue() == ""
    assert "blank" in capsys.readouterr().err


def test_missing_variable_is_invalid_and_shows_no_value(
    capsys: pytest.CaptureFixture[str],
) -> None:
    code = main(
        ["--dry-run", "exercises", "x"], {"APP_ID": "test-app-id"}, io.StringIO()
    )
    err = capsys.readouterr().err
    assert code == EXIT_INVALID
    assert "API_KEY" in err
    assert "test-app-id" not in err


def test_unreachable_server_gives_unreachable_code(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(
        "exercise_tracker.presentation.cli.UrllibHttpGateway",
        lambda: _GatewayTo("http://127.0.0.1:9/"),
    )
    code = main(["exercises", "x"], ENV, io.StringIO())
    assert code == EXIT_UNREACHABLE
    assert "test-api-key" not in capsys.readouterr().err


def test_api_refusal_gives_rejected_code(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    with serve(401, json_payload({"message": "bad key"})) as server:
        monkeypatch.setattr(
            "exercise_tracker.presentation.cli.UrllibHttpGateway",
            lambda: _GatewayTo(server.url),
        )
        code = main(["exercises", "x"], ENV, io.StringIO())
    assert code == EXIT_REJECTED
    assert "401" in capsys.readouterr().err


def test_malformed_answer_gives_rejected_code(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    with serve(200, json_payload({"nothing": 1})) as server:
        monkeypatch.setattr(
            "exercise_tracker.presentation.cli.UrllibHttpGateway",
            lambda: _GatewayTo(server.url),
        )
        assert main(["exercises", "x"], ENV, io.StringIO()) == EXIT_REJECTED


class _GatewayTo:
    """@brief Real urllib gateway that redirects every request to a local URL."""

    def __init__(self, url: str) -> None:
        """@brief Create the gateway.

        @param url The local URL that replaces the requested one.
        """
        self._url = url
        self._inner = UrllibHttpGateway(timeout=2)

    def post_json(
        self, url: str, headers: Mapping[str, str], body: Mapping[str, object]
    ) -> HttpResponse:
        """@brief Send the request to the local URL.

        @param url Ignored.
        @param headers The HTTP headers.
        @param body The JSON body.
        @return The answer of the local server.
        """
        return self._inner.post_json(self._url, headers, body)


def test_module_runs_in_a_subprocess_with_dry_run() -> None:
    env = {**os.environ, **ENV, "PYTHONPATH": "src"}
    result = subprocess.run(
        [sys.executable, "-m", "exercise_tracker", "--dry-run", "exercises", "ran 5k"],
        capture_output=True,
        text=True,
        env=env,
        timeout=30,
        check=False,
    )
    assert result.returncode == EXIT_OK
    assert "Running: 30 min, 300 kcal" in result.stdout
    assert "test-api-key" not in result.stdout + result.stderr
