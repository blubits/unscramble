import unittest

from engine.dictionary import Dictionary

class Test_TestDictionary(unittest.TestCase):
    
    def test_contains(self):
        self.dictionary = Dictionary("dictionary.txt")
        self.assertEquals("aardvark" in self.dictionary, True)
        self.assertEquals("bread" in self.dictionary, True)
        self.assertEquals("wersfdsf" in self.dictionary, False)

if __name__ == '__main__':
    unittest.main()