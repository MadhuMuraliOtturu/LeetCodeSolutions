# Problem: Largest Perimeter of a Triangle
# Description: Given an array of integers `nums` representing the lengths of sticks, find the largest perimeter
# of a triangle that can be formed using any three of these sticks. If no such triangle can be formed, return 0.

class Solution(object):
    def largestPerimeter(self, nums):
        """
        Computes the largest perimeter of a triangle that can be formed using any three lengths from the given list.

        :param nums: List[int], the list of stick lengths.
        :return: Integer, the largest perimeter of a triangle that can be formed.
        """
        nums.sort()  # Sort the list in non-decreasing order
        max_val = -1  # Initialize the maximum perimeter to be returned
        co = 0  # Accumulator for the sum of stick lengths
        ind = 0  # Index to keep track of the third side in the perimeter calculation
        
        # Iterate through the list from the beginning to the second last element
        for i in range(len(nums) - 1):
            co += nums[i]  # Accumulate the sum of lengths
            # Check if the accumulated length is greater than the next stick length
            if co > nums[i + 1]:
                max_val = max(max_val, co)  # Update the maximum perimeter found
                ind = i + 1  # Update the index of the third side
        # Add the length of the third side to the maximum perimeter if a valid triangle was found
        if ind != 0:
            max_val += nums[ind]
        
        return max_val  # Return the largest perimeter

## Time Complexity: O(N log N), where N is the number of stick lengths, due to sorting.
## Space Complexity: O(1), constant space used apart from the input.

# Example usage:
# nums = [2, 1, 2]
# solution = Solution()
# print(solution.largestPerimeter(nums))  
# Expected output: 5, since the largest perimeter triangle that can be formed is (2, 2, 1) with a perimeter of 5.
