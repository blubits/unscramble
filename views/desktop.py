"""
A desktop interface for SWUG using pyglet

:Author:     Jose Enrico Salinas
:Version:    v20181102
"""

from .interface_handler import InterfaceHandler
from .desktop_states import DesktopStates

import pyglet
import glooey

class DesktopInterface(InterfaceHandler):

    def __init__(self):
        self.window = pyglet.window.Window(width=1200, height=900)
        self.gui = glooey.Gui(self.window)

    def run(self):
        pyglet.app.run()
        print("In DesktopInterface")