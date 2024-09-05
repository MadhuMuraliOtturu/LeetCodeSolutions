# Problem: Rearrange Array Elements to Be Alternating
# https://leetcode.com/problems/rearrange-array-elements-to-be-alternating/

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        Rearranges the elements of the array such that the array alternates between 
        increasing and decreasing values.

        :param nums: List[int], the input list of integers to be rearranged.
        :return: List[int], the rearranged list with alternating increasing and decreasing values.
        """
        # Iterate over the array to check for the pattern and rearrange elements
        for i in range(1, len(nums) - 1):
            # Check if the current element is in a local minimum or maximum
            if ((nums[i-1] < nums[i] and nums[i] < nums[i+1]) 
            or  (nums[i-1] > nums[i] and nums[i] > nums[i+1])):
                # Swap the current element with the next element to fix the pattern
                nums[i], nums[i+1] = nums[i+1], nums[i]
                
        return nums

## Time Complexity: O(N), where N is the number of elements in the list.
## Space Complexity: O(1), as the rearrangement is done in place.

# Example usage:
# solution = Solution()
# print(solution.rearrangeArray([1, 2, 3, 4, 5]))  # Example output could be [1, 3, 2, 4, 5]
