"""
A basic terminal interface.

:Author:     Jose Enrico Salinas
:Version:    v20181102
"""

from engine import GameMode
from .interface import Interface

class TerminalInterface(Interface):

    def __init__(self):
        super().__init__()
        self.game_end = True

    def introduce(self):
        print("Welcome to the SWUG terminal interface!")
        print("Generating a 7-letter puzzle...")
        print()

    def ask_input(self):
        word = input("Input a word > ")
        self.view_events.answer(word)

    def print_board(self):
        print("Word: {0}".format(self.controller.current_game.word))
        print("Retries: {0}/{1} left".format(
            self.controller.current_game.retries,
            self.controller.current_game.maximum_retries)
        )
        for length, words in self.controller.current_game.board.words_by_length_filled().items():
            filled_in_words = [word for word in words if word is not None]
            print("{0}-letter words ({1}/{2}): {3}".format(
                length, len(filled_in_words), len(words), ' '.join(filled_in_words))
            )

    def on_answer_correct(self):
        print("Correct answer!")
        print()

    def on_answer_wrong(self):
        print("Wrong answer!")
        print()

    def on_answer_duplicate(self):
        print("You already answered that!")
        print()

    def on_end(self):
        print("Game over :(")
        print("Score: {0}/{1}".format(self.controller.current_game.score,
                                      self.controller.current_game.maximum_score))
        self.game_end = True

    def run(self):
        print("DEBUG: In TerminalInterface")
        # attempt to register controller event handlers
        if self.controller is None:
            raise RuntimeError("Controller not registered in the view yet")
        else:
            self.controller.controller_events.answer_correct += self.on_answer_correct
            self.controller.controller_events.answer_wrong += self.on_answer_wrong
            self.controller.controller_events.answer_duplicate += self.on_answer_duplicate
            self.controller.controller_events.end += self.on_end
        self.introduce()
        self.view_events.create(GameMode.RETRIES, 7)
        self.game_end = False
        while not self.game_end:
            self.print_board()
            self.ask_input()
