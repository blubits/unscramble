"""
Events passed by between view and controller in the game.

:Author:     Maded Batara III
:Version:    v20181103
"""

import events

class ViewEvents(events.Events):
    """
    Events that happen in the view and are listened to by the controller.

    Events:
        create: Raise when a game is created on the view, through a
            "Play Now" button, for example. The controller should
            make a new game appropriately.

            Messages:
                game_mode (GameMode): Type of game to create.
                word_length (int): Length of word to make game from.

        answer: Raise when an answer is entered on the view. The controller
            should fill this up on the game, and send an appropriate
            event back (see ControllerEvents).

            Messages:
                word (str): Word to fill up answer from.

        end: Raise when a game is ended, through user feedback on the view
            or otherwise. The controller should call game end on the model
            and clean up.
    """
    __events__ = ('create', 'answer', 'end')

class ControllerEvents(events.Events):
    """
    Events that happen in the controller and are listened to by the view.

    Events:
        answer_correct: Raise when an answer from the view is determined
            as correct, i.e. on the board and not filled up. The view
            should prompt the user accordingly.

        answer_wrong: Raise when an answer from the view is determined
            as wrong, i.e. not on the board. The view should prompt
            the user accordingly.

        answer_duplicate: Raise when an answer from the view is determined
            as a duplicate, i.e. already on the board. The view should
            prompt the user accordingly.

        end: Raise when a game is ended, through model manipulation on
            the controller or otherwise. The view should display end game
            and clean up.

    """
    __events__ = ('answer_correct', 'answer_wrong', 'answer_duplicate', 'end')
