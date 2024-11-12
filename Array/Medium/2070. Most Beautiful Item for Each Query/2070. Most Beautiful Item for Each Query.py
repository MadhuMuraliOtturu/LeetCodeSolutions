# Problem: Maximum Beauty of an Item After Price Filter
# Description:
# Given a list of items, where each item has a price and a beauty value, and a list of price queries, 
# the goal is to determine the maximum beauty obtainable for each query based on the maximum price that can be paid.
# 
# For each query, return the highest beauty achievable among items with prices <= query price. If no such item exists, return 0.
# 
# Example:
# Input: items = [[1,2],[3,5],[2,3]], queries = [2,3]
# Output: [3, 5]
# Explanation: For query price 2, the maximum beauty is 3. For query price 3, the maximum beauty is 5.
#
# Constraints:
# - `1 <= len(items), len(queries) <= 10^5`
# - `1 <= items[i][0], items[i][1], queries[j] <= 10^9`

from typing import List

class Solution:
    """
    Solution class to find the maximum beauty for each price query.
    
    :param items: List[List[int]] - List of items where each item is represented by [price, beauty].
    :param queries: List[int] - List of maximum prices for each query.
    :return: List[int] - List of maximum beauty values for each price query.
    """
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])  # Sort items by price

        max_beauty_so_far = []
        current_max_beauty = 0

        # Build a list of maximum beauty values for each price point
        for cost, beauty in items:
            current_max_beauty = max(current_max_beauty, beauty)
            max_beauty_so_far.append((cost, current_max_beauty))
        
        result = []
        for query in queries:
            left, right = 0, len(items) - 1
            # Binary search to find the highest affordable beauty
            while left <= right:
                mid = (left + right) // 2
                if max_beauty_so_far[mid][0] <= query:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if right == -1:
                result.append(0)
            else:
                result.append(max_beauty_so_far[right][1])
        
        return result

# Time Complexity: O((m + n) log m) - where m is the length of items, and n is the length of queries.
# Space Complexity: O(m) - storing maximum beauty values for each price point.

# Example usage:
# solution = Solution()
# print(solution.maximumBeauty([[1,2],[3,5],[2,3]], [2,3]))  # Output: [3, 5]
