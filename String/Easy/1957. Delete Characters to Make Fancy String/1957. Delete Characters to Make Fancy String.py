# Problem: Fancy String Generator
# Description:
# Given a string `s`, the task is to ensure no three consecutive characters in `s` are the same.
# This function returns a modified string that satisfies this condition.
#
# Example:
# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation: The input "aaabaaaa" has consecutive characters that violate the rule. The result is adjusted to "aabaa".
#
# Constraints:
# - 1 <= len(s) <= 10^5
# - s consists only of lowercase English letters.

class Solution:
    """
    Solution class for generating a "fancy" string without three consecutive identical characters.
    
    :param s: str - Input string with potential consecutive characters.
    :return: str - Modified string with no three consecutive identical characters.
    """
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        s_list = list(s)
        j = 2

        for i in range(2, len(s)):
            if s_list[i] != s_list[j - 1] or s_list[i] != s_list[j - 2]:
                s_list[j] = s_list[i]
                j += 1

        return "".join(s_list[:j])

# Time Complexity: O(n) - Each character is checked once, where n is the length of the string.
# Space Complexity: O(n) - A list is created from the string for efficient modifications.

# Example usage:
# solution = Solution()
# print(solution.makeFancyString("aaabaaaa"))  # Output: "aabaa"
