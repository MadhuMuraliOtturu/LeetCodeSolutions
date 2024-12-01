# Problem: Check If N and Its Double Exist
# Description:
# Given an array `arr` of integers, return `True` if there exist two integers `N` and `M` such that:
# - `N` is double the value of `M` (i.e., `N = 2 * M`).
# - Both `N` and `M` are elements in the array.
# Otherwise, return `False`.
#
# Example:
# Input: arr = [10, 2, 5, 3]
# Output: True
# Explanation: 10 is double the value of 5.
#
# Constraints:
# - 2 <= arr.length <= 500
# - -10^3 <= arr[i] <= 10^3

from typing import List

class Solution:
    """
    Checks if there exist two numbers N and M such that N = 2 * M in the given array.
    
    :param arr: List[int] - The input array of integers.
    :return: bool - True if such numbers exist, otherwise False.
    """
    def checkIfExist(self, arr: List[int]) -> bool:
        z = arr.count(0)  # Count the occurrences of 0 in the array
        s = set(arr)      # Convert the array into a set for faster lookups
        for i in arr:
            x = 2 * i
            # Check if double exists, ensuring 0 is handled correctly
            if x in s and (x != 0 or z > 1):
                return True
        return False

# Time Complexity: O(n) - Iterates through the array and uses O(1) set lookups.
# Space Complexity: O(n) - Space required for the set `s`.

# Example usage:
# solution = Solution()
# print(solution.checkIfExist([10, 2, 5, 3]))  # Output: True
# print(solution.checkIfExist([7, 1, 14, 11])) # Output: True
# print(solution.checkIfExist([3, 1, 7, 11]))  # Output: False
