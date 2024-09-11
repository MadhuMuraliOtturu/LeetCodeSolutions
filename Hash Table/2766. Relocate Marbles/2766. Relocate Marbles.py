# Problem: Relocate Marbles
# Description: Given a list `nums` representing the positions of marbles, and two lists `moveFrom` and `moveTo`
# representing moves from a marble's current position to a new position, perform the moves and return 
# the final positions of the marbles sorted in ascending order.

class Solution(object):
    def relocateMarbles(self, nums, moveFrom, moveTo):
        """
        Relocates marbles from positions specified in `moveFrom` to new positions in `moveTo`.

        :param nums: List of integers, initial positions of the marbles.
        :param moveFrom: List of integers, current positions of marbles to be moved.
        :param moveTo: List of integers, new positions to move the marbles to.
        :return: List of integers, sorted final positions of marbles.
        """
        new_nums = set(nums)  # Using a set to track unique positions
        for i in range(len(moveFrom)):
            x = moveFrom[i]
            y = moveTo[i]
            if x in new_nums:
                new_nums.remove(x)  # Remove the marble from its current position
                new_nums.add(y)     # Add the marble to its new position
        return sorted(list(new_nums))  # Return the sorted list of final positions

## Time Complexity: O(K + N log N), where K is the length of `moveFrom` and `moveTo`, and N is the number of unique positions.
## Space Complexity: O(N), for storing the set of unique positions.

# Example usage:
# solution = Solution()
# nums = [1, 3, 5]
# moveFrom = [1, 3]
# moveTo = [2, 4]
# print(solution.relocateMarbles(nums, moveFrom, moveTo))  
# Expected output: [2, 4, 5]
