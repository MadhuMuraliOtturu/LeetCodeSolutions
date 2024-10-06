# Problem: Sentence Similarity
# Description:
# Given two sentences `s1` and `s2` represented as strings of words separated by spaces, the task is to check if the sentences are similar. Two sentences are considered similar if one sentence can be derived from the other by removing some words from the ends. The function should return `True` if the sentences are similar, otherwise return `False`.

class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        """
        Checks if sentence `s1` can be made similar to sentence `s2` by removing some words from the beginning and/or end.

        :param s1: str, the first input sentence.
        :param s2: str, the second input sentence.
        :return: bool, True if the sentences are similar, False otherwise.
        """
        str1 = s1.split(" ")  # Split sentence `s1` into words
        str2 = s2.split(" ")  # Split sentence `s2` into words
        n1 = len(str1)
        n2 = len(str2)

        if n1 > n2:
            # If `s1` is longer than `s2`, swap them and check similarity again
            return self.areSentencesSimilar(s2, s1)

        i = 0  # Left pointer for `str1` and `str2`
        j = 0  # Left pointer for `str2`

        # Compare words from the beginning
        while i < n1 and j < n2:
            if str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                break

        # Compare words from the end
        a = n1 - 1  # Right pointer for `str1`
        b = n2 - 1  # Right pointer for `str2`
        while a >= 0 and b >= 0:
            if str1[a] == str2[b]:
                a -= 1
                b -= 1
            else:
                break

        # If the pointers from the left and right overlap, sentences are similar
        return i > a

# Time Complexity: O(n1 + n2), where `n1` is the number of words in `s1` and `n2` is the number of words in `s2`. We process each word in both sentences at most once.
# Space Complexity: O(n1 + n2), due to the space used for splitting the strings into lists of words.

# Example usage:
# solution = Solution()
# print(solution.areSentencesSimilar("My name is Alice", "Alice"))  # Expected output: True
# print(solution.areSentencesSimilar("Alice is happy", "Alice"))  # Expected output: False
