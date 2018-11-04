"""
Abstract base class for all Interfaces.

:Author:     Jose Enrico Salinas
:Version:    v20181103
"""

from engine import ViewEvents

class Interface:
    """
    A view for the SWUG game engine.

    Attributes:
        self.view_events (ViewEvents): Events happening on the view.
    """

    def __init__(self):
        self.view_events = ViewEvents()
        self.controller = None

    @property
    def current_game(self):
        """Game: Current game on the controller."""
        return self.controller.current_game

    def initialize_event_handlers(self):
        if self.controller is None:
            raise RuntimeError("Controller not registered in the view yet")
        else:
            self.controller.controller_events.answer_correct += self.on_answer_correct
            self.controller.controller_events.answer_wrong += self.on_answer_wrong
            self.controller.controller_events.answer_duplicate += self.on_answer_duplicate
            self.controller.controller_events.end += self.on_end

    def on_answer_correct(self):
        raise NotImplementedError

    def on_answer_wrong(self):
        raise NotImplementedError

    def on_answer_duplicate(self):
        raise NotImplementedError

    def on_end(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError
