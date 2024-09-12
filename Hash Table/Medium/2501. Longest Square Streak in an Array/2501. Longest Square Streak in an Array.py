# Problem: Longest Square Streak in an Array
# Description: Given an array of integers, find the length of the longest sequence where each number 
# is the square of the previous one. If no such sequence exists, return -1.

import math

class Solution(object):
    def longestSquareStreak(self, nums):
        """
        Finds the longest sequence where each number is the square of the previous one in the array.
        
        :param nums: List of integers.
        :return: Integer, the length of the longest square streak or -1 if no such streak exists.
        """
        nums = set(nums)
        long = 0
        
        for i in nums:
            val = i
            count = 0
            
            # Check if `sqrt(val)` is not in the set, meaning `val` is the start of a sequence
            if math.sqrt(val) not in nums:
                while val in nums:
                    count += 1
                    val = val**2
            
            long = max(long, count)
        
        # Return -1 if no sequence longer than 1 was found, otherwise return the longest streak
        return long if long > 1 else -1

# Time Complexity: O(n), where n is the number of unique elements in `nums`. We iterate over each element 
# and check for square streaks.
# Space Complexity: O(n), where n is the space required to store the set of unique elements from `nums`.

# Example usage:
# solution = Solution()
# nums = [4, 2, 16, 256]
# print(solution.longestSquareStreak(nums))  # Expected output: 4 (sequence: 2, 4, 16, 256)
