# Problem: Minimum Size Subarray Sum
# Description: Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a contiguous subarray of which the sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Finds the minimal length of a contiguous subarray of which the sum is greater than or equal to target.

        :param target: int, the target sum.
        :param nums: List[int], the list of positive integers.
        :return: int, the minimal length of the subarray or 0 if not found.
        """
        i = 0                     # Right pointer for the sliding window
        j = 0                     # Left pointer for the sliding window
        lens = float('inf')       # Initialize length of the subarray to infinity
        sums = 0                  # Initialize sum of the current window
        
        while(i < len(nums)):     # Expand the right pointer
            sums += nums[i]       # Add the current element to the sum
            i += 1                # Move the right pointer
            while sums >= target: # Shrink the window from the left
                lens = min(lens, i - j)  # Update the minimum length
                sums -= nums[j]   # Subtract the leftmost element from the sum
                j += 1            # Move the left pointer
                
        return lens if lens != float('inf') else 0  # Return the result

# Time Complexity: O(n), where n is the length of the nums array, as we iterate through the array once.
# Space Complexity: O(1), since we are using a fixed number of variables.

# Example usage:
# solution = Solution()
# print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))  # Expected output: 2
# print(solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))  # Expected output: 0
