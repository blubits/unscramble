"""
Controller class that initializes game dictionary,
and interfaces

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

from engine import Dictionary, Game, GameMode, ControllerEvents

class Controller:

    def __init__(self, interface, dictionary_file):
        """
        Initializes a new Controller.

        Args:
            interface (InterfaceHandler): A client/view of the SWUG engine.
            dictionary_file (str): Path to the dictionary file to
                load.
        """
        self.interface = interface
        self.dictionary = Dictionary(dictionary_file)
        self.current_game = None
        self.controller_events = ControllerEvents()
        # TODO register event handlers

    def on_game_create(self, game_mode, word_length):
        word = self.dictionary.filter_by_length(word_length).choice()
        query = self.dictionary.filter_from_string(word)
        if game_mode == GameMode.TIMED_RETRIES or game_mode == GameMode.RETRIES:
            self.current_game = Game(word, query, retries=3)
        else:
            self.current_game = Game(word, query)

    def on_game_answer(self, word):
        pass

    def on_game_over(self):
        pass

    def run_interface(self):
        self.interface.run()
