"""@file sheet_authorization.py
@brief The value of the Authorization header of the Sheety requests.
"""

import base64
from dataclasses import dataclass, field

from exercise_tracker import constants
from exercise_tracker.domain.errors.invalid_input_error import InvalidInputError


@dataclass(frozen=True, slots=True)
class SheetAuthorization:
    """@brief A bearer or basic authorization value.

    The value never appears in `repr` or `str`.
    """

    ## @brief The complete header value, for example `Bearer abc`.
    header_value: str = field(repr=False)

    @classmethod
    def bearer(cls, token: str) -> "SheetAuthorization":
        """@brief Build a bearer authorization.

        @param token The bearer token.
        @return The authorization.
        @throws InvalidInputError The token is blank.
        """
        if not token.strip():
            raise InvalidInputError("The token must not be blank.")
        return cls(f"{constants.BEARER_PREFIX} {token}")

    @classmethod
    def basic(cls, username: str, password: str) -> "SheetAuthorization":
        """@brief Build a basic authorization.

        @param username The user name.
        @param password The password.
        @return The authorization.
        @throws InvalidInputError The user name or the password is blank.
        """
        if not username.strip():
            raise InvalidInputError("The username must not be blank.")
        if not password.strip():
            raise InvalidInputError("The password must not be blank.")
        encoded = base64.b64encode(f"{username}:{password}".encode()).decode("ascii")
        return cls(f"{constants.BASIC_PREFIX} {encoded}")

    def __repr__(self) -> str:
        """@brief Show the class with the secret hidden.

        @return The masked text.
        """
        return f"SheetAuthorization({constants.HIDDEN_SECRET})"

    def __str__(self) -> str:
        """@brief Show the class with the secret hidden.

        @return The masked text.
        """
        return self.__repr__()
