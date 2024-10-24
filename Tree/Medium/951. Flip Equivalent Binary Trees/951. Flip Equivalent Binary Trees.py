# Problem: Flip Equivalent Binary Trees
# Description:
# Given two binary trees `root1` and `root2`, the goal is to determine if they are flip equivalent.
# Two binary trees are considered flip equivalent if they are structurally identical or 
# can be made identical by flipping certain children at some nodes. 
#
# A flip operation swaps the left and right children of a node.
#
# The task is to check if two given binary trees are flip equivalent.
#
# Example:
# Input: root1 = [1,2,3,4,5,6,None,None,None,7,8], root2 = [1,3,2,None,6,4,5,None,None,None,None,8,7]
# Output: True
#
# Explanation: 
# - You can flip the subtrees of the node with value 1 (the root), and the trees become identical.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Determines if two binary trees are flip equivalent.
    
    :param root1: Optional[TreeNode], the root of the first binary tree.
    :param root2: Optional[TreeNode], the root of the second binary tree.
    :return: bool, True if the two binary trees are flip equivalent, False otherwise.
    """
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Both trees are empty
        if root1 is None and root2 is None:
            return True
        # One tree is empty and the other is not
        if root1 is None or root2 is None:
            return False
        # The values of the roots differ
        if root1.val != root2.val:
            return False
        
        # Recursively check both configurations: without flip and with flip
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

# Time Complexity: O(n), where n is the total number of nodes in both trees. Each node is visited once.
# Space Complexity: O(h), where h is the height of the tree. This is the space used by the recursion stack.

# Example usage:
# tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, None, TreeNode(6)))
# tree2 = TreeNode(1, TreeNode(3, None, TreeNode(6)), TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(8), TreeNode(7))))
# solution = Solution()
# result = solution.flipEquiv(tree1, tree2)
# print(result)  # Output: True
