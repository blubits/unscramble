"""
An enumeration of game modes.

:Author:     Maded Batara III
:Author:     Jose Enrico Salinas
:Version:    v20181104
"""

from enum import Enum

class GameMode(Enum):
    UNTIMED = 0
    RETRIES = 1
    TIMED = 2
    TIMED_RETRIES = 3
