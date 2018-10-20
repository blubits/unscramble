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

    def __str__(self):
        return self.game_board.__str__()

    def set_game_mode(self, game_mode):
        if game_mode == GameModes.anagrams:
            self.game_board = GameBoard(self.dictionary.choice(), self.dictionary)
        elif game_mode == GameModes.random:
            self.game_board = GameBoard(self.dictionary.random_string(), self.dictionary)
        else:
            raise ValueError
        self.game_mode = game_mode

    def set_game_restrictions(self, game_restrictions):
        if  game_restrictions == GameModes.vanilla:
            pass
        elif game_restrictions == GameModes.timed_retries:
            self.time = 120000      #max game time in milliseconds
            self.retries = 3
        elif game_restrictions == GameModes.timed:
            self.time = 120000      #max game time in milliseconds
        elif game_restrictions == GameModes.retries:
            self.retries = 3
        else:
            raise ValueError
        self.game_restrictions = game_restrictions

    def answer(self, term):
        correct = self.game_board.answer(term)
        if (self.game_restrictions == GameModes.retries or self.game_restrictions == GameModes.timed_retries) and not correct:
            self.retries -= 1 
        return correct

    def is_complete(self):
        return self.game_board.is_complete()

    def is_dead(self)
        if self.retries = 0:
            return True
        return False

    def reset(self):
        self.game_board = None
        self.game_mode = None
        self.game_restrictions = None
        self.time = 0
        self.retries = 0