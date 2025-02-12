# Problem: Maximum Sum of Two Numbers with Equal Digit Sum
# Description:
# Given a list of integers, find the maximum sum of two numbers that have the same digit sum.
# If no such pair exists, return -1.
#
# Example:
# Input:
# nums = [51, 71, 17, 42]
# Output: 93
#
# Explanation:
# - Digit sum of 51 = 5 + 1 = 6
# - Digit sum of 71 = 7 + 1 = 8
# - Digit sum of 17 = 1 + 7 = 8
# - Digit sum of 42 = 4 + 2 = 6
# - The pairs with the same digit sum are:
#   - (51, 42) with sum = 51 + 42 = 93
#   - (71, 17) with sum = 71 + 17 = 88
# - The maximum sum is 93.
#
# Constraints:
# - 1 <= len(nums) <= 10^5
# - 1 <= nums[i] <= 10^9

from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """
        Finds the maximum sum of two numbers with the same digit sum.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The maximum sum of two numbers with the same digit sum, or -1 if no such pair exists.
        """
        digit_sum_map = {}  # Stores digit sum as key and numbers as values
        max_sum = -1

        for num in nums:
            original_num = num
            digit_sum = 0

            while num > 0:
                digit_sum += num % 10
                num //= 10

            if digit_sum not in digit_sum_map:
                digit_sum_map[digit_sum] = [original_num]
            else:
                max_sum = max(max_sum, original_num + max(digit_sum_map[digit_sum]))
                digit_sum_map[digit_sum].append(original_num)

        return max_sum

# Time Complexity: O(N log M), where N is the number of elements in nums and log M is the digit sum computation.
# Space Complexity: O(N), as we store mappings of digit sums.
