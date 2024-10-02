# Problem: Generate Results Array Based on Consecutive Numbers
# Description:
# Given an array `nums` of integers and an integer `k`, you need to check every consecutive subarray of size `k`.
# If the elements in the subarray form consecutive integers (i.e., each element is exactly 1 more than the previous element),
# append the last element of that subarray to the result. If they are not consecutive, append `-1`.
# Return the final list of results.

from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """
        Generates a results array based on consecutive subarrays of length k.

        :param nums: List[int], the input array of integers.
        :param k: int, the length of the subarray to check for consecutive elements.
        :return: List[int], a list containing the last element of consecutive subarrays or -1 for non-consecutive subarrays.
        """
        n = len(nums)
        ans = []
        left = 0
        
        while left < n - k + 1:  # Iterate through each possible subarray of length k
            check = True
            for right in range(left + 1, left + k):
                if nums[right - 1] + 1 != nums[right]:  # Check if elements are consecutive
                    check = False
                    break
            if check:
                ans.append(nums[left + k - 1])  # Append the last element if consecutive
            else:
                ans.append(-1)  # Append -1 if not consecutive
            left += 1

        return ans  # Return the results array

# Time Complexity: O(n * k), where `n` is the length of the input array `nums` and `k` is the length of the subarray.
# This is because, for each subarray of length `k`, we perform `k` comparisons.
# Space Complexity: O(n), where `n` is the size of the input list and the result list.

# Example usage:
# solution = Solution()
# print(solution.resultsArray([1, 2, 3, 5, 6, 7, 8], 3))  # Expected output: [3, -1, -1, 7, 8]
# print(solution.resultsArray([1, 2, 3, 4, 5], 2))  # Expected output: [2, 3, 4, 5]
# print(solution.resultsArray([10, 20, 30, 40], 2))  # Expected output: [-1, -1, -1]
