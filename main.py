import sys

from views.interface_modes import InterfaceModes
from game import Game

if __name__ == "__main__":
    launch_args = sys.argv

    dictionary_address = "dictionary.txt"
    if launch_args[1][-4:] == ".txt":
        dictionary_address = launch_args[1]

    interface_mode = InterfaceModes.terminal
    if '-d' in launch_args:
        interface_mode = InterfaceModes.desktop
    elif '-w' in launch_args:
        interface_mode = InterfaceModes.web

    try:
        game = Game(interface=interface_mode, dictionary=dictionary_address)
    except(FileNotFoundError):
        print("Dictionary file cannot be located.")