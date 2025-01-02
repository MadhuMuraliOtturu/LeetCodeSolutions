# Problem: Count Vowel Strings in Ranges
# Description:
# Given a list of words and a list of queries, determine how many words in the 
# specified range start and end with a vowel ('a', 'e', 'i', 'o', 'u'). 
# For each query, the range [a, b] is inclusive.
#
# Example:
# Input:
# words = ["apple", "banana", "orange", "umbrella"]
# queries = [[0, 2], [1, 3]]
# Output: [2, 2]
#
# Explanation:
# - Query [0, 2]: Words "apple" and "orange" start and end with vowels.
# - Query [1, 3]: Words "orange" and "umbrella" start and end with vowels.
#
# Constraints:
# - 1 <= len(words) <= 10^5
# - Each word contains only lowercase English letters.
# - 1 <= len(queries) <= 10^5

class Solution(object):
    def vowelStrings(self, words, queries):
        """
        Calculates the count of words starting and ending with vowels 
        for each range query.

        Args:
            words (List[str]): List of words.
            queries (List[List[int]]): List of range queries.

        Returns:
            List[int]: List of results for each query.
        """
        vowels = 'aeiou'
        l1 = []
        co = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                co += 1
            l1.append(co)
        
        res = []
        for a, b in queries:
            if a != 0:
                res.append(l1[b] - l1[a - 1])
            else:
                res.append(l1[b])
        
        return res

# Time Complexity: O(N + Q), where N is the number of words and Q is the number of queries.
# Space Complexity: O(N), due to the prefix sum array.
