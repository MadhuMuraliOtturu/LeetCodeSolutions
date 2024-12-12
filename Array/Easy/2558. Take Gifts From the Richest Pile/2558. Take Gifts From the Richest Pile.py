# Problem: Minimize Gift Count
# Description:
# You are given a list of integers `gifts`, where each integer represents the number of gifts in a pile.
# You can perform at most `k` operations where, in each operation, you:
# 1. Pick the pile with the largest number of gifts.
# 2. Replace the pile with the square root of the number of gifts, rounded down to the nearest integer.
# Return the total number of gifts remaining after performing the `k` operations.
#
# Example:
# Input: gifts = [9, 3, 5], k = 2
# Output: 8
# Explanation:
# - After the first operation, replace 9 with ⌊sqrt(9)⌋ = 3. Gifts become [3, 3, 5].
# - After the second operation, replace 5 with ⌊sqrt(5)⌋ = 2. Gifts become [3, 3, 2].
# - The total number of gifts remaining is 3 + 3 + 2 = 8.
#
# Constraints:
# - 1 <= len(gifts) <= 10^5
# - 1 <= gifts[i] <= 10^9
# - 1 <= k <= 10^4

import heapq
import math
from typing import List

class Solution:
    """
    Minimizes the total number of gifts after performing at most `k` operations on the piles.

    :param gifts: List[int] - A list of integers representing the number of gifts in each pile.
    :param k: int - The maximum number of operations to perform.
    :return: int - The total number of gifts remaining after `k` operations.
    """
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Convert the gifts list into a max-heap (using negative values for heapq)
        gifts = [-i for i in gifts]
        heapq.heapify(gifts)

        # Perform `k` operations
        for _ in range(k):
            largest = -heapq.heappop(gifts)  # Extract the largest pile
            reduced = math.floor(math.sqrt(largest))  # Reduce it to the floor of its square root
            heapq.heappush(gifts, -reduced)  # Push the reduced value back into the heap

        # Return the total number of gifts remaining (convert back from negative values)
        return -sum(gifts)

# Time Complexity: O(k * log(n)), where `n` is the number of piles and `k` is the number of operations.
# Space Complexity: O(n), for the heap storage.

# Example usage:
# solution = Solution()
# print(solution.pickGifts([9, 3, 5], 2))  # Output: 8
# print(solution.pickGifts([16, 5, 10], 3))  # Output: 15
