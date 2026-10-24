"""@file exercise_query.py
@brief The plain English sentence that describes the exercises done.
"""

from dataclasses import dataclass

from exercise_tracker.domain.errors.invalid_input_error import InvalidInputError


@dataclass(frozen=True, slots=True)
class ExerciseQuery:
    """@brief A non-blank sentence such as `ran 3 miles`; stored stripped."""

    ## @brief The sentence, without leading or trailing white space.
    text: str

    def __post_init__(self) -> None:
        """@brief Strip the text and check that something is left.

        @throws InvalidInputError The text is blank.
        """
        stripped = self.text.strip()
        if not stripped:
            raise InvalidInputError("The exercise query must not be blank.")
        object.__setattr__(self, "text", stripped)
