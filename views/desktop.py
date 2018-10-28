"""
A desktop interface for SWUG using pyglet

:Author:     Jose Enrico Salinas
:Version:    v20181020
"""


from .interface_handler import InterfaceHandler
from .interface_states import InterfaceStates

import time

import pyglet

class DesktopInterface(InterfaceHandler):

    def __init__(self, engine):
        self.engine = engine
        self.desktop_state = InterfaceStates.intro
        self.window = pyglet.window.Window(resizable=True)

        #Event handlers
        @self.window.event
        def on_draw():
            self.window.clear()

            if self.desktop_state == InterfaceStates.intro:
                self.draw_intro()
                pyglet.clock.schedule_once(self.set_to_menu, 3)

    def draw_intro(self):

        game_font_name = 'Ubuntu'

        main_title = pyglet.text.Label('SWUG',
            font_name = game_font_name,
            font_size = 36,
            x = self.window.width//2,
            y = self.window.height//2,
            anchor_x = 'center',
            anchor_y = 'center'
        )

        sub_title = pyglet.text.Label('The Simple Word Unscrabler Game',
            font_name = game_font_name,
            font_size = 12,
            x = self.window.width//2,
            y = self.window.height//2 - 36,
            anchor_x = 'center',
            anchor_y = 'center'
        )

        credits_by = pyglet.text.Label('by',
            font_name = game_font_name,
            font_size = 8,
            x = self.window.width//2,
            y = self.window.height//2 - 60,
            anchor_x = 'center',
            anchor_y = 'center'
        )

        credits_one = pyglet.text.Label('Maded Batara',
            font_name = game_font_name,
            font_size = 10,
            x = self.window.width//2,
            y = self.window.height//2 - 70,
            anchor_x = 'center',
            anchor_y = 'center'
        )

        credits_two = pyglet.text.Label('Jose Enrico Salinas',
            font_name = game_font_name,
            font_size = 8,
            x = self.window.width//2,
            y = self.window.height//2 - 82,
            anchor_x = 'center',
            anchor_y = 'center'
        )

        main_title.draw()
        sub_title.draw()
        credits_by.draw()
        credits_one.draw()
        credits_two.draw()

    def set_to_menu(self, callback=None):
        self.desktop_state = InterfaceStates.menu
 
    def run(self):
        pyglet.app.run()