"""
Abstract base class for all Interfaces.

:Author:     Jose Enrico Salinas
:Version:    v20181103
"""

from engine import ViewEvents

class Interface():
    """
    A view for the SWUG game engine.

    Attributes:
        self.view_events (ViewEvents): Events happening on the view.
    """

    def __init__(self):
        self.view_events = ViewEvents()

    def run(self):
        raise NotImplementedError
