# Problem: Count Fair Pairs
# Description:
# Given a sorted list of integers and a pair range [lower, upper], this function finds the count of pairs (i, j)
# such that i < j and lower <= nums[i] + nums[j] <= upper.
#
# Example:
# Input: nums = [1,2,3,4], lower = 3, upper = 6
# Output: 5
# Explanation: The fair pairs are (1, 2), (1, 3), (2, 3), (1, 4), and (2, 4).
#
# Constraints:
# - `1 <= len(nums) <= 10^5`
# - `-10^9 <= nums[i], lower, upper <= 10^9`

from typing import List

class Solution:
    """
    Solution class to count fair pairs within the given range.
    
    :param nums: List[int] - List of integers.
    :param lower: int - Lower bound for pair sums.
    :param upper: int - Upper bound for pair sums.
    :return: int - Count of fair pairs.
    """

    def left(self, nums: List[int], target: int) -> int:
        """Binary search to find the leftmost index where nums[index] >= target."""
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def right(self, nums: List[int], target: int) -> int:
        """Binary search to find the rightmost index where nums[index] <= target."""
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return right - 1

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """Count pairs with sum in the range [lower, upper]."""
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if upper - nums[i] < nums[i]:
                return count
            left = self.left(nums, lower - nums[i])
            right = self.right(nums, upper - nums[i])
            if i >= left:
                left = i + 1
            if right >= left:
                count += (right - left + 1)
        return count

# Time Complexity: O(n log n) - for sorting and binary searches.
# Space Complexity: O(1) - in-place sorting and counting.

# Example usage:
# solution = Solution()
# print(solution.countFairPairs([1,2,3,4], 3, 6))  # Output: 5
