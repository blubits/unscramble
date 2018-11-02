"""
A dictionary of words.

:Author:     Maded Batara III
:Version:    v20181010
"""

from collections import Counter

from .dictionary_query import DictionaryQuery

class Dictionary(DictionaryQuery):
    """A dictionary of words.

    As this is a subclass of DictionaryQuery, this class supports all its
    methods."""

    def __init__(self, filename):
        """
        Initializes a new dictionary.

        Args:
            filename (str): Filename of the dictionary to be loaded in.
        """
        with open(filename) as dictionary_file:
            self.words = {
                word: Counter(word)
                for word in dictionary_file.read().splitlines()
            }

    def __repr__(self):
        """Implements repr(Dictionary)."""
        return "Dictionary(words={0})".format(len(self))

    def __str__(self):
        """Implements str(Dictionary)."""
        return "Dictionary with {0} entries".format(len(self))
