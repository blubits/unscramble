"""
An enumeration of game modes

:Author:     Jose Enrico Salinas
:Version:    v20181020
"""

from enum import Enum

class GameModes(Enum):
    anagrams = "ENGINE.MODES.ANAGRAMS"
    random = "ENGINE.MODES.RANDOM"

    retries = "ENGINE.RESTRICTIONS.RETRIES"
    timed = "ENGINE.RESTRICTIONS.TIMED"
    timed_retries = "ENGINE.RESTRICTIONS.TIMEDRETRIES"