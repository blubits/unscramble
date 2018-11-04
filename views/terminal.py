"""
A basic terminal interface.

:Author:     Maded Batara III
:Version:    v20181104
"""

from engine import GameMode
from .interface import Interface

class TerminalInterface(Interface):

    def __init__(self):
        super().__init__()
        self.interface_end = True

    def introduce(self):
        print("Welcome to the SWUG terminal interface!")
        print("Generating a 7-letter puzzle...")
        print()
        self.view_events.create(GameMode.RETRIES, 7)

    def ask_input(self):
        word = input("Input a word > ")
        self.view_events.answer(word)

    def print_board(self):
        print("Word: {0}".format(self.current_game.word))
        print("Mistakes: {0}/{1} left".format(*self.current_game.mistakes))
        for length, words in self.current_game.words_by_length_filled().items():
            filled_in_words = [word for word in words if word is not None]
            print("{0}-letter words ({1}/{2}): {3}".format(
                length, len(filled_in_words), len(words), ' '.join(filled_in_words))
            )

    def on_answer_correct(self, word):
        print("Correct answer!")
        print()

    def on_answer_wrong(self, word):
        print("Wrong answer!")
        print()

    def on_answer_duplicate(self, word):
        print("You already answered that!")
        print()

    def on_end(self):
        if self.current_game.is_won():
            print("Congratulations, you won!")
        else:
            print("Game over :(")
        print("Score: {0}/{1}".format(*self.current_game.score))
        self.interface_end = True

    def run(self):
        self.initialize_event_handlers()
        self.introduce()
        self.interface_end = False
        while not self.interface_end:
            self.print_board()
            self.ask_input()
