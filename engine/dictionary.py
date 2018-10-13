"""
A dictionary of words.

:Author:     Maded Batara III
:Version:    v20181010
"""

from collections import Counter

if __name__ != "__main__":
    from .dictionary_query import DictionaryQuery
else:
    from dictionary_query import DictionaryQuery

class Dictionary(DictionaryQuery):

    def __init__(self, filename):
        with open(filename) as dictionary_file:
            self.words = {
                word: Counter(word)
                for word in dictionary_file.read().splitlines()
            }

    def __repr__(self):
        return "Dictionary(words={0})".format(len(self))

    def __str__(self):
        return "Dictionary with {0} entries".format(len(self))

if __name__ == "__main__":
    dictionary = Dictionary("dictionary.txt")
    print(dictionary)
    print("bread" in dictionary)
    print(dictionary.filter_by_anagram("tar"))
    print(dictionary.filter_from_string("tnettenba"))
