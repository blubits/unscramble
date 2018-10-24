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
        self.engine.set_game_restrictions(GameModes.timed_retries)

    def run(self):

        game_mode_choice = None
        while True:
            print("Select game mode [anagram / random / exit]")
            game_mode_choice = input()
            if game_mode_choice == "anagram" or game_mode_choice == "a":
                self.engine.set_game_mode(GameModes.anagrams)
                print()
                break
            elif game_mode_choice == "random" or game_mode_choice == "r":
                self.engine.set_game_mode(GameModes.random)
                print()
                break
            elif game_mode_choice == "exit" or game_mode_choice == "e":
                self.engine.reset()
                return

        game_restrictions_choice = None
        while True:
            print("Select game mode [lives / timed / timedlives / exit]")
            game_restrictions_choice = input()
            if game_restrictions_choice == "lives" or game_restrictions_choice == "l":
                self.engine.set_game_restrictions(GameModes.retries)
                print()
                break
            elif game_restrictions_choice == "timed" or game_restrictions_choice == "t":
                self.engine.set_game_restrictions(GameModes.timed)
                print()
                break
            elif game_restrictions_choice == "timedlives" or game_restrictions_choice == "h":
                self.engine.set_game_restrictions(GameModes.timed_retries)
                print()
                break
            elif game_mode_choice == "exit" or game_restrictions_choice == "e":
                self.engine.reset()
                return


        self.engine.start()

        if self.engine.game_restrictions == GameModes.retries or self.engine.game_restrictions == GameModes.timed_retries:
            print("Lives: {}".format(self.engine.retries))
        if self.engine.game_restrictions == GameModes.timed or self.engine.game_restrictions == GameModes.timed_retries:
            print("Time remaining: {}".format(self.engine.time_remaining()))
        print(self.engine)
        while not self.engine.is_complete() and not self.engine.is_dead():
            answer = input("Guess a word: ")
            self.engine.answer(answer)
            
            print(self.engine)
            if self.engine.game_restrictions == GameModes.retries or self.engine.game_restrictions == GameModes.timed_retries:
                print("Lives: {}".format(self.engine.retries))
            if self.engine.game_restrictions == GameModes.timed or self.engine.game_restrictions == GameModes.timed_retries:
                print("Time remaining: {}".format(self.engine.time_remaining()))