# Problem: Largest Number
# Description: Given a list of non-negative integers, arrange them such that they form the largest possible number.

from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        This function rearranges numbers in the list to form the largest possible concatenated number.
        
        :param nums: List[int] - a list of non-negative integers
        :return: str - the largest number possible by concatenating the integers
        """
        # Custom comparator to determine the order of concatenation
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            return 1

        # Convert each integer to string for comparison
        strs = [str(i) for i in nums]

        # Sort the numbers based on the custom comparator
        strs.sort(key=cmp_to_key(compare))

        # Join the sorted strings and return the result as a string
        # Convert to int first to remove leading zeros and back to string
        return str(int("".join(strs)))

# Time Complexity: O(n log n), where n is the length of the list, due to sorting.
# Space Complexity: O(n), for storing the string representations of the numbers.
#
# Example Usage:
# solution = Solution()
# print(solution.largestNumber([3, 30, 34, 5, 9]))
# Output: "9534330"
