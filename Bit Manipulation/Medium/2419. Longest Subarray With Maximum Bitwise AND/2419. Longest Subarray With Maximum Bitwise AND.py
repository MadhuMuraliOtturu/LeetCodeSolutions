# Problem: Longest Subarray of Maximum Element
# Description: Given an array `nums`, the task is to find the length of the longest subarray that contains the maximum element in the array.

class Solution(object):
    def longestSubarray(self, nums):
        """
        This function returns the length of the longest subarray that contains 
        the maximum element in the given list 'nums'.

        :param nums: List of integers.
        :return: Integer representing the length of the longest subarray that contains the maximum element.
        """
        maxs = 0  # Variable to store the maximum element in the array
        ans = 0   # Variable to store the length of the longest subarray
        curr = 0  # Counter for the current subarray of maximum element
        
        # Iterate through the array to find the longest subarray of maximum element
        for i in range(len(nums)):
            if maxs < nums[i]:
                maxs = nums[i]   # Update the maximum element
                curr = ans = 1   # Reset counters since a new maximum is found
            elif maxs == nums[i]:
                curr += 1        # Extend the current subarray if the element is equal to the maximum
            else:
                curr = 0         # Reset the current subarray count if the element is not the maximum
            
            ans = max(ans, curr) # Update the longest subarray count
        
        return ans

# Time Complexity: O(n), where n is the length of the input array `nums`. We traverse the array once.
# Space Complexity: O(1), since we are using constant extra space regardless of the input size.

# Example usage:
# solution = Solution()
# nums = [1, 2, 2, 3, 3, 3, 2]
# print(solution.longestSubarray(nums))  # Expected output: 3
