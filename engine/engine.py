"""
SWUG Game Engine

:Author:     Jose Enrico Salinas
:Version:    v20181020
"""


from .game_board import GameBoard
from .dictionary import Dictionary
from .game_modes import GameModes
from .timer import GameTimer

class Engine:

    def __init__(self, dictionary):
        self.dictionary = Dictionary(dictionary)
        self.game_board = None
        self.game_mode = None
        self.game_restrictions = None
        self.time = None
        self.retries = None
        self.dead = False
        self.timer = None

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
            self.time = 60      #max game time in seconds
            self.retries = 3
        elif game_restrictions == GameModes.timed:
            self.time = 60      #max game time in seconds
        elif game_restrictions == GameModes.retries:
            self.retries = 3
        else:
            raise ValueError
        self.game_restrictions = game_restrictions

    def answer(self, term):
        correct = self.game_board.answer(term)
        if (self.game_restrictions == GameModes.retries or self.game_restrictions == GameModes.timed_retries) and not correct:
            self.retries -= 1
        if self.retries == 0:
            self.set_dead(True)
        return correct

    def is_complete(self):
        return self.game_board.is_complete()

    def set_dead(self, dead):
        self.dead = dead

    def toggle_dead(self):
        self.dead = not self.dead

    def is_dead(self):
        return self.dead

    def time_remaining(self):
        if self.game_restrictions == GameModes.timed or self.game_restrictions == GameModes.timed_retries:
            return self.timer.remaining()
        else:
            return None

    def start(self):
        if self.game_restrictions == GameModes.timed or self.game_restrictions == GameModes.timed_retries:
            if self.is_dead():
                raise RuntimeError("Tried to start dead game engine.")
            self.timer = GameTimer(self.time, self.toggle_dead)
            self.timer.start()

    def reset(self):
        self.game_board = None
        self.game_mode = None
        self.game_restrictions = None
        self.time = None
        self.retries = None
        self.dead = False
        self.timer = None