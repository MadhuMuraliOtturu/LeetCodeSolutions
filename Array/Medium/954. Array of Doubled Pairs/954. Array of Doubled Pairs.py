# Problem: Can Reorder Array to Form Doubled Pairs
# Description:
# Given an array `arr` of integers, you are tasked with checking whether it is possible to reorder the array in such a way
# that for every element `x`, there is another element `y` such that `y = 2 * x`.
# Return `True` if it is possible to reorder the array as described, otherwise return `False`.

from typing import List
from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        """
        Determines if the array can be reordered such that for every element x, there is an element 2*x.
        
        :param arr: List[int], the input array of integers.
        :return: bool, True if the array can be reordered to form doubled pairs, False otherwise.
        """
        d = Counter(arr)  # Create a frequency counter for elements in arr
        for i in sorted(arr, key=abs):  # Sort the array by absolute values
            if d[i] == 0:  # If the current element is already used, continue
                continue
            if d[2 * i] == 0:  # If there's no 2*x counterpart, return False
                return False
            d[i] -= 1  # Use one occurrence of the current element
            d[2 * i] -= 1  # Use one occurrence of the 2*x element
        return True  # If all pairs are matched successfully, return True

# Time Complexity: O(n log n), where `n` is the length of the input array `arr`.
# The sorting operation takes O(n log n) time, and iterating through the array takes O(n) time.
# Space Complexity: O(n), due to the storage used by the Counter.

# Example usage:
# solution = Solution()
# print(solution.canReorderDoubled([3, 1, 3, 6]))  # Expected output: False
# print(solution.canReorderDoubled([4, -2, 2, -4]))  # Expected output: True
# print(solution.canReorderDoubled([1, 2, 4, 8]))  # Expected output: True
