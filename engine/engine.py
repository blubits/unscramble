from .game_board import GameBoard
from .dictionary import Dictionary

class Engine:

    def __init__(self, dictionary):
        self.dictionary = Dictionary(dictionary)
        self.game_board = GameBoard(self.dictionary.choice(), self.dictionary)