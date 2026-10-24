"""@file fixed_clock.py
@brief A fake of the Clock port that always tells the same moment.
"""

from datetime import datetime

## @brief The moment every FixedClock tells: 5 March 2026, 07:08:09.
FIXED_MOMENT = datetime(2026, 3, 5, 7, 8, 9)


class FixedClock:
    """@brief Tells a fixed moment and counts how often it was asked."""

    def __init__(self, moment: datetime = FIXED_MOMENT) -> None:
        """@brief Create the clock.

        @param moment The moment to tell.
        """
        self._moment = moment
        ## @brief How many times `now` was called.
        self.calls = 0

    def now(self) -> datetime:
        """@brief Return the fixed moment.

        @return The moment given to the constructor.
        """
        self.calls += 1
        return self._moment
