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

        untimed_btn = MenuButton("Untimed")
        retries_btn = MenuButton("Retries")
        timed_btn = MenuButton("Timed")
        timed_retries_btn = MenuButton("Timed + Retries")

        def handle_untimed_btn():
            pass

        def handle_retries_btn():
            pass

        def handle_timed_btn():
            pass

        def handle_timed_retries_btn():
            pass

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

    def __init__(self):
        super().__init__()

        self.vbox = glooey.VBox()
        self.game_board_hbox = GameBoardWidget()
        self.game_input = GameInputWidget()
        self.game_options = GameOptionsWidget()

        self.vbox.add(self.game_board_hbox)
        self.vbox.add(self.game_input)
        self.vbox.add(self.game_options)
        self._attach_child(self.vbox)

class GameBoardWidget(glooey.Widget):

    custom_alignment = "center"

    def __init__(self):
        super().__init__()

        self.hbox = glooey.HBox()
        self.hbox.add(MenuLabel("GameBoardWidget"))
        self._attach_child(self.hbox)

class GameInputWidget(glooey.Widget):

    custom_alignment = "center"

    def __init__(self):
        super().__init__()

        self.vbox = glooey.VBox()
        self.vbox.add(MenuLabel("GameInputWidget"))
        self._attach_child(self.vbox)

class GameOptionsWidget(glooey.Widget):

    custom_alignment = "left"

    def __init__(self):
        super().__init__()

        self.hbox = glooey.HBox()
        self.hbox.add(GameInformationWidget())
        self.hbox.add(GameButtonsWidget())
        self._attach_child(self.hbox)

class GameInformationWidget(glooey.Widget):

    custom_alignment = "left"
    custom_padding = 30

    def __init__(self):
        super().__init__()

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

    def __init__(self):
        super().__init__()

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
