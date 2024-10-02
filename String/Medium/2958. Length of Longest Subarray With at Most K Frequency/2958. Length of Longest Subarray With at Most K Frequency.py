# Problem: Maximum Length of Subarray with Elements Appearing No More Than K Times
# Description:
# Given an array of integers `nums` and an integer `k`, the task is to find the maximum length of a contiguous subarray
# where each element appears at most `k` times.

from typing import List, Dict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        Finds the maximum length of a subarray where each element appears at most `k` times.

        :param nums: List[int], the input array of integers.
        :param k: int, the maximum number of occurrences allowed for any element.
        :return: int, the length of the longest subarray that meets the condition.
        """
        d: Dict[int, int] = {}  # Dictionary to track the count of each element in the current window
        left = 0  # Left pointer of the sliding window
        right = 0  # Right pointer of the sliding window
        n = len(nums)
        lens = 0  # To store the maximum length of valid subarrays
        
        # Iterate over the array using a sliding window
        while right < n:
            if nums[right] not in d:
                d[nums[right]] = 0
            d[nums[right]] += 1  # Add the current element to the window
            
            # If the element count is within the allowed limit, calculate the maximum length
            if d[nums[right]] <= k:
                lens = max(lens, right - left + 1)
            
            # If the count of any element exceeds k, shrink the window from the left
            while d[nums[right]] > k:
                d[nums[left]] -= 1
                if d[nums[left]] == 0:
                    del d[nums[left]]  # Remove element when its count reaches 0
                left += 1
            
            right += 1  # Expand the window from the right
        
        return lens

# Time Complexity: O(n), where `n` is the length of the input array `nums`. Each element is processed once by both the left and right pointers.
# Space Complexity: O(n), for storing the count of elements in the sliding window using a dictionary.

# Example usage:
# solution = Solution()
# print(solution.maxSubarrayLength([1, 2, 2, 1, 3], 2))  # Expected output: 4
# print(solution.maxSubarrayLength([1, 2, 3, 1, 2, 3, 4], 1))  # Expected output: 4
