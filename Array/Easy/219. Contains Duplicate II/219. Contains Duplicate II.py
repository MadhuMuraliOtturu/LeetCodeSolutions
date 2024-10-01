# Problem: Contains Duplicate II
# Description: Given an array of integers `nums` and an integer `k`, 
# the task is to find out if there are two distinct indices `i` and `j` in the array 
# such that nums[i] == nums[j] and the absolute difference between `i` and `j` is at most `k`.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        Checks if the given array contains two distinct indices such that the values at these indices are the same 
        and their absolute difference is less than or equal to k.
        
        :param nums: List[int], list of integers to check.
        :param k: int, the maximum allowed difference between indices.
        :return: bool, True if such a pair exists, False otherwise.
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)
                if abs(d[nums[i]][-2] - d[nums[i]][-1]) <= k:  # Check if the condition is met
                    return True
        return False

## Time Complexity: O(n), where n is the length of the nums list. We go through the list once, and the operations with the dictionary take constant time.
## Space Complexity: O(n), due to the space required to store the indices of elements in the dictionary.

# Example usage:
# solution = Solution()
# print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))  # Expected output: True
# print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))  # Expected output: True
# print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Expected output: False
