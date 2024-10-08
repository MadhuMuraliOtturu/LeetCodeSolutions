# Problem: Minimum Swaps to Balance Brackets
# Description:
# You are given a string `s` consisting only of the characters '[' and ']'. The task is to make the string balanced by swapping some pairs of brackets. 
# A string is balanced if it has an equal number of '[' and ']', and for every prefix of the string, the number of ']' does not exceed the number of '['. 
# The function returns the minimum number of swaps required to balance the string.

class Solution(object):
    def minSwaps(self, s):
        """
        Calculates the minimum number of swaps required to balance the given string of brackets.

        :param s: str, input string consisting of characters '[' and ']'
        :return: int, the minimum number of swaps required to balance the string
        """
        co = 0  # Counter to track the number of unbalanced ']' brackets
        stack = []  # Stack to keep track of open '[' brackets
        
        # Iterate through each character in the string
        for i in s:
            if i == '[':
                stack.append(i)  # If an open bracket, push to stack
            else:
                if stack:
                    stack.pop()  # If there's an open bracket in the stack, balance it
                else:
                    co += 1  # Otherwise, increase the count of unbalanced close brackets
        
        # Each swap fixes 2 unbalanced brackets, so the result is (co + 1) // 2
        return (co + 1) // 2

# Time Complexity: O(n), where `n` is the length of the input string. Each character is processed once.
# Space Complexity: O(n), due to the space used by the stack to store unbalanced '[' brackets.

# Example usage:
# solution = Solution()
# print(solution.minSwaps("][]["))  # Expected output: 1 (one swap needed to balance the brackets)
# print(solution.minSwaps("[]"))  # Expected output: 0 (already balanced)
