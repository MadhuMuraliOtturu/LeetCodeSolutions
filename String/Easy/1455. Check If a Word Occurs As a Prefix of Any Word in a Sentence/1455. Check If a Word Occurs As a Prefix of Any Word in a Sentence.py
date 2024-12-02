# Problem: Check if a Word is a Prefix of Any Word in a Sentence
# Description:
# Given a sentence consisting of words separated by spaces and a search word, determine if the search word is a prefix of any word in the sentence.
# If the search word is a prefix of multiple words, return the 1-based index of the first occurrence. If it is not a prefix of any word, return -1.
#
# Example:
# Input: sentence = "i love programming", searchWord = "pro"
# Output: 3
# Explanation: "pro" is a prefix of the third word, "programming".
#
# Constraints:
# - 1 <= sentence.length <= 100
# - 1 <= searchWord.length <= 10
# - The sentence consists of lowercase English letters and spaces.
# - The searchWord consists of lowercase English letters.

class Solution:
    """
    Determines if a given word is a prefix of any word in the provided sentence.
    
    :param sentence: str - The input sentence consisting of words separated by spaces.
    :param searchWord: str - The word to check as a prefix.
    :return: int - 1-based index of the first word where searchWord is a prefix, or -1 if not found.
    """
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")  # Split sentence into words
        j = 0  # Word index counter
        for i in sentence:
            try:
                # Check if searchWord is a prefix of the current word
                if i.index(searchWord) == 0:
                    return j + 1  # Return 1-based index
            except ValueError:
                pass
            j += 1
        return -1  # Return -1 if no prefix match found

# Time Complexity: O(n * m), where n is the number of words in the sentence and m is the average word length.
# Space Complexity: O(n), where n is the number of words (for the split operation).

# Example usage:
# solution = Solution()
# print(solution.isPrefixOfWord("i love programming", "pro"))  # Output: 3
# print(solution.isPrefixOfWord("hello world", "wo"))          # Output: 2
# print(solution.isPrefixOfWord("a quick brown fox", "br"))    # Output: 3
# print(solution.isPrefixOfWord("look here", "no"))            # Output: -1
