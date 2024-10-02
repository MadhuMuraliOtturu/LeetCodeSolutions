# Problem: Longest Semi-Repetitive Substring
# Description:
# Given a string `s`, the function finds the length of the longest "semi-repetitive" substring.
# A substring is defined as "semi-repetitive" if it contains at most one adjacent pair of identical characters.
# The function returns the length of the longest such substring in `s`.

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        """
        Finds the length of the longest semi-repetitive substring in the given string.

        :param s: str, input string of characters.
        :return: int, the length of the longest semi-repetitive substring.
        """
        prev_pair = -1  # Track the previous pair of identical characters
        atmost = 1  # Allow at most one pair of identical characters
        i = 1  # Start checking from the second character
        n = len(s)
        co = 1  # Counter for the current substring length
        maxi = 1  # Maximum length of the semi-repetitive substring

        while i < n:
            if s[i - 1] == s[i]:  # Check if the current and previous characters form a pair
                if atmost > 0:
                    atmost -= 1  # Decrease the allowance for one pair
                    co += 1
                    i += 1
                    prev = i - 1  # Update the index of the last pair
                    maxi = max(maxi, co)  # Update the maximum length
                else:
                    i = prev + 1  # Reset the index to one character after the last pair
                    co = 1  # Reset the counter for the new substring
                    atmost = 1  # Reset the allowance for one pair
            else:
                co += 1  # Increment the substring length for non-pair characters
                maxi = max(maxi, co)  # Update the maximum length
                i += 1

        return maxi  # Return the maximum length of the semi-repetitive substring

# Time Complexity: O(n), where `n` is the length of the input string `s`.
# The string is traversed once, making the approach linear in terms of time.
# Space Complexity: O(1), as only a few extra variables are used, independent of the input size.

# Example usage:
# solution = Solution()
# print(solution.longestSemiRepetitiveSubstring("aabbcc"))  # Expected output: 2
# print(solution.longestSemiRepetitiveSubstring("abac"))  # Expected output: 4
