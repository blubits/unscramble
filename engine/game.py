"""
Game instance.

:Author:     Maded Batara III
:Version:    v20181024
"""

from .game_board import GameBoard
from .helpers import scrabble_score

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

    def __init__(self, word, query, *, mistakes=None, score=scrabble_score):
        """
        Initializes a new Game.

        Args:
            word (str): Word to form the board from. Note that it is
                not guaranteed that this matches the query; the
                controller is responsible for making sure it matches.
            query (DictionaryQuery): A list of words queried from the
                dictionary.
            mistakes (int, optional): Number of mistakes (i.e. wrong answers)
                before the game hits Game Over. If equal to None, the game
                operates on unlimited retries.
            score (function: str -> int, optional): Function that determines
                the point value of a certain word.
        """
        self.word = word
        self.board = GameBoard(query)
        # score
        self.score_function = score
        self.current_score = 0
        self.maximum_score = sum(score(word) for word in self.board)
        # retries
        self.current_mistakes = 0
        self.maximum_mistakes = mistakes
        # game over
        self.is_game_over = False

    @property
    def mistakes(self):
        """tuple: A pair describing the current and maximum amount of mistakes made."""
        return (self.current_mistakes, self.maximum_mistakes)

    @property
    def score(self):
        """tuple: A pair describing the current and maximum points made."""
        return (self.current_score, self.maximum_score)

    def answer(self, term):
        """
        Answers an item on the board.

        Args:
            term (str): Word to attempt to fill up on the board.

        Returns:
            bool: True if the word is on the board, False otherwise.
        """
        if self.is_game_over:
            return False
        if self.board.fill(term):
            self.current_score += self.score_function(term)
            if self.is_won():
                self.end_game()
            return True
        else:
            if self.maximum_mistakes is not None:
                self.current_mistakes += 1
                if self.current_mistakes == self.maximum_mistakes:
                    self.end_game()
                return False

    def end_game(self):
        """
        End the game.
        """
        if self.is_game_over:
            raise RuntimeError("Game has already ended")
        self.is_game_over = True

    def is_won(self):
        """
        Checks if the game is in a win condition, i.e. everything in the board
        is filled up.
        """
        return self.board.is_complete()

    def on_board(self, term):
        """
        Checks if a word is already on the board.

        Args:
            term (str): Word to check on the board.

        Returns:
            bool: True if the word is on the board, False otherwise.
        """
        return self.board.is_filled(term)

    def words_by_length(self):
        """
        Returns a dictionary view of all words in the board, sorted by length.

        Returns:
            dict: A dictionary of all words in the board, grouped
                by length of the word. Words are sorted alphabetically
                within the list.
        """
        return self.board.words_by_length()

    def words_by_length_filled(self):
        """
        Returns a dictionary view of all filled-up words in the board,
        sorted by length.

        Returns:
            dict: A dictionary of all words in the board, grouped
                by length of the word. Words are sorted alphabetically
                within the list. All words not filled up are replaced
                with None.
        """
        return self.board.words_by_length_filled()
