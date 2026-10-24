"""@file json_body.py
@brief Decoding of a JSON answer body.
"""

import json


def decode_json_object(raw: bytes) -> dict[str, object]:
    """@brief Decode bytes into a JSON object.

    @param raw The body as received.
    @return The JSON object; empty when the body is not a JSON object.
    """
    try:
        decoded = json.loads(raw)
    except ValueError:
        return {}
    if isinstance(decoded, dict):
        return decoded
    return {}
