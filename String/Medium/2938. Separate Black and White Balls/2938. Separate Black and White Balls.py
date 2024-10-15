# Problem: Minimum Steps to Rearrange Binary String
# Description:
# You are given a binary string `s` that contains only '0's and '1's. The goal is to calculate the 
# minimum number of steps to move all '0's to the left side of the string while keeping the relative 
# order of the '1's unchanged. The function returns the minimum number of steps required.

class Solution:
    def minimumSteps(self, s: str) -> int:
        """
        Computes the minimum number of steps required to move all '0's to the left side of the binary string
        while maintaining the relative order of the '1's.

        :param s: str, input binary string consisting of '0's and '1's
        :return: int, minimum number of steps to move all '0's to the left
        """
        co = 0  # Initialize step counter
        n = len(s)  # Length of the input string
        zero = 0  # Counter to track the number of '0's encountered
        
        for i in range(n):
            if s[i] == '0':  # If current character is '0'
                co += i - zero  # Calculate the number of steps needed to shift '0'
                zero += 1  # Increment the zero counter

        return co  # Return the minimum steps

# Time Complexity: O(n), where `n` is the length of the input string. We traverse the string once.
# Space Complexity: O(1), constant space is used since we only need a few variables.

# Example usage:
# solution = Solution()
# print(solution.minimumSteps("1101001"))  # Expected output: 5
