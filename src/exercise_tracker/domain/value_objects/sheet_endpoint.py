"""@file sheet_endpoint.py
@brief The URL of the Sheety endpoint.
"""

from dataclasses import dataclass

from exercise_tracker.domain.errors.invalid_input_error import InvalidInputError

## @brief The URL schemes an endpoint may use.
_ALLOWED_SCHEMES = ("http://", "https://")


@dataclass(frozen=True, slots=True)
class SheetEndpoint:
    """@brief A non-blank http or https URL; stored stripped."""

    ## @brief The URL, without leading or trailing white space.
    url: str

    def __post_init__(self) -> None:
        """@brief Strip the URL and check its scheme.

        @throws InvalidInputError The URL is blank or not http or https.
        """
        stripped = self.url.strip()
        if not stripped:
            raise InvalidInputError("The sheet endpoint must not be blank.")
        if not stripped.lower().startswith(_ALLOWED_SCHEMES):
            raise InvalidInputError(
                "The sheet endpoint must start with http:// or https://."
            )
        object.__setattr__(self, "url", stripped)
