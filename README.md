# Simple Word Unscramble Game

A simple word unscramble game, written in Python.

## Setup

Make sure Python >3.6 and [pipenv](https://pipenv.readthedocs.io/en/latest/) is installed on your system. Then simply run

```
$ pipenv install
$ pipenv run python main.py
```

to start the game.

---

## Architecture

The SWUG architecure is a basic implementation of [Model-View-Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller). If you're familiar with MVC, the game is divided into four main components:

* **The game engine**, i.e. the model, in the `engine` module. This is a simple implementation of the SWUG game logic. The main class we're concerned with is `Game`, which handles the entire game logic of a single game.
You might also be interested in the `Dictionary` and `DictionaryQuery` classes, which allow you to efficiently search, filter, and generate strings from a dictionary. Take a look at the documentation in each class for more.
* **The game views**, in the `views` module. We've implemented a terminal interface and a [Pyglet](https://pyglet.org)-based desktop interface. These all derive from a single base class, `Interface`, which we'll discuss more in the section below.
* **The game controller**, in `controller.py`. This is responsible for creating and manipulating game instances.
* **The game launcher**, in `main.py`. This is the main file a user will launch to start the game.

If you're not familiar with MVC, the bulk of the actual application logic is actually in the controller, which is responsible for manipulating the state of the game in response to user input, and relaying information to the user through the view (i.e. the interface) if the game requires it. This allows for something called *separation of concerns*: the interface does not need to care about how the game logic is implemented, and vice versa. The controller also does not care about what interface is hooked up to it; instead, it and any interface hooked up to it agree to expect a series of *events* that indicate when the game state has changed.

## Extensibility

If you need to change something in the side of the model, as long as you don't change method names around, you should be okay. Just make sure that, if you change core elements of the game logic (especially `DictionaryQuery` and `GameBoard`'s methods), check if it impacts the controller.

You'll most likely want to implement a new interface, though. In that case, simply make a new class in the `views` module that inherits from `Interface`, like so:

```python
from .interface import Interface

class NewInterface(Interface):

    def __init__(self):
        super().__init__()

    def on_answer_correct(self):
        raise NotImplementedError

    def on_answer_wrong(self):
        raise NotImplementedError

    def on_answer_duplicate(self):
        raise NotImplementedError

    def on_end(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

```

TODO: Complete extensibility documentation.


## Credits

`dictionary.txt` is the enable1 word list, source unknown; `popular.txt` is a subset of enable1, containing only the most popular ~25k words. Thanks to [dolph](https://github.com/dolph/dictionary).
