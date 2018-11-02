"""
A basic terminal interface.

:Author:     Jose Enrico Salinas
:Version:    v20181102
"""

from .interface_handler import InterfaceHandler

class TerminalInterface(InterfaceHandler):

    def run(self):
        print("Henlo world")