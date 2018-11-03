"""
A desktop interface for SWUG using pyglet

:Author:     Jose Enrico Salinas
:Version:    v20181102
"""

from .interface_handler import Interface
from .desktop_states import DesktopStates
from .widgets import *

import pyglet
import glooey

class DesktopInterface(Interface):

    def __init__(self):
        self.state = DesktopStates.menu
        self.window = pyglet.window.Window(width=1200, height=900)
        self.gui = glooey.Gui(self.window)

        self.menu = MenuWidget()
        self.gui.add(self.menu)

        @self.window.event
        def on_draw():
            if self.state == DesktopStates.intro:
                #TODO: Implement intro display
                pass
            elif self.state == DesktopStates.menu:
                #TODO: Implement menu display
                # self.draw_menu()
                self.menu.do_draw()
            elif self.state == DesktopStates.options:
                #TODO: Implement options display
                print("In Options")
            elif self.state == DesktopStates.game:
                #TODO: Implement game display
                print("In game")
            self.gui.on_draw()


    def run(self):
        pyglet.app.run()
        print("In DesktopInterface")
