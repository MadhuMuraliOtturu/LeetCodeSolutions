# Problem: Minimize the Score
# Description:
# You are given a list of integers `nums`. You need to calculate the "score" of the array by performing the following:
# 1. Repeatedly choose the smallest unmarked element in the array.
# 2. Add its value to the score and mark it and its neighbors (both left and right) as "used."
# Return the total score after all possible operations.
#
# Example:
# Input: nums = [2, 1, 3, 4]
# Output: 4
# Explanation:
# - Select 1 (the smallest unmarked element), add it to the score. Mark index 1 and its neighbors (0 and 2).
# - Remaining unmarked elements: [X, X, 3, 4].
# - Select 3, add it to the score. Mark index 2 and its neighbors.
# - Total score is 1 + 3 = 4.
#
# Constraints:
# - 1 <= len(nums) <= 10^5
# - 1 <= nums[i] <= 10^6

import heapq
from typing import List

class Solution:
    """
    Calculates the minimum score by marking elements and their neighbors based on the smallest value.
    
    :param nums: List[int] - A list of integers representing the array.
    :return: int - The total score after all operations.
    """
    def findScore(self, nums: List[int]) -> int:
        # Dictionary to store values and their indices
        d = {}
        ind = {}
        score = 0
        n = len(nums)

        # Populate dictionaries for fast lookup
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = []
            ind[i] = nums[i]
            d[nums[i]].append(i)

        # Create a min-heap of elements with their indices
        arr = [(nums[i], i) for i in range(n)]
        heapq.heapify(arr)

        # Array to track marked indices
        marked = [False] * n

        # Process elements in the heap
        while arr:
            value, idx = heapq.heappop(arr)
            if marked[idx]:
                continue
            # Add value to the score
            score += value
            # Mark the current index and its neighbors
            marked[idx] = True
            if idx > 0:
                marked[idx - 1] = True
            if idx < n - 1:
                marked[idx + 1] = True

        return score

# Time Complexity: O(n * log(n)), where `n` is the size of the input array.
# Space Complexity: O(n), for the heap and auxiliary data structures.

# Example usage:
# solution = Solution()
# print(solution.findScore([2, 1, 3, 4]))  # Output: 4
# print(solution.findScore([4, 3, 2, 6]))  # Output: 6
