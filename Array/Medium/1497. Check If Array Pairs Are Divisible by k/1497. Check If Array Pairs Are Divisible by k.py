# Problem: Check if Array Pairs Are Divisible by k
# Description: Given an array of integers `arr` and an integer `k`, the task is to check if the array can be rearranged such that 
# the sum of every pair of integers is divisible by `k`. Return True if possible, otherwise False.

from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """
        Checks if array elements can be paired such that their sum is divisible by k.

        :param arr: List[int], the array of integers.
        :param k: int, the divisor.
        :return: Boolean, True if the array can be rearranged to form pairs whose sum is divisible by k, False otherwise.
        """
        d = {}        
        for i in arr:
            r = i % k
            if r < 0:
                r += k  
            if r not in d:
                d[r] = 1
            else:
                d[r] += 1
        
        for j in d:
            x = (k - j) 
            if x in d:
                if d[x] != d[j]:
                    return False
            else:
                if j == 0 and d[j] % 2 == 0:
                    pass  
                else:
                    return False
        
        return True

## Time Complexity: O(n), where n is the length of the array. We iterate through the array once to populate the frequency map and then check the conditions for pair formation.
## Space Complexity: O(k), since we're using a dictionary to store remainder frequencies which could at most have k different values.

# Example usage:
# solution = Solution()
# print(solution.canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))  # Expected output: True
# print(solution.canArrange([1, 2, 3, 4, 5, 6], 7))  # Expected output: True
# print(solution.canArrange([1, 2, 3, 4, 5, 6], 10))  # Expected output: False
