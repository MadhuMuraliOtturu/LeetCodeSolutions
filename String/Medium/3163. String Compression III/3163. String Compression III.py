# Problem: Compressed String
# Description:
# Given a string `word`, compress it by counting consecutive characters and storing them in the format of
# "<count><character>". For any consecutive character sequence greater than 9, reset the count to 1 for the next
# occurrence.
#
# Example:
# Input: word = "aaabbccccdd"
# Output: "3a2b4c2d"
# Explanation: Compressing "aaabbccccdd" gives "3a2b4c2d".
#
# Constraints:
# - `word` consists of lowercase English letters only.
# - 1 <= len(word) <= 100.

class Solution:
    """
    Solution class to generate a compressed version of the given string by counting consecutive characters up to a max
    count of 9 per character.
    
    :param word: str - The input string to be compressed.
    :return: str - Compressed version of the input string.
    """
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        while i < len(word):
            ch = word[i]
            co = 0
            while i < len(word) and word[i] == ch and co < 9:
                co += 1
                i += 1
            comp += str(co) + ch
        return comp

# Time Complexity: O(n) - where n is the length of `word`. Each character is processed once.
# Space Complexity: O(n) - for storing the compressed string result.

# Example usage:
# solution = Solution()
# print(solution.compressedString("aaabbccccdd"))  # Output: "3a2b4c2d"
