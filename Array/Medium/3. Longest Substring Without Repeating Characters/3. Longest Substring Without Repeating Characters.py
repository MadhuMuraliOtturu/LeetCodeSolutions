# Problem: Longest Substring Without Repeating Characters
# Description: Given a string `s`, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Returns the length of the longest substring without repeating characters.

        :param s: str, input string.
        :return: int, length of the longest substring without repeating characters.
        """
        l = set()  # Set to store unique characters
        i = 0      # Right pointer
        co = 0     # Current length of substring
        maxi = 0   # Maximum length of substring found
        j = 0      # Left pointer
        
        while i < len(s):
            if s[i] not in l:  # If character is not in the set
                l.add(s[i])    # Add character to set
                co += 1        # Increase current length
                maxi = max(maxi, co)  # Update maximum length
                i += 1         # Move right pointer
            else:  # If character is already in the set
                l.remove(s[j])  # Remove leftmost character
                j += 1          # Move left pointer
                co -= 1         # Decrease current length
        
        return maxi  # Return maximum length

# Time Complexity: O(n), where n is the length of the input string. Each character is processed at most twice.
# Space Complexity: O(min(n, m)), where m is the size of the character set.

# Example usage:
# solution = Solution()
# print(solution.lengthOfLongestSubstring("abcabcbb"))  # Expected output: 3 (substring "abc")
# print(solution.lengthOfLongestSubstring("bbbbb"))     # Expected output: 1 (substring "b")
# print(solution.lengthOfLongestSubstring("pwwkew"))    # Expected output: 3 (substring "wke")
