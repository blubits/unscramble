"""

:Author:     Jose Enrico Salinas
:Version:    v20181013
"""

import unittest
from engine.dictionary import Dictionary

class Test_TestDictionary(unittest.TestCase):

    def test_contains(self):
        self.dictionary = Dictionary("dictionary.txt")
        self.assertEqual("aardvark" in self.dictionary, True)
        self.assertEqual("bread" in self.dictionary, True)
        self.assertEqual("wersfdsf" in self.dictionary, False)

if __name__ == '__main__':
    unittest.main()