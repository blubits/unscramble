"""
Enum class for GUI states

:Author:     Jose Enrico Salinas
:Version:    v20181021
"""

from enum import Enum

class InterfaceStates(Enum):

    intro = "INTERFACE.STATE.INTRO"
    menu = "INTERFACE.STATE.MENU"
    options = "INTERFACE.STATE.OPTIONS"
    game = "INTERFACE.STATE.GAME"