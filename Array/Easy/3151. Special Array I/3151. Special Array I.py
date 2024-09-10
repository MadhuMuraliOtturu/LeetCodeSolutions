# Problem: Check if the Array is Special
# Description: Given an array of integers, check if the array is "special." An array is considered special 
# if all consecutive elements have alternating parity (i.e., one is even and the next is odd, or vice versa).

class Solution(object):
    def isArraySpecial(self, nums):
        """
        Determines if an array has alternating even and odd numbers.

        :param nums: List[int], the array of integers.
        :return: Boolean, True if the array is special (alternating parity), False otherwise.
        """
        for i in range(len(nums) - 1):
            if (nums[i] % 2 == 0 and nums[i + 1] % 2 == 1) or (nums[i] % 2 == 1 and nums[i + 1] % 2 == 0):
                pass
            else:
                return False
        return True

## Time Complexity: O(N), where N is the length of the array.
## Space Complexity: O(1), as no extra space is used.

# Example usage:
# solution = Solution()
# print(solution.isArraySpecial([1, 2, 3, 4]))  # Expected output: True, since the array alternates between odd and even.
