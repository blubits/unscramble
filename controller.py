"""
Controller class for SWUG

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

from engine.model import Model

from views.interface_modes import InterfaceModes
from views.terminal.terminal_basic import BasicTerminalInterface
from views.pyglet.desktop import DesktopInterface


class Controller:

    def __init__(self, interface, dictionary):
        self.model = Model(dictionary)
        self.interface_mode = interface

        if self.interface_mode == InterfaceModes.terminal_basic:
            self.interface = BasicTerminalInterface(self.model)
        elif self.interface_mode == InterfaceModes.terminal_advanced:
            #TODO: Implement advanced terminal interface
            pass
        elif self.interface_mode == InterfaceModes.desktop:
            self.interface = DesktopInterface(self.model)
        else:
            raise ValueError

    def run(self):
        self.interface.run()