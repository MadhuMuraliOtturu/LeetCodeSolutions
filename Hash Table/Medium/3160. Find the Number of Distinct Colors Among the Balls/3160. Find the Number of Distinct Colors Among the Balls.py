# Problem: Query Results with Unique Values
# Description:
# Given a limit and a list of queries, where each query consists of (x, y),
# update the mapping of x to y and keep track of how many unique y-values exist.
# Return the count of unique y-values after each query.
#
# Example:
# Input:
# limit = 5
# queries = [[1, 2], [2, 3], [1, 3], [4, 2]]
# Output: [1, 2, 1, 2]
#
# Explanation:
# - (1,2) → {1:2}, unique values = {2} → count = 1
# - (2,3) → {1:2, 2:3}, unique values = {2,3} → count = 2
# - (1,3) → {1:3, 2:3}, unique values = {3} → count = 1
# - (4,2) → {1:3, 2:3, 4:2}, unique values = {3,2} → count = 2
#
# Constraints:
# - 1 <= limit <= 10^5
# - 1 <= len(queries) <= 10^5
# - 1 <= x, y <= limit

from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        """
        Processes queries and returns the number of unique y-values after each update.

        Args:
            limit (int): The upper bound on x and y values.
            queries (List[List[int]]): A list of queries where each query is [x, y].

        Returns:
            List[int]: A list of counts of unique y-values after each query.
        """
        result = []
        d1 = {}  # Maps x to its assigned y
        d2 = {}  # Maps y to the list of x-values assigned to it
        unique_count = 0

        for x, y in queries:
            if x in d1:
                old_y = d1[x]
                d2[old_y].remove(x)
                if not d2[old_y]:  # If old y-value is now empty, reduce count
                    unique_count -= 1

            d1[x] = y
            if y not in d2:
                d2[y] = [x]
            else:
                d2[y].append(x)

            if len(d2[y]) == 1:  # If new y-value is first-time unique, increase count
                unique_count += 1

            result.append(unique_count)

        return result

# Time Complexity: O(N), where N is the number of queries.
# Space Complexity: O(N), as we store mappings for x and y values.
