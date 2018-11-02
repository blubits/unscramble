"""
Controller class for SWUG

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

from engine.game import Game

from views.interface_modes import InterfaceModes
from views.terminal_basic import BasicTerminalInterface
from views.desktop import DesktopInterface


class Controller:

    def __init__(self, interface, dictionary):
        self.game = Game(dictionary)
        self.interface_mode = interface

        if self.interface_mode == InterfaceModes.terminal:
            self.interface = BasicTerminalInterface(self.game)
        elif self.interface_mode == InterfaceModes.desktop:
            self.interface = DesktopInterface(self.game)
        else:
            raise ValueError

    def run(self):
        self.interface.run()
