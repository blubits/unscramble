"""
A basic terminal interface using stdin and stdout.

:Author:     Jose Enrico Salinas
:Version:    v20181020
"""

from .interface_handler import InterfaceHandler
from engine.game_modes import GameModes


class BasicTerminalInterface(InterfaceHandler):

    def __init__(self, engine):
        self.engine = engine
        self.engine.set_game_mode(GameModes.random)
        self.engine.set_game_restrictions(GameModes.timed_retries)

    def run(self):
        self.engine.start()
        if self.engine.game_restrictions == GameModes.retries or self.engine.game_restrictions == GameModes.timed_retries:
            print("Lives: {}".format(self.engine.retries))
        if self.engine.game_restrictions == GameModes.timed or self.engine.game_restrictions == GameModes.timed_retries:
            print("Time remaining: {}".format(self.engine.time_remaining()))
        print(self.engine)
        while not self.engine.is_complete() and not self.engine.is_dead():
            answer = input("Guess a word: ")
            self.engine.answer(answer)

            if self.engine.game_restrictions == GameModes.retries or self.engine.game_restrictions == GameModes.timed_retries:
                print("Lives: {}".format(self.engine.retries))
            if self.engine.game_restrictions == GameModes.timed or self.engine.game_restrictions == GameModes.timed_retries:
                print("Time remaining: {}".format(self.engine.time_remaining()))
            print(self.engine)