"""
Game instance.

:Author:     Maded Batara III
:Version:    v20181024
"""

from .game_board import GameBoard
from .helpers import *

class Game:

    def __init__(self, query, *, retries=None):
        self.board = GameBoard(query)
        self.mode = mode
        self.current_score = 0
        self.maximum_score = sum(score(word) for word in self.board)
        self.retries = retries
        self._is_game_over = False

    @property
    def is_game_over(self):
        return self._is_game_over

    @is_game_over.setter
    def is_game_over(self, value):
        if not isinstance(value, bool):
            raise TypeError("is_game_over should be of class bool")
        if not self._is_game_over:
            self._is_game_over = value
        else:
            raise ValueError("game is already on game over")

    def answer(self, term):
        if not self.is_game_over() and not self.board.fill(term) and self.retries is not None:
            self.retries -= 1
            self.current_score += score(term)
        if self.retries == 0:
            self.is_active = True
