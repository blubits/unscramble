"""
Controller class that initializes game dictionary,
and interfaces

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

from engine.game import Game
from engine.dictionary import Dictionary

from views.interface_modes import InterfaceModes
from views.terminal import TerminalInterface
from views.desktop import DesktopInterface


class Controller:

    def __init__(self, interface, dictionary):
        self.interface_mode = interface
        self.game = Game(Dictionary(dictionary))

        if self.interface_mode == InterfaceModes.terminal:
            self.interface = TerminalInterface()
        elif self.interface_mode == InterfaceModes.desktop:
            self.interface = DesktopInterface()
        else:
            raise ValueError

    def run(self):
        self.interface.run()
