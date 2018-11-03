"""
A basic terminal interface.

:Author:     Jose Enrico Salinas
:Version:    v20181102
"""

from .interface import Interface

class TerminalInterface(Interface):

    def __init__(self):
        pass

    def run(self):
        print("In TerminalInterface")
