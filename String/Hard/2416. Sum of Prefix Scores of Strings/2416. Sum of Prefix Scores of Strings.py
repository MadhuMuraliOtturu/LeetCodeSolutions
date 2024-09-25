# Problem: Sum of Prefix Scores
# Description: Given an array of words, the task is to calculate the sum of scores for each word where the score of a word 
# is the total number of times each of its prefixes appears across all words in the array.

from collections import Counter
from typing import List

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        """
        This function computes the sum of prefix scores for each word in a list of words.

        :param words: List[str] - A list of words
        :return: List[int] - A list of prefix scores for each word
        """
        # Dictionary to store prefix counts
        d = Counter()
        
        # Count occurrences of each prefix
        for word in words:
            pref = ""
            for let in word:
                pref += let
                d[pref] += 1
        
        # Calculate the score for each word based on prefix counts
        ans = []
        for word in words:
            pref = ""
            co = 0
            for let in word:
                pref += let
                co += d[pref]  # Add prefix count to the score
            ans.append(co)
        
        return ans

# Time Complexity: O(n * m), where n is the number of words and m is the average length of the words.
# This is because we iterate over each word and its prefixes.
# Space Complexity: O(n * m), where n is the number of words and m is the length of the longest word, 
# as we store each prefix in the dictionary.
#
# Example Usage:
# solution = Solution()
# print(solution.sumPrefixScores(["abc", "ab", "bc", "b"]))  # Output: [5, 4, 3, 2]
# print(solution.sumPrefixScores(["abcd", "a", "abc", "ab"]))  # Output: [4, 1, 3, 2]
