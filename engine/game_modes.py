"""
An enumeration of game modes

:Author:     Jose Enrico Salinas
:Version:    v20181102
"""

from enum import Enum

class GameModes(Enum):
    anagrams = 0
    random = 1

class GameRestrictions(Enum):
    vanilla = 0
    retries = 1
    timed = 2
    timed_retries = 3