"""
A game board (i.e. list of words).

:Author:     Maded Batara III
:Author:     Jose Enrico Salinas
:Version:    v20181020
"""

from math import ceil

class GameBoard:

    def __init__(self, string, dictionary):
        self.string = string
        self.query = dictionary.filter_from_string(
            string).filter_by_length(3, len(string))
        self.board = {}
        for word in self.query:
            self.board[word] = False

    def __iter__(self):
        return iter(self.query)

    def __len__(self):
        return len(self.query)

    def __str__(self):
        columns = 7
        words_per_column = ceil(len(self.query) / columns)
        board = [[] for _ in range(columns)]
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
            ["String: {0}".format(self.string)] +
            [' '.join(row[i] if len(row) > i else '' for row in board)
             for i in range(words_per_column)]
        )

    def answer(self, word):
        if word in self.query:
            self.board[word] = True
            return True
        return False

    def is_complete(self):
        for word in self.board.values():
            if not word:
                return False
        return True