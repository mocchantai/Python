import unittest
from reverse_words import reverseWords

class TestReverseWords(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(reverseWords("the sky is blue"), "blue is sky the")
        self.assertEqual(reverseWords("  hello world  "), "world hello")
        self.assertEqual(reverseWords("a good   example"), "example good a")

    def test_edge_cases(self):
        self.assertEqual(reverseWords(""), "")
        self.assertEqual(reverseWords("a"), "a")
        self.assertEqual(reverseWords("  a  "), "a")

if __name__ == "__main__":
    unittest.main()