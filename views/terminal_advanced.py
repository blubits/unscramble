from .interface_handler import InterfaceHandler

import npyscreen

class AdvancedTerminalInterface(InterfaceHandler):

    def __init__(self, engine):
        self.engine = engine
        self.app = TerminalApp()

    def run(self):
        self.app.run()

class TerminalApp(npyscreen.NPSApp):

    def main(self):
        pass