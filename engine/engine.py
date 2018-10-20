"""
SWUG Game Engine

:Author:     Jose Enrico Salinas
:Version:    v20181020
"""


from .game_board import GameBoard
from .dictionary import Dictionary

class Engine:

    def __init__(self, dictionary):
        self.dictionary = Dictionary(dictionary)
        self.game_board = GameBoard(self.dictionary.choice(), self.dictionary)