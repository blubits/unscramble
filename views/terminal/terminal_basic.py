import urwid

from ..interface_handler import Interface_Handler

class BasicTerminalInterface(Interface_Handler):

    def __init__(self, dictionary, game_board):
        self.game_board = game_board

    def run(self):

        print(self.game_board)
        while not self.game_board.is_complete():
            answer = input("Guess a word: ")
            self.game_board.answer(answer)
            print(self.game_board)