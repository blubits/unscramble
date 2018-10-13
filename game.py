"""
Controller class for SWUG

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

from views.interface_modes import InterfaceModes

class Game:

    def __init__(self, interface=InterfaceModes.terminal):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError