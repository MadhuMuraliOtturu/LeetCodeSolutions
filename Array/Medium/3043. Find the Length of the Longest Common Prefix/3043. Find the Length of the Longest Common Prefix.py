# Problem: Longest Common Prefix in Arrays
# Description: Given two arrays of integers, find the length of the longest common prefix that exists in both arrays.
# The common prefix is defined as the common digit sequences starting from the highest power of ten in the integer.

from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        This function finds the length of the longest common prefix in two arrays of integers.

        :param arr1: List[int] - First array of integers
        :param arr2: List[int] - Second array of integers
        :return: int - Length of the longest common prefix found
        """
        d1 = {}
        d2 = {}
        
        # Helper function to calculate prefixes and store them in a dictionary
        def helper(num, d):
            pow = 0
            while 10 ** pow <= num:
                r = str(num // (10 ** pow))  # Extract the prefix at current power of ten
                if r not in d:
                    d[r] = 1
                else:
                    d[r] += 1
                pow += 1

        # Populate the prefix dictionaries for both arrays
        for i in arr1:
            helper(i, d1)
        for j in arr2:
            helper(j, d2)

        # Find the longest common prefix
        maxi = 0 
        for val in d1:
            if val in d2:  # Check if the prefix exists in both dictionaries
                x = len(val)
                if d1[val] > 0 and d2[val] > 0:
                    maxi = max(maxi, x)

        return maxi

# Time Complexity: O(n * log(m)), where n is the length of the arrays and m is the largest number in the arrays. 
# This is due to breaking down each number into its prefix by powers of ten.
# Space Complexity: O(n * log(m)), where we store the prefixes in two dictionaries.
#
# Example Usage:
# solution = Solution()
# print(solution.longestCommonPrefix([12345, 67890], [123, 678]))  # Output: 3
# print(solution.longestCommonPrefix([345, 678], [345, 6789]))  # Output: 3
