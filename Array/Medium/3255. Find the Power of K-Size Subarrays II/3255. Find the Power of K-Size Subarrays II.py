# Problem: Generate Results Array Based on Consecutive Numbers (Optimized)
# Description:
# Given an array `nums` of integers and an integer `k`, this function checks every consecutive subarray of size `k`.
# If the elements in the subarray form consecutive integers (i.e., each element is exactly 1 more than the previous element),
# append the last element of that subarray to the result. If they are not consecutive, append `-1`.
# If `k` is 1, return the array itself, as each element individually forms a subarray of size 1.
# The goal is to return the final list of results.

from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """
        Generates a results array based on consecutive subarrays of length k.

        :param nums: List[int], the input array of integers.
        :param k: int, the length of the subarray to check for consecutive elements.
        :return: List[int], a list containing the last element of consecutive subarrays or -1 for non-consecutive subarrays.
        """
        if k == 1:
            return nums  # If k is 1, return the nums array directly.
        
        i = 1
        cons = 1  # Counter for consecutive numbers
        ans = []

        while i < len(nums):  # Iterate through the array
            if nums[i] - 1 == nums[i - 1]:  # Check if the current number is consecutive to the previous one
                cons += 1
            else:
                cons = 1  # Reset consecutive counter if not consecutive

            if i >= k - 1:  # Start forming the result after reaching the first subarray of length k
                if cons >= k:
                    ans.append(nums[i])  # Append the last element of the consecutive subarray
                else:
                    ans.append(-1)  # Append -1 if the subarray is not consecutive
            i += 1

        return ans  # Return the results array

# Time Complexity: O(n), where `n` is the length of the input array `nums`.
# The array is traversed once, making this approach linear in terms of time.
# Space Complexity: O(n), where `n` is the size of the result list.

# Example usage:
# solution = Solution()
# print(solution.resultsArray([1, 2, 3, 5, 6, 7, 8], 3))  # Expected output: [3, -1, -1, 7, 8]
# print(solution.resultsArray([1, 2, 3, 4, 5], 2))  # Expected output: [2, 3, 4, 5]
# print(solution.resultsArray([10, 20, 30, 40], 2))  # Expected output: [-1, -1, -1]
