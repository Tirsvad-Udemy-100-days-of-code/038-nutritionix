"""@file configuration_error.py
@brief The error raised when the configuration is incomplete.
"""


class ConfigurationError(Exception):
    """@brief A required setting is missing; the message never shows a value."""
