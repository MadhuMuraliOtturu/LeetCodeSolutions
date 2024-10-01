# Problem: Repeated DNA Sequences
# Description: Given a string s that represents a DNA sequence, 
# return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        Finds all the 10-letter-long sequences (substrings) that occur more than once in a DNA sequence.

        :param s: str, input DNA sequence.
        :return: List[str], list of repeated 10-letter-long sequences.
        """
        n = len(s)         # Length of the input string
        i = 0              # Pointer to iterate through the string
        d = {}             # Dictionary to count occurrences of sequences
        ans = set()        # Set to store unique sequences
        new_str = ""       # Variable to hold the current 10-letter sequence
        
        while(i < 10 and i < n):  # Get the first 10 characters if possible
            new_str += s[i]
            i += 1
            
        if len(new_str) == 10:  # Store the first sequence
            d[new_str] = 1
            
        for k in range(i, n):  # Iterate through the rest of the string
            new_str = new_str[1:] + s[k]  # Slide the window
            if new_str in d:
                d[new_str] += 1  # Increment count if seen before
                ans.add(new_str)  # Add to result set
            else:
                d[new_str] = 1  # First occurrence of the sequence
        
        return list(ans)  # Convert set to list before returning

# Time Complexity: O(n), where n is the length of the string, as we iterate through the string once.
# Space Complexity: O(m), where m is the number of unique 10-letter sequences stored.

# Example usage:
# solution = Solution()
# print(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))  # Expected output: ['AAAAACCCCC', 'CCCCCAAAAA']
# print(solution.findRepeatedDnaSequences("AAAAAAAAAAAAA"))  # Expected output: ['AAAAAAAAAA']
