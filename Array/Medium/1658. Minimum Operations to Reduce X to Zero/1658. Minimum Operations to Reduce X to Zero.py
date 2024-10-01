# Problem: Minimum Operations to Reduce X to Zero
# Description: You are given an integer array nums and an integer x. 
# You need to remove elements from either end of nums until the sum of removed elements equals x. 
# Return the minimum number of operations required to remove elements from the array such that their sum equals x. 
# If it is impossible to remove elements such that their sum equals x, return -1.

from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Finds the minimum number of operations to reduce x to zero by removing elements from the ends of nums.

        :param nums: List[int], the list of integers.
        :param x: int, the target sum to achieve by removing elements.
        :return: int, the minimum number of operations or -1 if impossible.
        """
        co = float('inf')  # Initialize the count of operations to infinity
        pref_sum = [nums[0]]  # Prefix sum array
        
        for i in range(1, len(nums)):
            if pref_sum[-1] == x:
                co = min(co, i)
            pref_sum.append(pref_sum[-1] + nums[i])  # Build prefix sum
        
        suff_sum = [nums[-1]]  # Suffix sum array
        for j in range(len(nums) - 2, -1, -1):
            if suff_sum[-1] == x:
                co = min(len(nums) - j - 1, co)
            suff_sum.append(suff_sum[-1] + nums[j])  # Build suffix sum
        
        suff_sum = suff_sum[::-1]  # Reverse suffix sum
        
        pref_dict = {sum_: idx for idx, sum_ in enumerate(pref_sum)}  # Dictionary for prefix sums
        pref_dict[0] = -1  # Handle the case for prefix sum of zero
        
        for j, suffix_sum in enumerate(suff_sum):
            remaining = x - suffix_sum  # Calculate remaining sum needed
            if remaining in pref_dict:  # Check if remaining sum exists in prefix sums
                operations = pref_dict[remaining] + 1 + (len(nums) - j)  # Calculate total operations
                co = min(co, operations)  # Update minimum operations
                
        return co if co != float('inf') and co <= len(nums) else -1  # Return result

# Time Complexity: O(n), where n is the length of the nums array, as we iterate through the array twice.
# Space Complexity: O(n), for storing prefix and suffix sums.

# Example usage:
# solution = Solution()
# print(solution.minOperations([1, 1, 4, 2, 3], 5))  # Expected output: 2
# print(solution.minOperations([5, 6, 7, 8, 9], 4))  # Expected output: -1
