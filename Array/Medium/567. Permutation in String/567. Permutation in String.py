# Problem: Permutation in String
# Description:
# Given two strings `s1` and `s2`, the task is to check if any permutation of `s1` is a substring of `s2`. In other words, check if some arrangement of the characters in `s1` appears in `s2`.
# The function should return `True` if any permutation of `s1` is a substring of `s2`, otherwise return `False`.

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Determines if any permutation of the string `s1` is a substring of the string `s2`.

        :param s1: str, the first input string.
        :param s2: str, the second input string where we are searching for permutations of `s1`.
        :return: bool, True if any permutation of `s1` is a substring of `s2`, False otherwise.
        """
        d1 = Counter(s1)  # Frequency map of characters in `s1`
        d2 = {}           # Sliding window frequency map of characters in `s2`
        n1 = len(s1)
        n2 = len(s2)
        
        if n2 < n1:
            return False  # If `s2` is shorter than `s1`, permutation is not possible
        
        left = 0
        right = 0
        
        # Build the initial window of size `n1` in `s2`
        while right < n1:
            if s2[right] not in d2:
                d2[s2[right]] = 0
            d2[s2[right]] += 1
            right += 1
        
        if d1 == d2:
            return True  # Check if the initial window matches the permutation
        
        # Slide the window across `s2`
        while right < n2:
            # Remove the character going out of the window
            d2[s2[left]] -= 1
            if d2[s2[left]] == 0:
                del d2[s2[left]]
            left += 1
            
            # Add the new character coming into the window
            if s2[right] not in d2:
                d2[s2[right]] = 1
            else:
                d2[s2[right]] += 1
            
            if d1 == d2:
                return True  # Check if the current window matches the permutation
            
            right += 1
        
        return False  # No permutation found

# Time Complexity: O(n2), where `n2` is the length of `s2`.
# This is because we are sliding a window of size `n1` (length of `s1`) across `s2` and comparing the frequency maps, each of which takes O(1) time due to fixed character size.
# Space Complexity: O(1), as the frequency maps `d1` and `d2` are fixed to at most 26 characters (lowercase English letters).

# Example usage:
# solution = Solution()
# print(solution.checkInclusion("ab", "eidbaooo"))  # Expected output: True
# print(solution.checkInclusion("ab", "eidboaoo"))  # Expected output: False
