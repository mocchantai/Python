"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initial sum of the first k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Sliding window to find the maximum sum of k consecutive elements
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        return max_sum / k

if __name__ == "__main__":
    solution = Solution()
    
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(solution.findMaxAverage(nums, k))  # Output: 12.75

    nums = [0,4,0,3,2]
    k = 1
    print(solution.findMaxAverage(nums, k))  # Output: 4.0
    
    nums = [4,2,1,3,3]
    k = 2
    print(solution.findMaxAverage(nums, k))  # Output: 3.0
