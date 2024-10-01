# Problem: Number of Pairs Divisible by 60
# Description: Given a list of integers `time` where each element represents the duration of a song, find the number of pairs
# of songs such that their total duration is divisible by 60.

from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        Counts the number of pairs of songs whose total duration is divisible by 60.

        :param time: List[int], list of integers where each integer represents the duration of a song.
        :return: int, the number of valid pairs where the sum of two song durations is divisible by 60.
        """
        d = {}
        for i in time:
            rem = 60 - i
            rem = rem % 60
            if rem in d:
                d[rem] += 1
            else:
                d[rem] = 1

        pair = 0
        for j in d:
            x = (60 - j) % 60
            if x in d:
                if j == x and d[j] == d[x]:
                    pair += (d[j] * (d[j] - 1)) // 2  # Combinations for the same remainder
                    d[j] = 0
                    d[x] = 0
                else:
                    pair += d[j] * d[x]  # Multiply the counts of pairs
                    d[j] = 0
                    d[x] = 0
        return pair

## Time Complexity: O(n), where n is the length of the `time` list. We iterate through the list twice.
## Space Complexity: O(1), since the dictionary can store at most 60 unique values (the remainders).

# Example usage:
# solution = Solution()
# print(solution.numPairsDivisibleBy60([30, 20, 150, 100, 40]))  # Expected output: 3
# print(solution.numPairsDivisibleBy60([60, 60, 60]))  # Expected output: 3
# print(solution.numPairsDivisibleBy60([10, 50, 90, 30]))  # Expected output: 1
