# Problem: Max Score Indices
# Description: Given a binary array `nums`, find all the indices that yield the maximum score when 
# splitting the array into two parts: left of the index containing all zeros and right of the index 
# containing all ones.

from typing import List

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        """
        Finds all indices where the score, defined as the sum of zeros on the left side and ones on the right side,
        is maximized when splitting the array at these indices.
        
        :param nums: List of binary integers (0s and 1s).
        :return: List of integers representing indices where the maximum score is achieved.
        """
        zero_pref = []
        one_suff = []
        
        # Build zero_pref array to track cumulative zeros on the left side
        for i in range(len(nums)):
            if nums[i] == 0:
                if i == 0:
                    zero_pref.append(1)
                else:
                    zero_pref.append(zero_pref[-1] + 1)
            else:
                if i == 0:
                    zero_pref.append(0)
                else:
                    zero_pref.append(zero_pref[-1])
        
        # Build one_suff array to track cumulative ones on the right side
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == 1:
                if j == len(nums) - 1:
                    one_suff.append(1)
                else:
                    one_suff.append(one_suff[-1] + 1)
            else:
                if j == len(nums) - 1:
                    one_suff.append(0)
                else:
                    one_suff.append(one_suff[-1])
        
        # Reverse one_suff to align with indices
        one_suff = one_suff[::-1]
        
        # Dictionary to store scores and corresponding indices
        d = {}
        maxs = 0
        
        # Calculate scores for each possible split index
        for i in range(len(nums) + 1):
            if i == 0:
                zeros = 0
                ones = one_suff[i] if i < len(nums) else 0
            elif i == len(nums):
                zeros = zero_pref[-1]
                ones = 0
            else:
                zeros = zero_pref[i - 1]
                ones = one_suff[i]
            
            co = zeros + ones
            maxs = max(co, maxs)
            if co not in d:
                d[co] = [i]
            else:
                d[co].append(i)
    
        return d[maxs]

# Time Complexity: O(n), where n is the length of the `nums` array. We loop through the array 
# twice, once for building the zero_pref and once for building the one_suff arrays.
# Space Complexity: O(n), to store the prefix and suffix arrays.

# Example usage:
# solution = Solution()
# nums = [0,1,0,1,0]
# print(solution.maxScoreIndices(nums))  # Expected output: Indices with maximum score.
