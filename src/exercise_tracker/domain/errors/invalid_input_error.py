"""@file invalid_input_error.py
@brief The error raised when a value breaks a domain rule.
"""


class InvalidInputError(ValueError):
    """@brief A value does not follow a rule of the domain.

    It is raised before any request is sent.
    """
