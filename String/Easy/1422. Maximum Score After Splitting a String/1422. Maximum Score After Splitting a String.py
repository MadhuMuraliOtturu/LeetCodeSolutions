# Problem: Maximize Score After Splitting a String
# Description:
# Given a string `s` of 0's and 1's, split the string into two non-empty substrings 
# (left and right). The score after splitting is the number of '0's in the left substring 
# plus the number of '1's in the right substring. Return the maximum possible score 
# after splitting the string.
#
# Example:
# Input: s = "011101"
# Output: 5
# Explanation:
# - Split at index 3: Left substring "011", Right substring "101"
# - Score: 2 ('0's in left) + 3 ('1's in right) = 5
#
# Constraints:
# - 2 <= len(s) <= 500
# - s[i] is either '0' or '1'.

class Solution:
    def maxScore(self, s: str) -> int:
        """
        Calculates the maximum score achievable after splitting the string into two parts.

        Args:
            s (str): The binary string.

        Returns:
            int: The maximum score possible.
        """
        ones = s.count("1")
        zeros = 0
        ans = 0 
        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            ans = max(ans, zeros + ones)
        return ans

# Time Complexity: O(N), where N is the length of the string.
# Space Complexity: O(1), as we are using constant extra space.
