"""@file system_clock.py
@brief The clock of the computer.
"""

from datetime import datetime


class SystemClock:
    """@brief Tells the local date and time of the computer."""

    def now(self) -> datetime:
        """@brief Read the current local date and time.

        @return The current moment.
        """
        return datetime.now()  # noqa: DTZ005 - the sheet holds local wall-clock time
