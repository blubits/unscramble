import pyglet
import glooey

class IntroWidget(glooey.Widget):
    
    custom_alignment = 'center'

    def __init__(self):
        super().__init__()
        title = TitleLabel("SWUG")
        self._attach_child(title)

class MenuWidget(glooey.Widget):
    
    custom_alignment = 'center'

    def __init__(self):
        super().__init__()
        title = TitleLabel("SWUG 0.1")

        menu_hbox = glooey.HBox()
        untimed_btn = MenuButton("Untimed")
        retries_btn = MenuButton("Retries")
        timed_btn = MenuButton("Timed")
        timed_retries_btn = MenuButton("Timed + Retries")
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

    def __init__(self):
        super().__init__()

        self.vbox = glooey.VBox()
        self.game_board_hbox = glooey.HBox()

        self.vbox.add(self.game_board_hbox)
        self._attach_child(self.vbox)