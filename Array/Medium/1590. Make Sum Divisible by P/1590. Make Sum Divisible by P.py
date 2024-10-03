# Problem: Minimum Subarray Removal to Make Sum Divisible by `p`
# Description:
# Given an array `nums` of non-negative integers and a positive integer `p`, the task is to remove the smallest subarray such that the sum of the remaining elements is divisible by `p`.
# If this is not possible, return -1.
# The function returns the length of the smallest subarray to be removed.

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        Finds the length of the smallest subarray to be removed such that the sum of the remaining elements is divisible by `p`.

        :param nums: List[int], a list of non-negative integers.
        :param p: int, the divisor.
        :return: int, the length of the smallest subarray to remove. If no such subarray exists, return -1.
        """
        total = sum(nums) % p  # Calculate the total sum modulo p
        if total == 0:
            return 0  # If the total sum is divisible by p, no need to remove any subarray

        n = len(nums)
        d = {0: -1}  # Dictionary to store prefix sums and their indices
        pref_sum = 0  # Prefix sum modulo p
        mini = n  # Initialize the minimum subarray length as the array length

        for i in range(n):
            pref_sum = (pref_sum + nums[i]) % p  # Update the prefix sum
            d[pref_sum] = i  # Store the index for the current prefix sum
            needed = (pref_sum - total + p) % p  # Calculate the required prefix sum

            if needed in d:
                mini = min(mini, i - d[needed])  # Update the minimum subarray length

        return -1 if mini == n else mini  # Return -1 if no valid subarray is found

# Time Complexity: O(n), where `n` is the length of the input array `nums`.
# The function traverses the array once, making it linear in terms of time.
# Space Complexity: O(n), due to the additional space used by the dictionary storing the prefix sums.

# Example usage:
# solution = Solution()
# print(solution.minSubarray([3,1,4,2], 6))  # Expected output: 1
# print(solution.minSubarray([6,3,5,2], 9))  # Expected output: 2
