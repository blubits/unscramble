"""
Controller class for SWUG

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

from engine.dictionary import Dictionary
from views.interface_modes import InterfaceModes

class Game:

    def __init__(self, interface, dictionary):
        self.dictionary = Dictionary(dictionary)
        self.interface = interface

    def run(self):
        raise NotImplementedError