"""
Controller class for SWUG

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

from engine.dictionary import Dictionary
from engine.game_board import GameBoard
from views.interface_modes import InterfaceModes
from views.terminal.terminal_basic import BasicTerminalInterface


class Game:

    def __init__(self, interface, dictionary):
        self.dictionary = Dictionary(dictionary)
        self.interface_mode = interface
        self.game_board = GameBoard(self.dictionary.choice(), self.dictionary)

        if self.interface_mode == InterfaceModes.terminal_basic:
            # TODO: Implement basic terminal interface
            self.interface = BasicTerminalInterface(
                self.dictionary, self.game_board)
            pass
        elif self.interface_mode == InterfaceModes.terminal_advanced:
            # TODO: Implement advanced terminal interface
            pass
        elif self.interface_mode == InterfaceModes.desktop:
            # TODO: Implement desktop interface
            pass
        else:
            raise ValueError

    def run(self):
        self.interface.run()
