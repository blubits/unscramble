"""
A desktop interface for SWUG using pyglet

:Author:     Jose Enrico Salinas
:Version:    v20181020
"""


from .interface_handler import InterfaceHandler

import pyglet
from pyglet.window import event

class DesktopInterface(InterfaceHandler):

    def __init__(self, engine):
        self.engine = engine
        self.window = pyglet.window.Window()
 
    def run(self):
        pyglet.app.run()