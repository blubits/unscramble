"""
A dictionary of words.

:Author:     Maded Batara III
:Version:    v20181010
"""

from collections import Counter
import random

class Dictionary:

    def __init__(self, filename):
        with open(filename) as dictionary_file:
            self.words = dictionary_file.read().splitlines()
            self.frequencies = {word: Counter(word) for word in self.words}

    def __contains__(self, word):
        return word in self.words

    def filter_from_string(self, string):
        """
        Generate a list of words contained in a string.

        Args:
            string (str): String of alphabetical characters.
        """
        result = []
        freq_string = Counter(string)
        for word, freq_word in self.frequencies.items():
            if all(freq_string[x] >= freq_word[x] for x in freq_word):
                result.append(word)
        return result

    def random(self, n=1):
        return [random.choice(self.words) for _ in range(n)]

    def sort(self):
        self.words.sort()
