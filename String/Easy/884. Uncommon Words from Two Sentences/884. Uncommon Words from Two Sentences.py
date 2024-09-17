# Problem: Uncommon Words from Two Sentences
# Description: You are given two sentences, `s1` and `s2`, represented as strings.
# Your task is to find all words that appear exactly once in one of the sentences and not at all in the other sentence.
# Return the list of these uncommon words.

from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        This function takes two sentences s1 and s2 as input, finds all words that appear exactly once 
        in one sentence and do not appear in the other sentence, and returns a list of these words.
        
        :param s1: str - first sentence
        :param s2: str - second sentence
        :return: List[str] - list of uncommon words from both sentences
        """
        
        # Split the sentences into words
        str1 = s1.split(" ")
        str2 = s2.split(" ")
        
        # Create frequency counters for both sentences
        d1 = Counter(str1)
        d2 = Counter(str2)
        
        # Initialize the answer list
        ans = []
        
        # Check for words that appear once in s1 and not in s2
        for i in d1:
            if d1[i] == 1 and i not in d2:
                ans.append(i)
        
        # Check for words that appear once in s2 and not in s1
        for j in d2:
            if d2[j] == 1 and j not in d1:
                ans.append(j)
        
        return ans

# Time Complexity: O(n + m), where n and m are the number of words in s1 and s2 respectively.
# This is due to splitting the sentences and counting the word frequencies.
#
# Space Complexity: O(n + m), since we store all the words from s1 and s2 in frequency counters.
#
# Example Usage:
# solution = Solution()
# print(solution.uncommonFromSentences("apple banana orange", "banana grape apple"))
# Output: ["orange", "grape"]
