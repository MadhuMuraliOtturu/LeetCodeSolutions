# Problem: Decrypt the Code
# Description:
# You are given a list of integers `code` and an integer `k`. To decrypt the code:
# - If `k > 0`, replace each code[i] with the sum of the next `k` numbers. The list is circular.
# - If `k < 0`, replace each code[i] with the sum of the previous `|k|` numbers. The list is circular.
# - If `k == 0`, replace each code[i] with 0.
#
# Example:
# Input: code = [5, 7, 1, 4], k = 3
# Output: [12, 10, 16, 13]
# Explanation:
# - For code[0], sum the next 3 numbers: 7 + 1 + 4 = 12.
# - For code[1], sum the next 3 numbers: 1 + 4 + 5 = 10.
# - For code[2], sum the next 3 numbers: 4 + 5 + 7 = 16.
# - For code[3], sum the next 3 numbers: 5 + 7 + 1 = 13.
#
# Constraints:
# - 1 <= len(code) <= 100
# - 1 <= code[i] <= 100
# - -len(code) <= k <= len(code)

from typing import List

class Solution:
    """
    Solution to decrypt the circular array based on the given rules.
    
    :param code: List[int] - List of integers representing the encrypted code.
    :param k: int - Number indicating how to decrypt the code.
    :return: List[int] - List representing the decrypted code.
    """

    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        for i in range(n):
            co = 0
            if k > 0:
                for j in range(1, k + 1):
                    co += code[(i + j) % n]
            elif k < 0:
                for j in range(1, -k + 1):
                    co += code[(i - j) % n]
            result[i] = co

        return result

# Time Complexity: O(n * |k|) - Iterating through the array and performing up to |k| additions per element.
# Space Complexity: O(n) - Output list.

# Example usage:
# solution = Solution()
# print(solution.decrypt([5, 7, 1, 4], 3))  # Output: [12, 10, 16, 13]
