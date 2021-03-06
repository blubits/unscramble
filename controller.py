"""
Controller class that initializes game dictionary,
and interfaces

:Author:     Jose Enrico Salinas
:Author:     Maded Batara III
:Version:    v20181013
"""

from engine import Dictionary, Game, GameMode, ControllerEvents

class Controller:

    def __init__(self, interface, dictionary_file):
        """
        Initializes a new Controller.

        Args:
            interface (Interface): A client/view of the SWUG engine.
            dictionary_file (str): Path to the dictionary file to
                load.
        """
        self.dictionary = Dictionary(dictionary_file)
        self.current_game = None

        self.interface = interface
        # Enable two-way communication between C and V
        # On the view side, self.controller.controller_events can
        # then be used to register event handlers
        self.interface.controller = self

        self.controller_events = ControllerEvents()
        # register view event handlerrs
        self.interface.view_events.create += self.on_create
        self.interface.view_events.answer += self.on_answer
        self.interface.view_events.end += self.on_end

    def on_create(self, game_mode, word_length):
        word = self.dictionary.filter_by_length(word_length).choice()
        query = self.dictionary.filter_from_string(
            word).filter_by_length(3, word_length)
        if game_mode == GameMode.TIMED_RETRIES or game_mode == GameMode.RETRIES:
            self.current_game = Game(
                word, query, mistakes=3, mode=game_mode)
        else:
            self.current_game = Game(word, query, mode=game_mode)

    def on_answer(self, word):
        if self.current_game.on_board(word):
            self.controller_events.answer_duplicate(word)
        else:
            if self.current_game.answer(word):
                self.controller_events.answer_correct(word)
            else:
                self.controller_events.answer_wrong(word)
        if self.current_game.is_game_over:
            self.controller_events.end()

    def on_end(self):
        if not self.current_game.is_game_over:
            self.current_game.end_game()

    def run_interface(self):
        self.interface.run()
