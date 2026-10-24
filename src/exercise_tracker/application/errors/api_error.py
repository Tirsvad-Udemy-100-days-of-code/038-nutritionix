"""@file api_error.py
@brief The error raised when an API answers with an error status.
"""


class ApiError(Exception):
    """@brief An API answered with an HTTP status of 400 or more."""

    def __init__(self, status_code: int, message: str) -> None:
        """@brief Create the error.

        @param status_code The HTTP status code.
        @param message A short message of the API; never a header or a secret.
        """
        super().__init__(f"The API answered HTTP {status_code}: {message}")
        ## @brief The HTTP status code.
        self.status_code = status_code
        ## @brief The short message of the API.
        self.message = message
