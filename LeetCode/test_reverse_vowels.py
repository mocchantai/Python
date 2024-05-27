import unittest
from reverse_vowels import reverseVowels

class TestReverseVowels(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(reverseVowels('hello'), 'holle')
        self.assertEqual(reverseVowels('leetcode'), 'leotcede')

    def test_edge_cases(self):
        self.assertEqual(reverseVowels('a'), 'a')  # Single character
        self.assertEqual(reverseVowels(''), '')  # Empty string
        self.assertEqual(reverseVowels('bcdfg'), 'bcdfg')  # No vowels
        self.assertEqual(reverseVowels('aeiou'), 'uoiea')  # All vowels

    def test_mixed_cases(self):
        self.assertEqual(reverseVowels('AaEeIiOoUu'), 'uUoOiIeEaA')  # Mixed case vowels
        self.assertEqual(reverseVowels('bAcE'), 'bEcA')  # Mixed case with consonants

    def test_repeated_vowels(self):
        self.assertEqual(reverseVowels('aabbccddeeff'), 'eebbccddaaff')  # Repeated vowels

if __name__ == '__main__':
    unittest.main()
