"""
A desktop interface for SWUG using pyglet

:Author:     Jose Enrico Salinas
:Version:    v20181102
"""

from .interface import Interface
from .desktop_states import DesktopStates

import pyglet
import glooey

class DesktopInterface(Interface):

    def __init__(self):
        self.window = pyglet.window.Window(width=1200, height=900)
        self.gui = glooey.Gui(self.window)

    def run(self):
        pyglet.app.run()
        print("In DesktopInterface")
