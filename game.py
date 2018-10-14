"""
Controller class for SWUG

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

from engine.dictionary import Dictionary
from views.interface_modes import InterfaceModes
from views.terminal.terminal import TerminalInterface


class Game:

    def __init__(self, interface, dictionary):
        self.dictionary = Dictionary(dictionary)
        self.interface_mode = interface

        if self.interface_mode == InterfaceModes.terminal:
            self.interface = TerminalInterface()
        elif self.interface_mode == InterfaceModes.desktop:
            #TODO: Implement desktop interface
            pass
        else:
            raise ValueError

    def run(self):
        self.interface.run()