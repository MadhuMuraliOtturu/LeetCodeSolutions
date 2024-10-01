# Problem: Count Complete Day Pairs
# Description: Given a list of integers `hours` representing the hours worked per day, find the number of distinct pairs of days
# such that the sum of the hours worked on the two days is exactly 24.

from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        """
        Counts the number of pairs of days where the sum of the hours worked is exactly 24.

        :param hours: List[int], list of integers where each integer represents the hours worked in a day.
        :return: int, the number of valid pairs where the sum of two days equals 24.
        """
        d = {}
        for i in hours:
            rem = 24 - i
            rem = rem % 24
            if rem in d:
                d[rem] += 1
            else:
                d[rem] = 1

        pair = 0
        for j in d:
            x = (24 - j) % 24
            if x in d:
                if j == x and d[j] == d[x]:
                    co = d[j]
                    d[x] -= d[j]
                    d[j] = 0
                    pair += (co * (co - 1)) // 2  # Combinations for the same remainder
                else:
                    pair += d[j] * d[x]  # Multiply the counts of pairs
                    d[j] = 0
                    d[x] = 0
        return pair

## Time Complexity: O(n), where n is the length of the hours list. We iterate through the list twice.
## Space Complexity: O(1), since we only store a constant number of elements (at most 24 unique values in the dictionary).

# Example usage:
# solution = Solution()
# print(solution.countCompleteDayPairs([8, 16, 5, 19, 12, 12]))  # Expected output: 2
# print(solution.countCompleteDayPairs([5, 19, 8, 16]))  # Expected output: 2
# print(solution.countCompleteDayPairs([1, 23, 5, 19]))  # Expected output: 1
