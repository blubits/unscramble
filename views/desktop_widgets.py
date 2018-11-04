import pyglet
import glooey

from engine import GameMode
from .desktop_states import DesktopStates

class IntroWidget(glooey.Widget):
    
    custom_alignment = 'center'

    def __init__(self, interface):
        super().__init__()
        self.interface = interface
        title = TitleLabel("SWUG")
        self._attach_child(title)

class MenuWidget(glooey.Widget):
    
    custom_alignment = 'center'

    def __init__(self, interface):
        super().__init__()
        self.interface = interface
        title = TitleLabel("SWUG 0.1")

        untimed_btn = MenuButton("Untimed")
        retries_btn = MenuButton("Retries")
        timed_btn = MenuButton("Timed")
        timed_retries_btn = MenuButton("Timed + Retries")


        def handle_untimed_btn(source):
            self.interface.view_events.create(GameMode.UNTIMED, 7)
            self.interface.state = DesktopStates.game

        def handle_retries_btn(source):
            self.interface.view_events.create(GameMode.RETRIES, 7)
            self.interface.state = DesktopStates.game

        def handle_timed_btn(source):
            self.interface.view_events.create(GameMode.TIMED, 7)
            self.interface.state = DesktopStates.game

        def handle_timed_retries_btn(source):
            self.interface.view_events.create(GameMode.TIMED_RETRIES, 7)
            self.interface.state = DesktopStates.game

        untimed_btn.push_handlers(on_click=handle_untimed_btn)
        retries_btn.push_handlers(on_click=handle_retries_btn)
        timed_btn.push_handlers(on_click=handle_timed_btn)
        timed_retries_btn.push_handlers(on_click=handle_timed_retries_btn)

        menu_hbox = glooey.HBox()
        menu_hbox.add(untimed_btn)
        menu_hbox.add(retries_btn)
        menu_hbox.add(timed_btn)
        menu_hbox.add(timed_retries_btn)

        vbox = glooey.VBox()
        vbox.add(title)
        vbox.add(menu_hbox)
        self._attach_child(vbox)

class MenuLabel(glooey.Label):
    custom_color = "white"
    custom_font_name = "Ubuntu"
    custom_font_size = 18

class MenuButton(glooey.Button):
    Label = MenuLabel

class TiledBackground(glooey.Background):
    custom_center = pyglet.resource.texture("resources/images/background.png")

class TitleLabel(MenuLabel):
    custom_font_size = 70
    custom_alignment = "center"
    custom_padding = 10

class GameWidget(glooey.Widget):

    def __init__(self, interface):
        super().__init__()
        self.interface = interface

        self.vbox = glooey.VBox()
        self.game_board_hbox = GameBoardWidget(interface)
        self.game_input = GameInputWidget(interface)
        self.game_options = GameOptionsWidget(interface)

        self.vbox.add(self.game_board_hbox)
        self.vbox.add(self.game_input)
        self.vbox.add(self.game_options)
        self._attach_child(self.vbox)

class GameBoardWidget(glooey.Widget):

    custom_alignment = "center"

    def __init__(self, interface):
        super().__init__()
        self.interface = interface

        self.hbox = glooey.HBox()
        self.hbox.add(MenuLabel("GameBoardWidget"))
        self._attach_child(self.hbox)

class GameInputWidget(glooey.Widget):

    custom_alignment = "center"

    def __init__(self, interface):
        super().__init__()
        self.interface = interface

        self.vbox = glooey.VBox()
        self.input_display = GameTileDisplay(interface, "A")
        self.tile_display = GameTileDisplay(interface, "a")
        self.vbox.add(self.input_display)
        self.vbox.add(self.tile_display)
        self._attach_child(self.vbox)

class GameTileDisplay(glooey.Widget):

    custom_alignment = "center"

    def __init__(self, interface, string):
        super().__init__()
        self.interface = interface

        self.hbox = glooey.HBox()
        for char in string:
            self.hbox.add(GameTile(interface, char))
        self._attach_child(self.hbox)

class GameTile(glooey.Image):

    custom_alignment = "center"
    custom_padding = 10

    def __init__(self, interface, char):
        super().__init__()
        image = pyglet.image.load("resources/images/tiles.png")
        self.char_grid = pyglet.image.ImageGrid(image, 2, 13)
        print(self.char_grid[0])
        self._image = self.char_grid[0]

class GameOptionsWidget(glooey.Widget):

    custom_alignment = "left"

    def __init__(self, interface):
        super().__init__()
        self.interface = interface

        self.hbox = glooey.HBox()
        self.hbox.add(GameInformationWidget(interface))
        self.hbox.add(GameButtonsWidget(interface))
        self._attach_child(self.hbox)

class GameInformationWidget(glooey.Widget):

    custom_alignment = "left"
    custom_padding = 30

    def __init__(self, interface):
        super().__init__()
        self.interface = interface

        self.hbox = glooey.HBox()
        self.hbox.add(InformationWidget("Time", "00:00"))
        self.hbox.add(InformationWidget("Retries", "3"))
        self.hbox.add(InformationWidget("Score", "0"))
        self._attach_child(self.hbox)

class InformationWidget(glooey.Widget):

    custom_padding = 10

    def __init__(self, label, information):
        super().__init__()

        self.vbox = glooey.VBox()
        self.vbox.add(MenuLabel(label))
        self.vbox.add(MenuLabel(information))
        self._attach_child(self.vbox)

class GameButtonsWidget(glooey.Widget):
    custom_alignment = "right"

    def __init__(self, interface):
        super().__init__()
        self.interface = interface

        self.hbox = glooey.HBox()
        self.check_ans_button = GameButton("A")
        self.hbox.add(self.check_ans_button)
        self._attach_child(self.hbox)

class GameButton(glooey.Button):
    
    class Label(glooey.Label):
        custom_padding = 30
        custom_color = "#000000"

    class Base(glooey.Background):
        custom_color = "#aaaaaa"
