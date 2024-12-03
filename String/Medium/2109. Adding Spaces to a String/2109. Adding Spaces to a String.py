# Problem: Add Spaces to a String
# Description:
# You are given a string `s` and a list of indices `spaces`. Your task is to insert a space at each of the given indices in the string `s`.
# Return the resulting string after adding all the spaces.
#
# Example:
# Input: s = "leetcodeisfun", spaces = [8, 4]
# Output: "leet code is fun"
# Explanation:
# Insert a space at index 4: "leet codeisfun"
# Insert a space at index 8: "leet code is fun"
#
# Constraints:
# - 1 <= s.length <= 3 * 10^5
# - 1 <= len(spaces) <= 3 * 10^5
# - The values in `spaces` are sorted in strictly increasing order.
# - All characters in `s` are lowercase English letters.

from typing import List

class Solution:
    """
    Adds spaces to a given string at specified indices.
    
    :param s: str - The input string to modify.
    :param spaces: List[int] - A list of indices where spaces should be added.
    :return: str - The modified string with spaces inserted at the specified indices.
    """
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i = 0
        spaces = set(spaces)  # Convert the list to a set for efficient lookup
        new_s = []
        
        # Iterate over the string to construct the result with spaces
        while i < len(s):
            if i + 1 in spaces:  # Check if a space needs to be added after the current character
                new_s.append(s[i])
                new_s.append(" ")
            else:
                new_s.append(s[i])
            i += 1
        
        # Add a leading space if index 0 is in spaces
        if 0 in spaces:
            new_s = [" "] + new_s
        
        return "".join(new_s)

# Time Complexity: O(n), where n is the length of the string `s`.
# Space Complexity: O(n), where n is the size of the resulting string.

# Example usage:
# solution = Solution()
# print(solution.addSpaces("leetcodeisfun", [8, 4]))  # Output: "leet code is fun"
# print(solution.addSpaces("abc", [0]))             # Output: " abc"
