"""
Game instance.

:Author:     Maded Batara III
:Version:    v20181024
"""

from .game_board import GameBoard
from .helpers import *

class Game:
    """An instance of the Simple Word Unscrambler Game.

    The Game class is meant to be a 'shell' for any game interface to
    instantiate and manipulate if necessary. As such, it does not
    change its own state unless a word is filled up or the maximum
    number of retries have been reached.

    Attributes:
        current_score (int): Current score achieved by the player.
        maximum_score (int): Maximum score achievable by a player.
    """

    def __init__(self, word, query, *, retries=None):
        """
        Initializes a new Game.

        Args:
            word (str): Word to form the board from. Note that it is
                not guaranteed that this matches the query; the
                controller is responsible for making sure it matches.
            query (DictionaryQuery): A list of words queried from the
                dictionary.
            retries (int, optional): Number of retries (i.e. wrong answers)
                before the game hits Game Over.
        """
        self.word = word
        self.board = GameBoard(query)
        self.current_score = 0
        self.maximum_score = sum(score(word) for word in self.board)
        self.retries = retries
        self._is_game_over = False

    @property
    def is_game_over(self):
        """bool: True if the game is over, False otherwise."""
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
        """
        Answers an item on the board.

        Args:
            term (str): Word to attempt to fill up on the board.

        Returns:
            bool: True if the word is on the board, False otherwise.
        """
        if not self.is_game_over and not self.board.fill(term) and self.retries is not None:
            self.retries -= 1
            self.current_score += score(term)
            return True
        if self.retries == 0:
            self.is_game_over = True
        return False
