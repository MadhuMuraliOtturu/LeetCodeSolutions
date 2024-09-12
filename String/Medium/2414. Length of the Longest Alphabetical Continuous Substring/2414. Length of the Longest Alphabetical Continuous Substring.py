# Problem: Longest Continuous Substring
# Description: Given a string `s`, return the length of the longest alphabetical continuous substring.
# A substring is considered alphabetical if it consists of letters in increasing order with no gaps.

class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        Finds the longest substring in which the characters are in continuous alphabetical order.

        :param s: A string of lowercase letters.
        :return: Length of the longest continuous alphabetical substring.
        """
        # Map each letter to a corresponding number (a -> 0, b -> 1, ..., z -> 25)
        d = {
            'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
            'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
            't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
        }
        
        prev = bit_mask = 0 | 1 << d[s[0]]
        co = 1  # Initialize count for the first character
        maxs = co
        
        # Traverse through the string starting from the second character
        for i in range(1, len(s)):
            bit_mask = 0 | 1 << d[s[i]]
            # Check if the current character is the next in the alphabetical order
            if prev * 2 == bit_mask:
                co += 1
            else:
                co = 1
            prev = bit_mask
            maxs = max(maxs, co)
        
        return maxs

# Time Complexity: O(n), where n is the length of the string `s`. We traverse the string once.
# Space Complexity: O(1), since we are only using a fixed size of additional memory regardless of the input size.

# Example usage:
# solution = Solution()
# s = "abcde"
# print(solution.longestContinuousSubstring(s))  # Expected output: 5
