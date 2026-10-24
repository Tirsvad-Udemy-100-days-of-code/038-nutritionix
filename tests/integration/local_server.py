"""@file local_server.py
@brief A local HTTP server on 127.0.0.1 for the integration tests.
"""

import json
import threading
from collections.abc import Iterator
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

LOCAL_HOST = "127.0.0.1"


class RecordedRequest:
    """@brief What the server received."""

    def __init__(self, method: str, path: str, headers: dict[str, str], body: bytes):
        """@brief Create the record.

        @param method The HTTP method.
        @param path The request path.
        @param headers The request headers, names in lower case.
        @param body The raw body.
        """
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body


class LocalServer:
    """@brief Handle of a running server: its address and what it saw."""

    def __init__(self, status: int, payload: bytes) -> None:
        """@brief Create the handle.

        @param status The status code to answer with.
        @param payload The raw body to answer with.
        """
        self.status = status
        self.payload = payload
        self.requests: list[RecordedRequest] = []
        self.port = 0

    @property
    def url(self) -> str:
        """@brief The URL of the server.

        @return The base URL with the ephemeral port.
        """
        return f"http://{LOCAL_HOST}:{self.port}/v2/natural/exercise"


@contextmanager
def serve(status: int = 200, payload: bytes = b"{}") -> Iterator[LocalServer]:
    """@brief Run a local server on an ephemeral port.

    @param status The status code to answer with.
    @param payload The raw body to answer with.
    @return A context that yields the server handle.
    """
    state = LocalServer(status, payload)

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:  # noqa: N802 - name fixed by http.server
            length = int(self.headers.get("Content-Length", "0"))
            state.requests.append(
                RecordedRequest(
                    "POST",
                    self.path,
                    {k.lower(): v for k, v in self.headers.items()},
                    self.rfile.read(length),
                )
            )
            self.send_response(state.status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(state.payload)))
            self.end_headers()
            self.wfile.write(state.payload)

        def log_message(self, format: str, *args: object) -> None:  # noqa: A002
            return

    server = ThreadingHTTPServer((LOCAL_HOST, 0), Handler)
    state.port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield state
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def json_payload(value: object) -> bytes:
    """@brief Encode a value as JSON bytes.

    @param value The value.
    @return The JSON bytes.
    """
    return json.dumps(value).encode("utf-8")
