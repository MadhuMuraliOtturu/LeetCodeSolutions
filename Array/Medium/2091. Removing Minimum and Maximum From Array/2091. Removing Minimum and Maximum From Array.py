# Problem: Minimum Number of Deletions to Ensure Array is Sorted
# Description: Given a list of integers, determine the minimum number of deletions required to ensure 
# that the maximum and minimum values are separated by at least one index in the remaining list.

class Solution(object):
    def minimumDeletions(self, nums):
        """
        Computes the minimum number of deletions required to ensure the maximum and minimum values in the list
        are separated by at least one index.

        :param nums: List[int], the list of integers.
        :return: Integer, the minimum number of deletions required.
        """
        # Initialize indices for maximum and minimum values
        max_ind = 0
        min_ind = 0
        
        # Initialize values for maximum and minimum
        maxi = nums[0]
        mini = nums[0]
        
        # Traverse through the list to find max/min values and their indices
        for i in range(1, len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
                max_ind = i
            if nums[i] < mini:
                mini = nums[i]
                min_ind = i
        
        # Ensure min_ind is always less than max_ind
        if min_ind > max_ind:
            min_ind, max_ind = max_ind, min_ind
        
        # Calculate the number of deletions needed
        min_back = len(nums) - min_ind
        max_front = max_ind + 1
        min_ind_back = min_ind + (len(nums) - max_ind) + 1
        
        # Return the minimum deletions needed from all cases
        return min(min_back, max_front, min_ind_back)

## Time Complexity: O(N), where N is the number of elements in the list.
## Space Complexity: O(1), constant space used.

# Example usage:
# solution = Solution()
# print(solution.minimumDeletions([1, 3, 2, 7, 6]))  
# Expected output: 3, which is the minimum number of deletions required.
