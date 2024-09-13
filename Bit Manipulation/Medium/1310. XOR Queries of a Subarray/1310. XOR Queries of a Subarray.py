# Problem: XOR Queries of a Subarray
# Description: You are given an array `arr` and a list of queries `queries` where each query is represented as a list `[x, y]`. For each query, the task is to find the XOR of elements from index `x` to `y` in the array `arr`.

from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        Given an array 'arr' and a list of queries, this function returns the XOR of elements 
        between each query range [x, y].

        :param arr: List of integers.
        :param queries: List of queries where each query is a list of two integers [x, y].
        :return: List of results, where each result is the XOR of elements between indices x and y.
        """
        n = len(arr)
        # Create an auxiliary array where xor[i] stores the XOR from 0 to i-1
        xor = [0] * (n + 1)
        
        # Fill the XOR array
        for i in range(n):
            xor[i + 1] = xor[i] ^ arr[i]
        
        ans = []
        
        # Process each query
        for query in queries:
            x = query[0]
            y = query[1]
            # The XOR for range [x, y] is computed as xor[y+1] ^ xor[x]
            ans.append(xor[x] ^ xor[y + 1])
        
        return ans

# Time Complexity: O(n + m), where n is the length of the array `arr` and m is the number of queries.
# The preprocessing step takes O(n), and each query is processed in constant time O(1).
# Space Complexity: O(n), due to the extra space needed for the `xor` array.

# Example usage:
# solution = Solution()
# arr = [1, 3, 4, 8]
# queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
# print(solution.xorQueries(arr, queries))  # Expected output: [2, 7, 14, 8]
