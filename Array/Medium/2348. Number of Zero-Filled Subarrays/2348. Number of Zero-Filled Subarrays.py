# Problem: Zero-Filled Subarrays
# Description: Given an integer array `nums`, return the number of zero-filled subarrays. A subarray is a contiguous non-empty sequence of elements within an array.

class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        Returns the total number of zero-filled subarrays in the input list `nums`.

        :param nums: List of integers.
        :return: Number of zero-filled subarrays.
        """
        if nums[0] == 0:
            prev = True  # A flag to track if we are in a zero-filled subarray
            co = 1       # Counter for the length of the current zero-filled subarray
        else:
            prev = False
            co = 0
        
        final = 0  # Final count of all zero-filled subarrays
        
        # Traverse the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] == 0:
                if prev:
                    co += 1
                else:
                    co = 1
                prev = True
            else:
                if co > 0:
                    # Calculate the number of subarrays from the current streak of zeros
                    final = final + co * (co + 1) // 2
                co = 0
                prev = False
        
        # Final calculation if the last subarray ends with zeros
        if prev and co > 0:
            final = final + co * (co + 1) // 2
        
        return final

# Time Complexity: O(n), where n is the length of the array `nums`. We traverse the array once.
# Space Complexity: O(1), as we use a constant amount of extra space.

# Example usage:
# solution = Solution()
# nums = [1, 0, 0, 1, 0]
# print(solution.zeroFilledSubarray(nums))  # Expected output: 3
