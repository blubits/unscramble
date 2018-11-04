"""
Abstract base class for all Interfaces.

:Author:     Maded Batara III
:Author:     Jose Enrico Salinas
:Version:    v20181104
"""

from engine import ViewEvents

class Interface:
    """A view for the SWUG game engine.

    All views interacting with the SWUG engine should be subclassed from
    this interface. This will allow the controller to bind to your class.
    This also means that communication between the controller and your
    interface is two-way. Thus, you must expect to both send and recieve
    events.

    You can send three events: `create`, `answer`, and `end`. Look at the
    documentation for ViewEvents for more information. You must also
    expect to recieve four events from the controller: three variants
    of a response to `answer` (either correct, wrong, or duplicate) and
    `end`. (Notice how game end can be sent both ways; this is to allow
    the view to force quit the game, either through the user giving up or
    the timer running out, while also allowing the controller to calculate
    when the game actually ends.)
    """

    def __init__(self):
        """
        Initializes an Interface.

        When subclassing Interface, always make sure to call super().__init__()
        so the controller can communicate with your interface.
        """
        self.view_events = ViewEvents()
        self.controller = None

    @property
    def current_game(self):
        """Game: Current game on the controller."""
        return self.controller.current_game

    def initialize_event_handlers(self):
        """Bind all event handlers to the controller."""
        if self.controller is None:
            raise RuntimeError("Controller not registered in the view yet")
        else:
            self.controller.controller_events.answer_correct += self.on_answer_correct
            self.controller.controller_events.answer_wrong += self.on_answer_wrong
            self.controller.controller_events.answer_duplicate += self.on_answer_duplicate
            self.controller.controller_events.end += self.on_end

    def on_answer_correct(self):
        """
        Event handler when an answer sent by the interface has been
        judged as correct by the controller.
        """
        raise NotImplementedError

    def on_answer_wrong(self):
        """
        Event handler when an answer sent by the interface has been
        judged as wrong by the controller.
        """
        raise NotImplementedError

    def on_answer_duplicate(self):
        """
        Event handler when an answer sent by the interface has been
        judged as a duplicate by the controller.
        """
        raise NotImplementedError

    def on_end(self):
        """
        Event handler when the controller has determined that the game
        has ended. This usually results from a Game Over condition, e.g.
        retries have been maxed or the board is complete.
        """
        raise NotImplementedError

    def run(self):
        """
        Event loop, where your interface should be started. The controller
        will call this function to start your interface up.
        """
        raise NotImplementedError
