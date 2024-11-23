# Problem: Minimum Cost to Shift Characters
# Description:
# Given two strings `s` and `t` of the same length and two arrays `nextCost` and `previousCost`,
# determine the minimum cost to transform `s` into `t`. Each character in the string can be
# shifted forward or backward cyclically in the alphabet with associated costs.
#
# Example:
# Input:
# s = "abc", t = "xyz"
# nextCost = [1, 2, 3, ..., 26]
# previousCost = [26, 25, ..., 1]
# Output: Minimum total cost to transform `s` into `t`.
#
# Constraints:
# - 1 <= len(s) <= 10^5
# - `s` and `t` are lowercase English letters.
# - len(nextCost) == len(previousCost) == 26

from typing import List

class Solution:
    """
    Solution to calculate the minimum cost to transform string `s` into `t`.

    :param s: str - Source string.
    :param t: str - Target string.
    :param nextCost: List[int] - Cost to shift forward in the alphabet.
    :param previousCost: List[int] - Cost to shift backward in the alphabet.
    :return: int - Minimum total cost.
    """
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        def get_min_cost(src: str, target: str) -> int:
            if src == target:
                return 0
                
            src_idx = ord(src) - ord('a')
            target_idx = ord(target) - ord('a')
            
            # Calculate forward cost
            forward_steps = (target_idx - src_idx) % 26
            forward_cost = sum(nextCost[(src_idx + i) % 26] for i in range(forward_steps))
                
            # Calculate backward cost
            backward_steps = (src_idx - target_idx) % 26
            backward_cost = sum(previousCost[(src_idx - i) % 26] for i in range(backward_steps))
            
            return min(forward_cost, backward_cost)
        
        total_cost = 0
        for src_char, target_char in zip(s, t):
            total_cost += get_min_cost(src_char, target_char)
            
        return total_cost

# Time Complexity: O(n * 26) - For each character in `s`, calculate the cost (up to 26 steps).
# Space Complexity: O(1) - Only constant extra space is used.

# Example usage:
# solution = Solution()
# print(solution.shiftDistance(
#     s="abc",
#     t="xyz",
#     nextCost=[1, 2, 3, ..., 26],
#     previousCost=[26, 25, ..., 1]
# ))  # Replace with actual costs.
