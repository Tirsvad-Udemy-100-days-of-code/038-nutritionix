"""@file malformed_response_error.py
@brief The error raised when an answer does not have the expected shape.
"""


class MalformedResponseError(Exception):
    """@brief An API answered successfully but the body cannot be understood."""
