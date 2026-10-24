"""@file clock.py
@brief The port through which the use cases ask for the current time.
"""

from datetime import datetime
from typing import Protocol


class Clock(Protocol):
    """@brief Tells the current date and time."""

    def now(self) -> datetime:
        """@brief Read the current date and time.

        @return The current moment.
        """
        ...
