"""
Main launch file to start the game and process launch options.

:Author:     Maded Batara III
:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

import sys

from views import DesktopInterface, TerminalInterface
from controller import Controller

def main():
    if '-h' in sys.argv or '--help' in sys.argv:
        print("Usage: python main.py [FILE] [-d] [--help]")
        print("Load the SWUG game, using FILE as the dictionary if given.")
        print("    -t            run in terminal mode (default)")
        print("    -d            run in desktop mode")
        print("    -h, --help    print this help message")
        exit(0)

    if len(sys.argv) > 1 and sys.argv[1].endswith(".txt"):
        dictionary_address = sys.argv[1]
    else:
        dictionary_address = "resources/dict/dictionary.txt"

    if '-d' in sys.argv:
        interface_mode = DesktopInterface()
    else:
        interface_mode = TerminalInterface()

    try:
        controller = Controller(interface=interface_mode,
                                dictionary_file=dictionary_address)
        controller.run_interface()
    except FileNotFoundError:
        print("Dictionary file cannot be located.")

if __name__ == "__main__":
    main()
