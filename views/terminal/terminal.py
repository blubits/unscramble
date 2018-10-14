import urwid

from ..inteface import Interface

class TerminalInterface(Interface):

    def __init__(self):
        txt = urwid.Text(u"Hello World")
        fill = urwid.Filler(txt, 'top')
        self.loop = urwid.MainLoop(fill)
    
    def run(self):
        self.loop.run()