"""@file test_http_helpers.py
@brief Unit tests of the dry-run gateway and the JSON body decoder.
"""

import io
import json

from exercise_tracker import constants
from exercise_tracker.infrastructure.http.dry_run_http_gateway import (
    DryRunHttpGateway,
)
from exercise_tracker.infrastructure.http.json_body import decode_json_object


def test_dry_run_prints_request_with_secrets_hidden() -> None:
    out = io.StringIO()
    DryRunHttpGateway(out).post_json(
        "https://example.test/x",
        {
            "x-app-id": "test-app-id",
            "X-App-Key": "test-api-key",
            "Authorization": "Bearer test-token",
            "Content-Type": "application/json",
        },
        {"query": "ran 5k"},
    )
    text = out.getvalue()
    assert text.startswith("POST https://example.test/x\n")
    assert f"x-app-id: {constants.HIDDEN_SECRET}" in text
    assert f"Authorization: {constants.HIDDEN_SECRET}" in text
    assert "Content-Type: application/json" in text
    assert '"query": "ran 5k"' in text
    for secret in ("test-app-id", "test-api-key", "test-token"):
        assert secret not in text


def test_dry_run_returns_the_sample_and_sends_nothing() -> None:
    response = DryRunHttpGateway(io.StringIO()).post_json("http://127.0.0.1:1", {}, {})
    assert response.status_code == 200
    assert response.body == json.loads(constants.DRY_RUN_SAMPLE_BODY_JSON)


def test_decode_returns_object() -> None:
    assert decode_json_object(b'{"a": 1}') == {"a": 1}


def test_decode_returns_empty_for_non_json_or_non_object() -> None:
    assert decode_json_object(b"<html>") == {}
    assert decode_json_object(b"[1, 2]") == {}
    assert decode_json_object(b"") == {}
