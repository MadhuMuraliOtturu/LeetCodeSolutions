# Problem: Ways to Split Array Into Two Parts
# Description:
# You are given an integer array `nums` of length `n`.
# You need to count the number of ways to split the array into two non-empty 
# parts such that the sum of the left part is greater than or equal to the sum 
# of the right part.
#
# Example:
# Input: nums = [10, 4, -8, 7]
# Output: 2
#
# Explanation:
# - Split at index 0: Left = [10], Right = [4, -8, 7], Not valid.
# - Split at index 1: Left = [10, 4], Right = [-8, 7], Valid.
# - Split at index 2: Left = [10, 4, -8], Right = [7], Valid.
# There are 2 valid ways to split the array.
#
# Constraints:
# - 2 <= len(nums) <= 10^5
# - -10^5 <= nums[i] <= 10^5

from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        Counts the number of valid ways to split the array into two non-empty 
        parts such that the sum of the left part is greater than or equal 
        to the sum of the right part.

        Args:
            nums (List[int]): The input array of integers.

        Returns:
            int: Number of valid splits.
        """
        count = 0
        right_sum = 0
        left_sum = sum(nums)
        
        for i in range(len(nums) - 1):
            right_sum += nums[i]
            left_sum -= nums[i]
            if right_sum >= left_sum:
                count += 1
        
        return count

# Time Complexity: O(N), where N is the number of elements in the array.
# Space Complexity: O(1), as no additional space is used.
