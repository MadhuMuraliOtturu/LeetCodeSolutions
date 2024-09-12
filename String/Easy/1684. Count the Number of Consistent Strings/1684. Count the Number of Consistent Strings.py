### BRUTE FORCE APPROACH ###
# Problem: Count Consistent Strings
# Description: Given a string `allowed` consisting of distinct characters and an array of strings `words`,
# return the number of strings in `words` that consist only of characters from `allowed`.

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        Counts the number of consistent strings in `words` that only contain characters present in `allowed`.

        :param allowed: String, the allowed characters.
        :param words: List of strings, where each string is checked for consistency.
        :return: Integer, the number of consistent strings.
        """
        allow = set(allowed)  # Create a set of allowed characters for quick lookup
        co = len(words)  # Start with the total number of words
        
        # Step 1: Iterate through each word
        for word in words:
            # Step 2: Check if all characters in the word are allowed
            for letter in word:
                if letter not in allow:
                    co -= 1  # If any letter is not allowed, decrement the count
                    break  # Move to the next word

        return co

## Time Complexity: O(N * M), where N is the number of words and M is the average length of each word.
## Space Complexity: O(K), where K is the number of distinct characters in the allowed string.

# Example usage:
# solution = Solution()
# allowed = "abc"
# words = ["a", "b", "c", "ab", "ac", "bc", "abc", "abcd"]
# print(solution.countConsistentStrings(allowed, words))  
# Expected output: 7 (all except "abcd" are consistent)




### OPTIMAL APPROACH USING BIT MASK ###

# Problem: Count the Number of Consistent Strings
# Description: Given a string `allowed` consisting of distinct characters and an array `words` 
# where each word consists of characters from the English alphabet, return the number of consistent strings in the array `words`.
# A string is consistent if all characters in the string appear in the string `allowed`.

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        Counts the number of consistent strings in the array `words` that can be formed 
        using only characters from the string `allowed`.

        :param allowed: String, containing distinct characters allowed in consistent strings.
        :param words: List of strings, the array of words to be checked for consistency.
        :return: Integer, the count of consistent strings.
        """
        allow = set(allowed)
        check = 0
        for i in allow:
            check |= 1 << (ord(i) - ord('a'))

        count = 0

        for word in words:
            bits = 0
            for letter in word:
                bits |= 1 << (ord(letter) - ord('a'))

            if bits & check == bits:
                count += 1

        return count

# Time Complexity: O(N + L), where N is the total number of characters in all words combined, 
# and L is the number of characters in the allowed string.
# Space Complexity: O(1), as we are using a constant amount of space for the bitmask representation of characters.

# Example usage:
# solution = Solution()
# allowed = "ab"
# words = ["ad", "bd", "aaab", "baa", "badab"]
# print(solution.countConsistentStrings(allowed, words))  # Expected output: 2


