# Problem: LeetCode 2028 - Find Missing Observations
# https://leetcode.com/problems/find-missing-observations/

from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        Finds the missing n rolls of a dice given the current rolls and the target mean.

        :param rolls: List[int], the current dice rolls.
        :param mean: Integer, the target mean of all dice rolls (current + missing).
        :param n: Integer, the number of missing rolls.
        :return: List[int], the missing rolls if they can satisfy the target mean, otherwise an empty list.
        """
        m = len(rolls)  # Number of current rolls
        new_mean = mean * (n + m)  # Total sum required to achieve the target mean
        req_sum = new_mean - sum(rolls)  # Sum required for the missing rolls
        
        # Step 1: Check if the required sum is possible within the range [n, 6*n]
        if req_sum > 6 * n or req_sum <= 0 or req_sum < n:
            return []  # If it's not possible, return an empty list
        
        # Step 2: Distribute the required sum evenly across the missing rolls
        val = req_sum // n  # Base value for each missing roll
        mods = req_sum % n  # Remainder to be distributed across the first 'mods' rolls
        ans = [val] * n  # Initialize the missing rolls with the base value
        
        # Step 3: Distribute the remaining sum to the first 'mods' elements
        for i in range(mods):
            ans[i] += 1
        
        return ans  # Return the list of missing rolls

## Time Complexity: O(n), where n is the number of missing rolls.
## Space Complexity: O(n), for storing the missing rolls.

# Example usage:
# solution = Solution()
# print(solution.missingRolls([3,2,4,3], 4, 2))  # Output should be [6, 6] or another valid combination.
