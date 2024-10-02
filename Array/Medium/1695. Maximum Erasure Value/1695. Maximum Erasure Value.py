# Problem: Maximum Erasure Value
# Description:
# Given an array `nums` of positive integers, the task is to find the maximum sum of any subarray containing unique elements.
# A subarray is a contiguous segment of the array. We need to calculate the maximum sum of such a subarray where all elements are distinct.

from typing import List, Dict

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Finds the maximum sum of a subarray that contains only unique elements.
        
        :param nums: List[int], the input array of positive integers.
        :return: int, the maximum sum of a subarray containing unique elements.
        """
        maxi = 0  # To store the maximum sum of any subarray
        co = 0  # Current sum of the sliding window
        d: Dict[int, int] = {}  # Dictionary to track the count of elements in the current window
        left = 0  # Left pointer of the sliding window
        right = 0  # Right pointer of the sliding window
        n = len(nums)
        
        # Iterate over the array using a sliding window approach
        while right < n:
            if nums[right] not in d:
                d[nums[right]] = 1  # Add the current element to the dictionary
                co += nums[right]  # Add its value to the current sum
            else:
                # If the element is already in the window, shrink the window from the left
                while nums[right] in d and d[nums[right]] > 0:
                    d[nums[left]] -= 1
                    co -= nums[left]  # Subtract the leftmost element from the current sum
                    if d[nums[left]] == 0:
                        del d[nums[left]]  # Remove the element if its count reaches 0
                    left += 1
                d[nums[right]] = 1  # Add the current element after adjusting the window
                co += nums[right]  # Add its value to the current sum

            maxi = max(co, maxi)  # Update the maximum sum found
            right += 1
        
        return maxi  # Return the maximum sum of unique subarrays

# Time Complexity: O(n), where `n` is the length of the input array `nums`. Each element is processed once by both the left and right pointers.
# Space Complexity: O(n), for storing the count of elements in the sliding window using a dictionary.

# Example usage:
# solution = Solution()
# print(solution.maximumUniqueSubarray([4, 2, 4, 5, 6]))  # Expected output: 17 (subarray: [2, 4, 5, 6])
# print(solution.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))  # Expected output: 8 (subarray: [5, 2, 1])
