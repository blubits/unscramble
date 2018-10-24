"""
Helper functions and constants for the game engine.

:Author:     Maded Batara III
:Version:    v20181024
"""

from enum import Enum

LETTER_POINTS = {
    'e': 1,
    'a': 1,
    'i': 1,
    'o': 1,
    'n': 1,
    'r': 1,
    't': 1,
    'l': 1,
    's': 1,
    'u': 1,
    'd': 2,
    'g': 2,
    'b': 3,
    'c': 3,
    'm': 3,
    'p': 3,
    'f': 4,
    'h': 4,
    'v': 4,
    'w': 4,
    'y': 4,
    'k': 5,
    'j': 8,
    'x': 8,
    'q': 10,
    'z': 10
}

class GameModes(Enum):
    ALL_WORDS = 0
    ANAGRAMS = 1

class GameRestrictions(Enum):
    THREE_TRIES = 0
    TIMED = 1

def score(word):
    """
    Scores a word using Scrabble point values.
    """
    return sum(LETTER_POINTS.get(l, 0) for l in word.lower())
