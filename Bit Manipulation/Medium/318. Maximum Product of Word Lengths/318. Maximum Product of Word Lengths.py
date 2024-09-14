# Problem: Maximum Product of Word Lengths
# Description: Given an array of strings `words`, we are tasked with finding the maximum product of the lengths of two words 
# such that the two words do not share any common characters.

class Solution(object):
    def maxProduct(self, words):
        """
        This function returns the maximum product of the lengths of two words in the list `words` such that 
        these two words do not share any common characters.

        :param words: A list of strings.
        :return: The maximum product of lengths of two words with no common characters.
        """
        arr = []
        
        # Step 1: Create bit masks for each word
        for word in words:
            co = 0
            for letter in word:
                co |= 1 << (ord(letter) - ord('a'))  # Set bits corresponding to each character in the word
            arr.append((co, len(word)))  # Store both bit mask and length of the word
        
        max_product = 0
        
        # Step 2: Find maximum product of lengths where bitwise AND of bit masks is 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i][0] & arr[j][0]) == 0:  # Check if words have no common characters
                    product = arr[i][1] * arr[j][1]  # Calculate the product of lengths
                    if product > max_product:
                        max_product = product  # Update maximum product if current product is greater
        
        return max_product  # Return the maximum product found

# Time Complexity: O(n^2 * m), where n is the number of words and m is the average length of the words. We generate bit masks for all words (O(n * m)) and check pairs (O(n^2)).
# Space Complexity: O(n), where n is the number of words. We store the bit masks and lengths for each word.

# Example usage:
# solution = Solution()
# words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# print(solution.maxProduct(words))  # Expected output: 16
