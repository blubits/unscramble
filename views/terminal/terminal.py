import urwid

from ..interface_handler import Interface_Handler

class BasicTerminalInterface(Interface_Handler):

    def __init__(self):
        txt = urwid.Text(u"Hello World")
        fill = urwid.Filler(txt, 'top')
        self.loop = urwid.MainLoop(fill)
    
    def run(self):
        self.loop.run()