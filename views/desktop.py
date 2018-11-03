"""
A desktop interface for SWUG using pyglet

:Author:     Jose Enrico Salinas
:Version:    v20181102
"""

from .interface_handler import InterfaceHandler
from .desktop_states import DesktopStates

import pyglet

class DesktopInterface(InterfaceHandler):

    def __init__(self):
        self.state = DesktopStates.menu
        self.window = pyglet.window.Window(width=1200, height=900)

        @self.window.event
        def on_draw():
            self.window.clear()

            if self.state == DesktopStates.intro:
                #TODO: Implement intro display
                print("In Intro")
            elif self.state == DesktopStates.menu:
                #TODO: Implement menu display
                print("In Menu")
            elif self.state == DesktopStates.options:
                #TODO: Implement options display
                print("In Options")
            elif self.state == DesktopStates.game:
                #TODO: Implement game display
                print("In game")

    def run(self):
        pyglet.app.run()
        print("In DesktopInterface")