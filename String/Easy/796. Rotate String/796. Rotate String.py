# Problem: Rotate String
# Description:
# Given two strings, `s` and `goal`, determine if `s` can be rotated to become `goal`.
# A string rotation is defined by taking characters from the beginning and moving them to the end.
#
# Example:
# Input: s = "abcde", goal = "cdeab"
# Output: True
# Explanation: Rotating "abcde" to the right by two positions results in "cdeab", which matches `goal`.
#
# Constraints:
# - `s` and `goal` consist of lowercase English letters only.
# - 1 <= len(s), len(goal) <= 100.

class Solution(object):
    """
    Solution class to check if one string can be rotated to become another string.
    
    :param s: str - Original string to be checked for rotation.
    :param goal: str - Target string to compare with rotated `s`.
    :return: bool - True if `s` can be rotated to match `goal`, False otherwise.
    """
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        d = s + s
        return d.find(goal) != -1

# Time Complexity: O(n) - where n is the length of `s`. Checking substring and concatenation are linear operations.
# Space Complexity: O(n) - for the concatenated string `d`.

# Example usage:
# solution = Solution()
# print(solution.rotateString("abcde", "cdeab"))  # Output: True
