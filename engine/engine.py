"""
SWUG Game Engine

:Author:     Jose Enrico Salinas
:Version:    v20181020
"""


from .game_board import GameBoard
from .dictionary import Dictionary
from .game_modes import GameModes

class Engine:

    def __init__(self, dictionary):
        self.dictionary = Dictionary(dictionary)
        self.game_board = None
        self.game_mode = None
        self.game_restrictions = None
        self.time = 0
        self.retries = 0

    def set_game_mode(self, game_mode):
        if game_mode == GameModes.anagrams:
            self.game_mode = game_mode
            self.game_board = GameBoard(self.dictionary.choice(), self.dictionary)
        elif game_mode == GameModes.random:
            self.game_mode = game_mode
            self.game_board = GameBoard(self.dictionary.filter_from_random_string(), self.dictionary)
        else:
            raise ValueError

    def set_game_restrictions(self, game_restrictions):
        if game_restrictions == GameModes.timed or game_restrictions == GameModes.timed_retries:
            self.game_restrictions = game_restrictions
            self.time = 120000      #max game time in milliseconds
        if game_restrictions == GameModes.retries or game_restrictions == GameModes.timed_retries:
            self.game_restrictions = game_restrictions
            self.retries = 3

    def answer(self, term):
        correct = self.game_board.answer(term)
        if (self.game_restrictions == GameModes.retries or self.game_restrictions == GameModes.timed_retries) and not correct:
            self.retries -= 1 
        return correct