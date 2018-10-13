"""
A query on a dictionary.

:Author:     Maded Batara III
:Version:    v20181013
"""

from collections import Counter
from functools import reduce
from operator import or_ as union
import random

class DictionaryQuery:

    def __init__(self, words):
        self.words = {
            word: Counter(word)
            for word in words
        }

    def __contains__(self, word):
        return word in self.words

    def __iter__(self):
        return sorted(iter(self.words))

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "DictionaryQuery(words={0})".format(len(self))

    def __str__(self):
        return "Query from dictionary: [{0}]".format(
            ", ".join(word for word in self.words))

    def filter_by_anagram(self, term):
        """
        Generate all anagrams of a certain word.
        """
        result = []
        freq_term = Counter(term)
        for word, freq_word in self.words.items():
            if freq_term == freq_word:
                result.append(word)
        return DictionaryQuery(result)

    def filter_by_length(self, start, end=None):
        """
        Generate a list of words with a certain length.
        """
        if end is None:
            end = start
        result = []
        for word in self.words:
            if start <= len(word) <= end:
                result.append()

    def filter_from_string(self, string):
        """
        Generate a list of words contained in a string.
        """
        result = []
        freq_string = Counter(string)
        for word, freq_word in self.words.items():
            if all(freq_string[x] >= freq_word[x] for x in freq_word):
                result.append(word)
        return DictionaryQuery(result)

    def minimal_string(self):
        """
        Generate the minimal string that contains all words in the list.
        """
        minimal_freq = reduce(union, self.words.values())
        return ''.join(sorted(minimal_freq.elements()))

    def random(self, n=1):
        """
        Generate a random list of words.
        """
        return DictionaryQuery([random.choice(list(self.words)) for _ in range(n)])
