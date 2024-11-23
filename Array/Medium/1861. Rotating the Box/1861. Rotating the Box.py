# Problem: Rotate the Box
# Description:
# Given a 2D grid `box` representing a box filled with stones (`#`), obstacles (`*`), 
# and empty spaces (`.`), rotate the box 90 degrees clockwise. Stones fall to the bottom
# due to gravity before rotation.
#
# Example:
# Input: box = [["#", ".", "#"], [".", "#", "*"], ["#", "#", "."]]
# Output: [[".", "#", "#"], ["#", "#", "."], ["#", ".", "*"]]
#
# Constraints:
# - 1 <= box.length, box[0].length <= 50
# - box[i][j] is either '#', '*', or '.'

from typing import List

class Solution:
    """
    Rotates a box 90 degrees clockwise after simulating gravity.
    
    :param box: List[List[str]] - The 2D grid representing the box.
    :return: List[List[str]] - The rotated box.
    """
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        # Simulate gravity within each row
        for i in range(m):
            rightmost = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == '#':
                    if j != rightmost:
                        box[i][j] = '.'
                        box[i][rightmost] = '#'
                    rightmost -= 1
                elif box[i][j] == '*':
                    rightmost = j - 1
        
        # Create the rotated grid
        rotated = [['.'] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = box[i][j]
        
        return rotated

# Time Complexity: O(m * n) - Traverses all elements for gravity and rotation.
# Space Complexity: O(m * n) - Space for the rotated box.

# Example usage:
# solution = Solution()
# box = [["#", ".", "#"], [".", "#", "*"], ["#", "#", "."]]
# print(solution.rotateTheBox(box))
# Output: [[".", "#", "#"], ["#", "#", "."], ["#", ".", "*"]]
