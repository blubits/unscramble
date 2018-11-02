"""
A game board (i.e. list of words).

:Author:     Maded Batara III
:Author:     Jose Enrico Salinas
:Version:    v20181024
"""

from math import ceil

class GameBoard:

    def __init__(self, query):
        """
        Initializes a new game board.

        Args:
            query (DictionaryQuery): A list of words queried from the
                dictionary.
        """
        self.query = query
        self.columns = 7
        self.board = {}
        for word in self.query:
            self.board[word] = False

    def __iter__(self):
        return iter(self.query)

    def __len__(self):
        return len(self.query)

    def __str__(self):
        words_per_column = ceil(len(self.query) / self.columns)
        board = [[] for _ in range(self.columns)]
        col = 0
        for _, words in sorted(self.query.group_by_length().items()):
            for word in words:
                if self.board[word]:
                    w = word
                else:
                    w = "_" * len(word)
                board[col].append(w.ljust(15))
                if len(board[col]) == words_per_column:
                    col += 1
        return '\n'.join(
            [' '.join(row[i] if len(row) > i else '' for row in board)
             for i in range(words_per_column)]
        )

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
            return True
        return False

    def is_complete(self):
        """
        Checks if a board is completely filled up.format

        Returns:
            bool: True if board is filled up, False otherwise.
        """
        for word in self.board.values():
            if not word:
                return False
        return True
