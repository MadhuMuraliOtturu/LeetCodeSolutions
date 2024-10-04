# Problem: Divide Players into Pairs with Equal Skill
# Description:
# Given an array `nums` representing the skill levels of players, the task is to divide the players into pairs such that each pair has an equal combined skill level. 
# The score of a pair is calculated as the product of the skill levels of the two players. Return the sum of the scores of all pairs if it's possible to divide the players in this manner, otherwise return -1.

class Solution:
    def dividePlayers(self, nums: List[int]) -> int:
        """
        Divides players into pairs such that each pair has the same combined skill level. 
        Returns the sum of the product of skill levels for each pair if possible, otherwise returns -1.

        :param nums: List[int], a list of integers representing the skill levels of the players.
        :return: int, the sum of the products of paired players' skill levels or -1 if no valid pairing exists.
        """
        n = len(nums)
        nums.sort()  # Sort the skill levels
        left = 0
        right = n - 1
        co = 0
        prev = -1  # Used to store the sum of the first pair's skill levels

        while left < right:
            if prev == -1:
                # For the first pair, set the initial sum of skill levels
                prev = nums[left] + nums[right]
                co += nums[left] * nums[right]  # Calculate the product for the first pair
            else:
                if nums[left] + nums[right] != prev:
                    return -1  # If any pair doesn't match the sum of the first pair, return -1
                else:
                    co += nums[left] * nums[right]  # Add the product of the current pair

            left += 1
            right -= 1

        return co  # Return the total sum of all products

# Time Complexity: O(n log n), where `n` is the length of the input array `nums`.
# This is due to the sorting operation, which dominates the time complexity.
# Space Complexity: O(1), since the sorting is done in place and only a few extra variables are used.

# Example usage:
# solution = Solution()
# print(solution.dividePlayers([3,2,5,1,3,4]))  # Expected output: 22
# print(solution.dividePlayers([1,2,3,4]))      # Expected output: -1
