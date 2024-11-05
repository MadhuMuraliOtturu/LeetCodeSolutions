# Problem: Minimum Changes
# Description:
# Given a binary string `s`, the task is to count the minimum number of changes required
# to make all adjacent characters different. The string `s` has an even length, and each 
# character is either '0' or '1'. The changes involve flipping a character from '0' to '1' 
# or from '1' to '0' as needed.
#
# Example:
# Input: s = "0101"
# Output: 0
# Explanation: The string "0101" already has alternating characters, so no changes are needed.
#
# Input: s = "0011"
# Output: 1
# Explanation: Changing one '0' to '1' or one '1' to '0' results in alternating characters.
#
# Constraints:
# - `s` consists only of '0' and '1' characters.
# - The length of `s` is even.

class Solution:
    """
    Solution class to calculate the minimum number of changes required to make
    a binary string have alternating characters.
    
    :param s: str - The input binary string.
    :return: int - Minimum number of changes needed.
    """
    def minChanges(self, s: str) -> int:
        i = 0
        co = 0
        while i < len(s):
            if s[i] == s[i + 1]:
                pass  # No action required if consecutive characters are the same
            else:
                co += 1  # Increment count if characters alternate as expected
            i += 2  # Move to the next pair
        return co

# Time Complexity: O(n) - where n is the length of `s`, iterating once through `s` with steps of 2.
# Space Complexity: O(1) - only a constant amount of space is used.

# Example usage:
# solution = Solution()
# print(solution.minChanges("0101"))  # Output: 0
# print(solution.minChanges("0011"))  # Output: 1
