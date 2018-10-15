"""

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

import unittest
from engine import Dictionary

class Test_TestDictionary(unittest.TestCase):

    dictionary = Dictionary("dictionary_test.txt")

    def test_contains(self):
        self.assertEqual("foo" in self.dictionary, True)
        self.assertEqual("bar" in self.dictionary, True)
        self.assertEqual("wersfdsf" in self.dictionary, False)

    def test_choice(self):
        self.assertEqual(self.dictionary.choice() in self.dictionary, True)
        self.assertEqual(self.dictionary.choice() in self.dictionary, True)
    
    def test_filter_by_anagram(self):
        self.assertEqual(list(self.dictionary.filter_by_anagram("bar")), ["arb", "bar", "rab"])

    def test_filter_by_length(self):
        self.assertEqual(list(self.dictionary.filter_by_length(start=3)), ["arb", "bar", "foo", "rab", "ree"])
        self.assertEqual(list(self.dictionary.filter_by_length(start=3, end=4)), ["arb", "bar", "baza", "foo", "rab", "ree"])

    def test_filter_from_string(self):
        self.assertEqual(list(self.dictionary.filter_from_string("arb")), ["arb", "bar", "rab"])
        self.assertEqual(list(self.dictionary.filter_from_string("oof")), ["foo"])

    def test_group_by_length(self):
        self.assertEqual(self.dictionary.group_by_length(), {3: ["arb", "bar", "foo", "rab", "ree"], 4: ["baza"]})

    def test_minimal_string(self):
        self.assertEqual(self.dictionary.minimal_string(), "aabeefoorz")

    def test_random(self):
        for word in list(self.dictionary.random()):
            self.assertEqual(word in self.dictionary, True)

if __name__ == '__main__':
    unittest.main()
