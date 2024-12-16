# Problem: Get Final State After k Operations
# Description:
# You are given a list of integers `nums`, an integer `k`, and a multiplier `mul`. Perform the following operations exactly `k` times:
# 1. Extract the smallest element from the list.
# 2. Multiply the extracted element by `mul`.
# 3. Add the updated element back to the list.
# After `k` operations, return the final state of the list, preserving the original order of indices.
#
# Example:
# Input: nums = [4, 2, 5], k = 2, mul = 3
# Output: [4, 18, 5]
# Explanation:
# - First operation: Extract 2 (smallest), multiply by 3 → 6. The list becomes [4, 6, 5].
# - Second operation: Extract 4 (smallest), multiply by 3 → 12. The list becomes [12, 6, 5].
# - Return the list in original index order: [4, 18, 5].
#
# Constraints:
# - 1 <= len(nums) <= 10^5
# - 1 <= nums[i], k, mul <= 10^6

import heapq
from typing import List

class Solution:
    """
    Computes the final state of the list after k operations of multiplying 
    the smallest element by a given multiplier.

    :param nums: List[int] - The initial list of integers.
    :param k: int - The number of operations to perform.
    :param mul: int - The multiplier for the smallest element.
    :return: List[int] - The final state of the list, preserving the original order of indices.
    """
    def getFinalState(self, nums: List[int], k: int, mul: int) -> List[int]:
        # Initialize a heap with (value, index) pairs
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)  # Min-heap based on the value
        
        # Perform k operations
        for _ in range(k):
            val, idx = heapq.heappop(heap)  # Extract the smallest value
            val *= mul  # Multiply the value by the multiplier
            heapq.heappush(heap, (val, idx))  # Push the updated value back to the heap
        
        # Construct the result array based on original indices
        result = [0] * len(nums)
        for val, idx in heap:
            result[idx] = val
        
        return result

# Time Complexity: O(k * log(n) + n * log(n)), where `n` is the length of the array and `k` is the number of operations.
# Space Complexity: O(n), for the heap and the result array.

# Example usage:
# solution = Solution()
# print(solution.getFinalState([4, 2, 5], 2, 3))  # Output: [4, 18, 5]
# print(solution.getFinalState([1, 3, 2], 3, 2))  # Output: [8, 6, 4]
