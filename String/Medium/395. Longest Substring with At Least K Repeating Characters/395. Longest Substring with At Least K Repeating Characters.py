# Problem: Longest Substring with At Least K Repeating Characters
# Description:
# Given a string `s` and an integer `k`, find the length of the longest substring where every character appears at least `k` times.

from typing import Dict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring in the string `s` where each character appears at least `k` times.

        :param s: str, the input string.
        :param k: int, the minimum number of repetitions for each character in the substring.
        :return: int, the length of the longest valid substring.
        """
        lens = 0  # To keep track of the maximum length of valid substrings
        n = len(s)
        left = 0  # Starting point of the sliding window
        
        # Iterate through all possible substrings using a sliding window approach
        while left < n:
            d: Dict[str, int] = {}  # Dictionary to count occurrences of characters
            co = 0  # Counter for how many characters meet the 'k' condition
            
            # Move the right pointer to explore new substrings
            for right in range(left, n):
                if s[right] not in d:
                    d[s[right]] = 0
                d[s[right]] += 1
                
                # If the character count reaches k, increment the valid character counter
                if d[s[right]] == k:
                    co += 1

                # If all characters in the current substring have counts >= k, update the maximum length
                if co == len(d):
                    lens = max(lens, right - left + 1)
            
            left += 1  # Move the left pointer to explore new substrings
        
        return lens

# Time Complexity: O(n^2), where `n` is the length of the string. The algorithm uses a nested loop where the inner loop checks for each character count.
# Space Complexity: O(n), due to the use of the dictionary to store character counts.

# Example usage:
# solution = Solution()
# print(solution.longestSubstring("aaabb", 3))  # Expected output: 3
# print(solution.longestSubstring("ababbc", 2)) # Expected output: 5
