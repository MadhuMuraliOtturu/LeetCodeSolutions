# Problem: Maximum Count of Non-Banned Numbers Within a Maximum Sum
# Description:
# You are given a list of banned integers `banned`, an integer `n`, and an integer `maxSum`.
# You are tasked to find the maximum number of integers from the range [1, n] that are not in `banned`
# such that the sum of these integers does not exceed `maxSum`.
#
# Example:
# Input: banned = [1, 4, 6], n = 10, maxSum = 20
# Output: 3
# Explanation:
# - Select integers 2, 3, and 5. Their sum is 2 + 3 + 5 = 10 <= 20.
# - You cannot include 1 (banned) or 4, 6 (banned).
#
# Constraints:
# - 1 <= n <= 10^4
# - 1 <= maxSum <= 10^9
# - 0 <= banned.length <= 10^4
# - 1 <= banned[i] <= n
#
# Note:
# The `banned` array may contain duplicates. Ensure the final result considers only unique values.

class Solution:
    """
    Finds the maximum count of integers from 1 to n that are not in the banned list
    and whose sum does not exceed maxSum.

    :param banned: List[int] - A list of integers that are banned.
    :param n: int - The upper limit of the range [1, n].
    :param maxSum: int - The maximum allowable sum of selected integers.
    :return: int - The maximum count of integers satisfying the conditions.
    """
    def maxCount(self, banned, n, maxSum):
        nums = []
        check = 0
        co = 0

        # Convert banned list to a set for fast lookup
        banned = list(set(banned))

        # Iterate over the range [1, n] to find non-banned integers
        for i in range(1, n + 1):
            if i not in banned:
                check += i
                if check <= maxSum:
                    co += 1
                if check >= maxSum:
                    return co
        return co

# Time Complexity: O(n), where n is the upper limit of the range [1, n].
# Space Complexity: O(b), where b is the size of the banned list.

# Example usage:
# solution = Solution()
# print(solution.maxCount([1, 4, 6], 10, 20))  # Output: 3
# print(solution.maxCount([], 5, 15))          # Output: 5
