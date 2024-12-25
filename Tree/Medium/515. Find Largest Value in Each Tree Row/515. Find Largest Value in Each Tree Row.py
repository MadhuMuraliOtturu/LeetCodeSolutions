# Problem: Find Largest Values in Each Tree Row
# Description:
# Given the root of a binary tree, return an array of the largest value in each row of the tree.
#
# Example:
# Input: root = [1, 3, 2, 5, 3, None, 9]
# Output: [1, 3, 9]
# Explanation:
# - Row 1: Largest value is 1
# - Row 2: Largest value is 3
# - Row 3: Largest value is 9
#
# Constraints:
# - The number of nodes in the tree is in the range [0, 10^4].
# - -2^31 <= Node.val <= 2^31 - 1

from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        Finds the largest value in each row of the binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: A list of the largest values in each row of the tree.
        """
        if root is None:
            return []

        ans = []
        queue = [root]
        while queue:
            maxi_ = float("-inf")
            for i in range(len(queue)):
                x = queue.pop(0)
                maxi_ = max(maxi_, x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            ans.append(maxi_)

        return ans

# Time Complexity: O(N), where N is the number of nodes in the tree.
# Space Complexity: O(M), where M is the maximum width of the tree (max number of nodes in a level).
