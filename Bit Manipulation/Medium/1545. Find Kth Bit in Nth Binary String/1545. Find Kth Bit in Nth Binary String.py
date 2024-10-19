# Problem: Find Kth Bit in Nth Binary String
# Description:
# Given two integers n and k, we need to find the k-th bit in the n-th binary string, 
# where the binary string is formed by repeatedly following these steps:
# - S1 = "0"
# - Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
# The function invert(s) inverts the binary string s, and reverse(s) reverses the string s.

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Returns the k-th bit of the n-th binary string in the generated sequence.

        :param n: int, the index of the binary string to generate
        :param k: int, the 1-based position of the bit to return in the binary string
        :return: str, the k-th bit in the n-th binary string
        """
        
        # Function to reverse and invert a binary string
        def invert_reverse(s):
            return ''.join('1' if c == '0' else '0' for c in s[::-1])
        
        l = ["0"]  # List to store the binary strings
        
        for i in range(1, n + 1):
            # Generate the i-th string by appending "1" and the inverted reverse of the previous string
            x = l[-1] + "1" + invert_reverse(l[-1])
            l.append(x)
        
        # Return the (k-1)th character of the n-th binary string (since indexing starts from 0)
        return l[n][k - 1]

# Time Complexity: O(2^n), as the length of the n-th string grows exponentially due to recursive generation.
# Space Complexity: O(2^n), because we are storing the binary strings up to length 2^n.

# Example usage:
# solution = Solution()
# print(solution.findKthBit(3, 5))  # Expected output: "1"
