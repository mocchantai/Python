import unittest
from maximum_number_of_vowels import Solution

class TestMaxVowels(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        s = "abciiidef"
        k = 3
        self.assertEqual(self.solution.maxVowels(s, k), 3)

        s = "aeiou"
        k = 2
        self.assertEqual(self.solution.maxVowels(s, k), 2)

        s = "leetcode"
        k = 3
        self.assertEqual(self.solution.maxVowels(s, k), 2)
    
    def test_edge_cases(self):
        s = "a"
        k = 1
        self.assertEqual(self.solution.maxVowels(s, k), 1)

        s = "ababa"
        k = 1
        self.assertEqual(self.solution.maxVowels(s, k), 1)
    
    def tearDown(self):
        self.solution = None

if __name__ == "__main__":
    unittest.main()