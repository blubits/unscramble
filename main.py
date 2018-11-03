"""
Main launch file to start the game
and process launch options

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

import sys

from views import DesktopInterface, TerminalInterface
from controller import Controller

if __name__ == "__main__":
    launch_args = sys.argv

    dictionary_address = "resources/dict/dictionary.txt"
    if len(launch_args) > 1 and launch_args[1][-4:] == ".txt":
        dictionary_address = launch_args[1]

    interface_mode = TerminalInterface()
    if '-d' in launch_args:
        interface_mode = DesktopInterface()

    try:
        controller = Controller(interface=interface_mode,
                                dictionary_file=dictionary_address)
        controller.run_interface()
    except FileNotFoundError:
        print("Dictionary file cannot be located.")
