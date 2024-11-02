# Problem: Circular Sentence Checker
# Description:
# Given a sentence represented as a single string `s`, the task is to determine if it is a "circular sentence."
# A sentence is circular if the last character of each word matches the first character of the next word, 
# with the last word linking back to the first.
#
# Example:
# Input: s = "loop over relay yes"
# Output: True
# Explanation: The last letter of each word matches the first letter of the next word, making it circular.
#
# Constraints:
# - 1 <= len(s) <= 10^4
# - s consists of lowercase English letters and spaces.
# - `s` does not contain leading or trailing spaces, and there is exactly one space between each pair of words.

class Solution:
    """
    Solution class to check if a sentence is circular.
    
    :param s: str - A sentence to be checked for circularity.
    :return: bool - True if the sentence is circular, False otherwise.
    """
    def isCircularSentence(self, s: str) -> bool:
        words = s.split()  
        n = len(words)
        
        for i in range(n):
            if words[i][-1] != words[(i + 1) % n][0]:  
                return False
        
        return True

# Time Complexity: O(n) - where n is the number of words in the sentence.
# Space Complexity: O(n) - for storing the split words list.

# Example usage:
# solution = Solution()
# print(solution.isCircularSentence("loop over relay yes"))  # Output: True
