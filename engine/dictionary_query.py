"""
A query on a dictionary.

:Author:     Maded Batara III
:Version:    v20181013
"""

from collections import Counter, defaultdict
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

    def __eq__(self, other):
        if isinstance(other, list):
            return other == list(self)
        elif isinstance(other, DictionaryQuery):
            return list(other) == list(self)
        else:
            return False

    def __iter__(self):
        return iter(sorted(self.words))

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "DictionaryQuery(words={0})".format(len(self))

    def __str__(self):
        return "Query from dictionary: [{0}]".format(
            ", ".join(word for word in self.words))

    def choice(self):
        """
        Selects a random word.
        """
        return random.choice(list(self.words))

    def filter_by_anagram(self, term):
        """
        Generates all anagrams of a certain word.
        """
        result = []
        freq_term = Counter(term)
        for word, freq_word in self.words.items():
            if freq_term == freq_word:
                result.append(word)
        return DictionaryQuery(result)

    def filter_by_length(self, start, end=None):
        """
        Generates a list of words with a certain length.
        """
        if end is None:
            end = start
        result = []
        for word in self.words:
            if start <= len(word) <= end:
                result.append(word)
        return DictionaryQuery(result)

    def filter_from_string(self, string):
        """
        Generates a list of words contained in a string.
        """
        result = []
        freq_string = Counter(string)
        for word, freq_word in self.words.items():
            if all(freq_string[x] >= freq_word[x] for x in freq_word):
                result.append(word)
        return DictionaryQuery(result)

    def group_by_length(self):
        """
        Groups a list of words by length.
        """
        grouping = defaultdict(list)
        for word in self.words:
            key = len(word)
            grouping[key].append(word)
        for key in grouping:
            grouping[key].sort()
        return dict(grouping)

    def minimal_string(self):
        """
        Generates the minimal string that contains all words in the list.
        """
        minimal_freq = reduce(union, self.words.values())
        return ''.join(sorted(minimal_freq.elements()))

    def random(self, n=1):
        """
        Generates a random list of words.
        """
        return DictionaryQuery([random.choice(list(self.words)) for _ in range(n)])
