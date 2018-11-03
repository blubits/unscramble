"""
A basic terminal interface.

:Author:     Jose Enrico Salinas
:Version:    v20181102
"""

from .interface_handler import Interface

class TerminalInterface(Interface):

    def run(self):
        print("In TerminalInterface")
