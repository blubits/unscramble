"""
Main launch file to start the game
and process launch options

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

import sys

from views.interface_modes import InterfaceModes
from controller import Controller

if __name__ == "__main__":
    launch_args = sys.argv

    dictionary_address = "resources/dict/dictionary.txt"
    if len(launch_args) > 1 and launch_args[1][-4:] == ".txt":
        dictionary_address = launch_args[1]

    interface_mode = InterfaceModes.terminal_basic
    if '-d' in launch_args:
        interface_mode = InterfaceModes.desktop
    elif '-a' in launch_args:
        interface_mode = InterfaceModes.terminal_advanced

    try:
        game = Controller(interface=interface_mode, dictionary=dictionary_address)
        game.run()
    except(FileNotFoundError):
        print("Dictionary file cannot be located.")
