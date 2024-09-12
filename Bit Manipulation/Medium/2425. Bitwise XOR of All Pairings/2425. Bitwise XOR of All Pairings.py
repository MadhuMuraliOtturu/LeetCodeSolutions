# Problem: XOR of All Numbers in Two Lists
# Description: Given two lists of integers `nums1` and `nums2`, compute the XOR of all integers
# in `nums1` and `nums2` based on their lengths. The result depends on whether the lengths of the lists are odd or even.

from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Computes the XOR of all integers in two lists based on their lengths.

        :param nums1: List[int], the first list of integers.
        :param nums2: List[int], the second list of integers.
        :return: Integer, the XOR result.
        """
        len1 = len(nums1)
        len2 = len(nums2)
        xor1 = nums1[0]
        for i in range(1, len(nums1)):
            xor1 ^= nums1[i]
        xor2 = nums2[0]
        for j in range(1, len(nums2)):
            xor2 ^= nums2[j]
        if len1 % 2 == 1 and len2 % 2 == 1:
            return xor1 ^ xor2
        elif len1 % 2 == 1:
            return xor2
        elif len2 % 2 == 1:
            return xor1
        return 0

## Time Complexity: O(N + M), where N is the number of elements in `nums1` and M is the number of elements in `nums2`.
## Space Complexity: O(1), constant space used.

# Example usage:
# solution = Solution()
# print(solution.xorAllNums([1, 2, 3], [3, 4]))  
# Expected output: 7, based on the XOR operations described.
