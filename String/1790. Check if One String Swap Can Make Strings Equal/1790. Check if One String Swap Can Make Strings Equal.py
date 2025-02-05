# Problem: Check if One String Swap Can Make Strings Equal
# Description:
# Given two strings `s1` and `s2` of equal length, determine if they can be made 
# equal by swapping exactly one pair of characters in `s1`.
#
# Example:
# Input:
# s1 = "bank"
# s2 = "kanb"
# Output: True
#
# Explanation:
# Swapping 'b' and 'k' in `s1` results in `s2`.
#
# Constraints:
# - 1 <= len(s1), len(s2) <= 100
# - `s1` and `s2` consist only of lowercase English letters.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Determines if one string swap in s1 can make it equal to s2.

        Args:
            s1 (str): First string.
            s2 (str): Second string.

        Returns:
            bool: True if s1 can be made equal to s2 by one swap, else False.
        """
        d1 = {}
        d2 = {}
        diff_count = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_count += 1

            d1[s1[i]] = d1.get(s1[i], 0) + 1
            d2[s2[i]] = d2.get(s2[i], 0) + 1

        return (diff_count == 2 or diff_count == 0) and d1 == d2

# Time Complexity: O(N), where N is the length of the strings.
# Space Complexity: O(1), as the dictionary stores at most 26 characters.
