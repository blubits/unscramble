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

        self.intro = IntroWidget()
        self.menu = MenuWidget()
        self.game = GameWidget()

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
            self.gui.on_draw()

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

    def run(self):
        pyglet.app.run()
        print("In DesktopInterface")
