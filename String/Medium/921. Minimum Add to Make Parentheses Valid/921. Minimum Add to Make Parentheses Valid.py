# Problem: Minimum Add to Make Parentheses Valid
# Description:
# Given a string `s` consisting of '(' and ')', determine the minimum number of parentheses to add 
# in order to make the string valid. A string is valid if:
# - Every open parenthesis '(' has a corresponding closing parenthesis ')'.
# - Every closing parenthesis ')' has a preceding matching open parenthesis '('.
# The function returns the minimum number of parentheses (both open and close) needed to make the string valid.

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        Calculates the minimum number of parentheses to add to make the given string valid.

        :param s: str, input string consisting of '(' and ')'
        :return: int, the minimum number of parentheses to add to make the string valid
        """
        op = 0  # Counter for unmatched open parentheses '('
        cl = 0  # Counter for unmatched closing parentheses ')'
        
        # Iterate through each character in the string
        for i in s:
            if i == '(': 
                op += 1  # Increment open parentheses counter
            else:
                if op == 0:
                    cl += 1  # No open parenthesis to match, increment closing counter
                else:
                    op -= 1  # Match open parenthesis with closing one
        
        # The total parentheses to add will be the sum of unmatched open and close parentheses
        return cl + op

# Time Complexity: O(n), where `n` is the length of the input string. Each character is processed once.
# Space Complexity: O(1), since the algorithm uses a constant amount of extra space regardless of input size.

# Example usage:
# solution = Solution()
# print(solution.minAddToMakeValid("())"))  # Expected output: 1 (one open parenthesis needed)
# print(solution.minAddToMakeValid("((("))  # Expected output: 3 (three closing parentheses needed)
