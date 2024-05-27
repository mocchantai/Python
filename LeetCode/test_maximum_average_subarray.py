import unittest
from maximum_average_subarray import Solution

class TestFindMaxAverage(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        nums = [1,12,-5,-6,50,3]
        k = 4
        self.assertEqual(self.solution.findMaxAverage(nums, k), 12.75)

    def test_edge_cases(self):
        nums = [5]
        k = 1
        self.assertEqual(self.solution.findMaxAverage(nums, k), 5.0)
    
    def test_negative_average(self):
        nums = [-1]
        k = 1
        self.assertEqual(self.solution.findMaxAverage(nums, k), -1.0)

if __name__ == '__main__':
    unittest.main()
