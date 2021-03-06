"""
A game board (i.e. list of words).

:Author:     Maded Batara III
:Author:     Jose Enrico Salinas
:Version:    v20181104
"""

from collections import OrderedDict
from math import ceil

class GameBoard:
    """A board with a list of words to fill up."""

    def __init__(self, query):
        """
        Initializes a new game board.

        Args:
            query (DictionaryQuery): A list of words queried from the
                dictionary.
        """
        self.query = query
        self.num_words = len(self.query)
        self.filled_up_words = 0
        self.columns = 7
        self.board = {}
        for word in self.query:
            self.board[word] = False

    def __iter__(self):
        """Implements iter(gameboard)."""
        return iter(self.query)

    def __len__(self):
        """Implements len(GameBoard)."""
        return self.num_words

    def __str__(self):
        """Implements str(GameBoard)."""
        return "GameBoard, {0}/{1} filled up".format(
            self.filled_up_words, len(self))

    def fill(self, word):
        """
        Fills a word on the board.

        Args:
            word (str): Word to put on the board.

        Returns:
            bool: True if the word is on the board, False otherwise.
        """
        if word in self.query:
            self.board[word] = True
            self.filled_up_words += 1
            return True
        return False

    def is_filled(self, word):
        """
        Checks if a word is already filled up on the board.

        Args:
            word (str): Word to check on the board.

        Returns:
            bool: True if the word is on the board, False otherwise.
        """
        if word in self.query:
            return self.board[word]
        return False

    def is_complete(self):
        """
        Checks if a board is completely filled up.format

        Returns:
            bool: True if board is filled up, False otherwise.
        """
        return self.filled_up_words == self.num_words

    def words_by_length(self):
        """
        Returns a dictionary view of all words in the board, sorted by length.
        Equivalent to calling self.query.group_by_length().

        Returns:
            dict: A dictionary of all words in the board, grouped
                by length of the word. Words are sorted alphabetically
                within the list.
        """
        return self.query.group_by_length()

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
        g = OrderedDict()
        for length, words in sorted(self.words_by_length().items()):
            g[length] = words[:]
            for i in range(len(g[length])):
                if not self.is_filled(g[length][i]):
                    g[length][i] = None
        return dict(g)
