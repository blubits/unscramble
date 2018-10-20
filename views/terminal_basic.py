"""
A basic terminal interface using stdin and stdout.

:Author:     Jose Enrico Salinas
:Version:    v20181020
"""

from .interface_handler import InterfaceHandler
from engine.game_modes import GameModes


class BasicTerminalInterface(InterfaceHandler):

    def __init__(self, engine):
        self.engine = engine
        self.engine.set_game_mode(GameModes.anagrams)
        self.game_board = engine.game_board

    def run(self):

        print(self.game_board)
        while not self.game_board.is_complete():
            answer = input("Guess a word: ")
            self.game_board.answer(answer)
            print(self.game_board)