"""
Abstract base class for all Interfaces.

:Author:     Jose Enrico Salinas
:Version:    v20181103
"""

from engine import ViewEvents

class Interface():

    def __init__(self):
        self.view_events = None

    def run(self):
        raise NotImplementedError
