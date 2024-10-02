# Problem: Rank Transform of an Array
# Description: Given an array of integers `arr`, return an array of the same length where each element is replaced by its rank. 
# The rank represents the position of the number in a sorted version of the array.
# Ranks should be as small as possible, and tied numbers should share the same rank.

import copy
import heapq
from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Transforms the array `arr` by replacing each element with its rank, where the rank is its position
        in the sorted unique list of the elements.

        :param arr: List[int], input array of integers.
        :return: List[int], transformed array with ranks in place of original values.
        """
        heap = copy.deepcopy(arr)  # Make a deep copy of the array to avoid modifying the original
        heapq.heapify(heap)  # Convert the array into a heap (min-heap by default)
        d = {}  # Dictionary to store the rank of each element
        i = 1   # Starting rank

        # Assign ranks to each unique element by popping from the heap
        while heap:
            x = heapq.heappop(heap)  # Get the smallest element from the heap
            if x not in d:  # If the element hasn't been assigned a rank yet
                d[x] = i
                i += 1
        
        # Replace the elements in the original array with their corresponding ranks
        for i in range(len(arr)):
            arr[i] = d[arr[i]]
        
        return arr

# Time Complexity: O(n log n), where n is the length of the input array. The heapify operation takes O(n), 
# and each pop operation from the heap takes O(log n). The final loop to assign ranks takes O(n).
# Space Complexity: O(n), for storing the heap and the dictionary.

# Example usage:
# solution = Solution()
# print(solution.arrayRankTransform([40, 10, 20, 30]))  # Expected output: [4, 1, 2, 3]
# print(solution.arrayRankTransform([100, 100, 100]))   # Expected output: [1, 1, 1]
