# Problem: Minimum Length After Deletions
# Description:
# Given a string `s` consisting of characters 'A', 'B', 'C', and 'D', the task is to reduce the string by performing the following operations:
# - Whenever "AB" or "CD" appears consecutively, remove these pairs from the string.
# The function returns the minimum length of the string after performing all possible deletions.

class Solution(object):
    def minLength(self, s):
        """
        Reduces the string by removing consecutive pairs "AB" or "CD" and returns the minimum possible length of the string.

        :param s: str, the input string consisting of characters 'A', 'B', 'C', and 'D'.
        :return: int, the minimum length of the string after deletions.
        """
        stack = []  # Stack to keep track of characters
        
        # Process each character in the string
        for char in s:
            if not stack:
                stack.append(char)  # If stack is empty, push the current character
            else:
                # Check for consecutive "AB" or "CD" and remove them
                if char == 'B' and stack[-1] == 'A':
                    stack.pop()
                elif char == 'D' and stack[-1] == 'C':
                    stack.pop()
                else:
                    stack.append(char)  # Otherwise, push the current character into the stack

        # The final length of the stack represents the remaining string length
        return len(stack)

# Time Complexity: O(n), where `n` is the length of the input string. Each character is pushed and popped from the stack at most once.
# Space Complexity: O(n), due to the space used by the stack to store characters.

# Example usage:
# solution = Solution()
# print(solution.minLength("ABCD"))  # Expected output: 0 (all characters are deleted)
# print(solution.minLength("AABCCB"))  # Expected output: 2 (remaining string: "AA")
