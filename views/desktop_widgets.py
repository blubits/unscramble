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
            self.interface.view_events.create(GameMode.UNTIMED, 5)
            self.interface.state = DesktopStates.game

        def handle_retries_btn(source):
            self.interface.view_events.create(GameMode.RETRIES, 5)
            self.interface.state = DesktopStates.game

        def handle_timed_btn(source):
            self.interface.view_events.create(GameMode.TIMED, 5)
            self.interface.state = DesktopStates.game

        def handle_timed_retries_btn(source):
            self.interface.view_events.create(GameMode.TIMED_RETRIES, 5)
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
        self.game_options = GameOptionsWidget(interface, self)

        self.vbox.add(self.game_board_hbox)
        self.vbox.add(self.game_input)
        self.vbox.add(self.game_options)
        self._attach_child(self.vbox)

    def refresh_board(self):
        self.game_board_hbox.populate_board()
        self.game_input.update_display()

    def handle_keypress(self, key):
        self.game_input.input_key(chr(key))

class GameBoardWidget(glooey.Widget):

    custom_alignment = "left"
    custom_horz_padding = 30

    def __init__(self, interface):
        super().__init__()
        self.interface = interface
        self.vbox = glooey.Grid()
        self._attach_child(self.vbox)

    def populate_board(self):

        # remove all children in game board
        col = 0
        row = 0
        vbox_children = [child for child in self.vbox]
        for child in vbox_children:
            if row == 5:
                col += 1
                row = 0
            self.vbox.remove(row, col)
            row += 1

        # repopulate game board
        col = 0
        row = 0
        for length, words in self.interface.current_game.words_by_length_filled().items():
            for word in words:
                if row == 5:
                    col += 1
                    row = 0
                if word is not None:
                    self.vbox.add(row, col, GameBoardRow(self.interface, word))
                else:
                    self.vbox.add(row, col, GameBoardRow(
                        self.interface, " " * length))
                row += 1

class GameBoardRow(glooey.Widget):
    custom_alignment = "left"

    def __init__(self, interface, string):
        super().__init__()
        self.interface = interface

        self.hbox = glooey.HBox()
        for char in string:
            self.hbox.add(GameBoardTile(interface, char))
        self._attach_child(self.hbox)

class GameBoardTile(glooey.Image):

    custom_alignment = "center"
    custom_padding = 1

    def __init__(self, interface, char):
        super().__init__()
        image = pyglet.image.load("resources/images/boardletters.png")
        self.char_grid = pyglet.image.ImageGrid(image, 3, 9)
        if char == " ":
            self._image = self.char_grid[0]
        else:
            self._image = self.char_grid[ord(char.lower()) - ord("a") + 1]

class GameInputWidget(glooey.Widget):

    custom_alignment = "center"

    def __init__(self, interface):
        super().__init__()
        self.interface = interface

        self.vbox = glooey.VBox()
        self.input_display = GameTileDisplay(interface, "A")
        self.tile_display = GameTileDisplay(interface, "A")
        self.vbox.add(self.input_display)
        self.vbox.add(self.tile_display)
        self._attach_child(self.vbox)

        self.input_string = ""

    def input_key(self, key):
        self.game_string = self.interface.current_game.word
        if key in self.game_string:
            self.input_string = self.input_string + key

    def update_display(self):
        self.game_string = self.interface.current_game.word
        self.input_display.update_display(self.input_string)
        self.tile_display.update_display(self.game_string)

class GameTileDisplay(glooey.Widget):

    custom_alignment = "center"

    def __init__(self, interface, string):
        super().__init__()
        self.interface = interface
        self.string = string

        self.hbox = glooey.HBox()
        for char in string:
            self.hbox.add(GameTile(interface, char))
        self._attach_child(self.hbox)

    def update_display(self, string):
        self.string = string

        hbox_children = [child for child in self.hbox]
        for child in hbox_children:
            self.hbox.remove(child)

        for char in string:
            self.hbox.add(GameTile(self.interface, char))

class GameTile(glooey.Image):

    custom_alignment = "center"
    custom_padding = 10

    def __init__(self, interface, char):
        super().__init__()
        image = pyglet.image.load("resources/images/tiles.png")
        self.char_grid = pyglet.image.ImageGrid(image, 2, 13)
        self._image = self.char_grid[ord(char.lower()) - ord("a")]

class GameOptionsWidget(glooey.Widget):

    custom_alignment = "left"

    def __init__(self, interface, game_input):
        super().__init__()
        self.interface = interface
        self.game_input = game_input

        self.hbox = glooey.HBox()
        self.hbox.add(GameInformationWidget(interface))
        self.hbox.add(GameButtonsWidget(interface, game_input))
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

    def __init__(self, interface, game_input):
        super().__init__()
        self.interface = interface
        self.game_input = game_input

        def handle_ans_btn(source):
            self.interface.view_events.answer(self.game_input.game_input.input_string)
            self.game_input.game_input.input_string = ""

        hbox = glooey.HBox()
        check_ans_button = GameButton("Answer")
        check_ans_button.push_handlers(on_click=handle_ans_btn)
        hbox.add(check_ans_button)
        self._attach_child(hbox)

class GameButton(glooey.Button):

    class Label(glooey.Label):
        custom_padding = 30
        custom_color = "#000000"

    class Base(glooey.Background):
        custom_color = "#cccccc"
