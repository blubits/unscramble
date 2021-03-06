"""
A desktop interface for SWUG using pyglet

:Author:     Jose Enrico Salinas
:Version:    v20181102
"""

from .interface import Interface
from .desktop_states import DesktopStates
from .desktop_widgets import *

import pyglet
import glooey

class DesktopInterface(Interface):

    def __init__(self):
        super().__init__()
        self.state = DesktopStates.menu
        self.window = pyglet.window.Window(width=1200, height=900)

        background = TiledBackground()

        self.gui = glooey.Gui(self.window)
        self.gui.add(background)

        self.intro = IntroWidget(self)
        self.menu = MenuWidget(self)
        self.game = GameWidget(self)

        self.time_remaining = None

        @self.window.event
        def on_draw():
            if self.state == DesktopStates.intro:
                self.clear_window()
                self.gui.add(self.intro)
                pyglet.clock.schedule_once(menu_state, 2)
            elif self.state == DesktopStates.menu:
                self.clear_window()
                self.gui.add(self.menu)
            elif self.state == DesktopStates.options:
                # TODO: Implement options display
                pass
            elif self.state == DesktopStates.game:
                self.clear_window()
                self.gui.add(self.game)
                self.game.refresh_board()
            self.gui.on_draw()

        @self.window.event()
        def on_key_press(symbol, modifer):
            if self.state == DesktopStates.game:
                self.game.handle_keypress(symbol)

        def intro_state(dt):
            self.state = DesktopStates.intro

        def menu_state(dt):
            self.state = DesktopStates.menu

        def game_state(dt):
            self.state = DesktopStates.game

    def clear_window(self):
        try:
            self.gui.remove(self.intro)
        except glooey.helpers.UsageError:
            pass
        try:
            self.gui.remove(self.menu)
        except glooey.helpers.UsageError:
            pass
        try:
            self.gui.remove(self.game)
        except glooey.helpers.UsageError:
            pass

    def on_answer_correct(self, word):
        pass

    def on_answer_wrong(self, word):
        pass

    def on_answer_duplicate(self, word):
        pass

    def on_end(self):
        self.state = DesktopStates.menu

    def run(self):
        self.initialize_event_handlers()
        self.interface_end = False
        pyglet.app.run()
