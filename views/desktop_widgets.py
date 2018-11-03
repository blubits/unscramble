import pyglet
import glooey

class MenuWidget(glooey.Widget):
    
    custom_alignment = 'center'

    def __init__(self):
        super().__init__()

        menu_hbox = glooey.HBox()
        self.untimed_btn = MenuButton("Untimed")
        self.retries_btn = MenuButton("Retries")
        self.timed_btn = MenuButton("Timed")
        self.timed_retries_btn = MenuButton("Timed + Retries")
        menu_hbox.add(self.untimed_btn)
        menu_hbox.add(self.retries_btn)
        menu_hbox.add(self.timed_btn)
        menu_hbox.add(self.timed_retries_btn)

        vbox = glooey.VBox()
        vbox.add(menu_hbox)
        self._attach_child(vbox)

class MenuLabel(glooey.Label):
    custom_color = "white"
    custom_font_name = "Ubuntu"

class MenuButton(glooey.Button):
    Label = MenuLabel