"""
A query on a dictionary.

:Author:     Maded Batara III
:Author:     Jose Enrico Salinas
:Version:    v20181020
"""

from collections import Counter, defaultdict
from functools import reduce
from operator import or_ as union
import random

class DictionaryQuery:
    """A query from a dictionary.

    The DictionaryQuery class is a general-purpose class supporting
    relevant queries from a list of words.
    """

    def __init__(self, words):
        """
        Initializes a DictionaryQuery.

        Args:
            words (list of str): A list of words to add to the query.
        """
        self.words = {
            word: Counter(word)
            for word in words
        }

    def __contains__(self, word):
        """Implements word in DictionaryQuery."""
        return word in self.words

    def __eq__(self, other):
        """Implements DictionaryQuery == other."""
        if isinstance(other, list):
            return other == list(self)
        elif isinstance(other, DictionaryQuery):
            return list(other) == list(self)
        else:
            return False

    def __iter__(self):
        """Implements iter(DictionaryQuery)."""
        return iter(sorted(self.words))

    def __len__(self):
        """Implements len(DictionaryQuery)."""
        return len(self.words)

    def __repr__(self):
        """Implements repr(DictionaryQuery)."""
        return "DictionaryQuery(words={0})".format(len(self))

    def __str__(self):
        """Implements str(DictionaryQuery)."""
        return "Query from dictionary: [{0}]".format(
            ", ".join(word for word in self.words))

    def choice(self):
        """
        Selects a random word.

        Returns:
            str: A random word from the query.
        """
        return random.choice(list(self.words))

    def filter_by_anagram(self, term):
        """
        Generates all anagrams of a certain word.

        >> > dq = DictionaryQuery("rat", "tar", "art", "tarot", "carrot")
        >> > for word in dq.filter_by_anagram("art"):
        ... print(word)
        art
        rat
        tar

        Args:
            term(str): Term to find the anagrams of.

        Returns:
            DictionaryQuery: List of words which are anagrams of term.
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

        Args:
            start(int): Minimum length of a word in the new list.
            end(int, optional): Maximum length of a word in the new list.

        Returns:
            DictionaryQuery: A list of words with length at least equal to
                start. If end is specified, the list does not include words
                with lengths greater than end.
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

        Args:
            string(str): String to find words in.

        Returns:
            DictionaryQuery: A list of words whose letters are contained
                in the string.
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

        Returns:
            dict: The words in the query, grouped by length.
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

        >> > dq = DictionaryQuery(["apple", "banana"])
        >> > dq.minimal_string()
        aaabelnnpp

        Returns:
            str: The minimal - length string that satisfies the property that
                the letters of all words in the query are in it.
        """
        minimal_freq = reduce(union, self.words.values())
        return ''.join(sorted(minimal_freq.elements()))

    def random(self, n=1):
        """
        Generates a random list of words.

        Args:
            n(int, optional): Number of words to select from the query.

        Returns:
            DictionaryQuery: A random selection of n words already in the query.
        """
        return DictionaryQuery([random.choice(list(self.words)) for _ in range(n)])

    def random_string(self, n=1):
        """Generates the minimal string from a list of random words."""
        return self.random(n=n).minimal_string()
