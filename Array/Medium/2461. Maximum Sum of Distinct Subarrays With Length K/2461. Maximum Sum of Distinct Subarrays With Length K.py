# Problem: Maximum Sum of Distinct Subarray With Length K
# Description: Given an array `nums` and an integer `k`, find the maximum sum of a subarray of length `k`
# such that all elements of the subarray are distinct. If no such subarray exists, return 0.

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        Finds the maximum sum of a subarray of length `k` with all distinct elements.
        
        :param nums: List of integers.
        :param k: Integer, the required length of the subarray.
        :return: Integer, the maximum sum of such a subarray or 0 if no such subarray exists.
        """
        sums = 0
        i = 0
        d = {}
        co = 0
        
        # Initialize the first window
        while i < k:
            if nums[i] not in d:
                d[nums[i]] = 1
                co += nums[i]
            else:
                d[nums[i]] += 1
                co += nums[i]
            i += 1
        
        # Check if the first window has distinct elements
        if len(d) == k:
            sums = co
        
        # Slide the window across the array
        while i < len(nums):
            prev_ind = nums[i - k]
            d[prev_ind] -= 1
            if d[prev_ind] == 0:
                del d[prev_ind]
            co -= prev_ind
            
            # Add the new element to the window
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
            co += nums[i]
            
            # Update the maximum sum if the current window has distinct elements
            if len(d) == k:
                sums = max(sums, co)
            
            i += 1
        
        return sums

# Time Complexity: O(n), where n is the number of elements in `nums`. Each element is added and removed 
# from the dictionary at most once.
# Space Complexity: O(k), where k is the size of the sliding window, as we store up to k distinct elements.

# Example usage:
# solution = Solution()
# nums = [1, 2, 3, 4, 2, 5]
# k = 3
# print(solution.maximumSubarraySum(nums, k))  # Expected output: 9 (subarray [2, 3, 4])
