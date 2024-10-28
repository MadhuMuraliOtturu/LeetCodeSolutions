# Problem: Longest Square Streak in Array
# Description:
# Given an array of integers `nums`, the goal is to find the longest square streak in the array.
# A square streak is defined as a sequence of integers `x, x^2, (x^2)^2, ...` such that each element
# in the sequence is present in the array `nums`. The task is to return the length of the longest
# square streak or -1 if there is no valid streak of length >= 2.
#
# Example:
# Input: nums = [2, 4, 16, 256]
# Output: 4
# Explanation: The longest square streak is [2, 4, 16, 256].
#
# Constraints:
# - 1 <= len(nums) <= 10^5
# - 1 <= nums[i] <= 10^5

from typing import List

class Solution:
    """
    Solution for finding the longest square streak in an array.
    
    :param nums: List[int] - List of integers to analyze for square streaks.
    :return: int - The length of the longest square streak, or -1 if no streak of length >= 2 exists.
    """
    def longestSquareStreak(self, nums: List[int]) -> int:
        maxi = 0
        s = set(nums)  # Use a set for efficient lookups
        
        for num in s:  
            co = 0
            x = num
            
            while x in s:  
                co += 1
                x = x ** 2  # Move to the next square
            
            maxi = max(co, maxi)  
        
        return maxi if maxi >= 2 else -1

# Time Complexity: O(n * log(max(nums))) - For each element, squares are checked up to log max possible squares.
# Space Complexity: O(n) - Storing elements in a set.

# Example usage:
# solution = Solution()
# print(solution.longestSquareStreak([2, 4, 16, 256]))  # Output: 4
