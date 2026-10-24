"""@file gateway_unreachable_error.py
@brief The error raised when a server cannot be reached.
"""


class GatewayUnreachableError(Exception):
    """@brief The request could not be sent or no answer arrived in time."""
