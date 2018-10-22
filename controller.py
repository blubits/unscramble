"""
Controller class for SWUG

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

from engine.engine import Engine

from views.interface_modes import InterfaceModes
from views.terminal_basic import BasicTerminalInterface
from views.desktop import DesktopInterface
from views.terminal_advanced import AdvancedTerminalInterface


class Controller:

    def __init__(self, interface, dictionary):
        self.engine = Engine(dictionary)
        self.interface_mode = interface

        if self.interface_mode == InterfaceModes.terminal_basic:
            self.interface = BasicTerminalInterface(self.engine)
        elif self.interface_mode == InterfaceModes.terminal_advanced:
            self.interface = AdvancedTerminalInterface(self.engine)
        elif self.interface_mode == InterfaceModes.desktop:
            self.interface = DesktopInterface(self.engine)
        else:
            raise ValueError

    def run(self):
        self.interface.run()
