# Problem: Longest ZigZag Path in a Binary Tree
# Description:
# Given a binary tree `root`, the goal is to find the length of the longest ZigZag path in the tree.
# A ZigZag path starts from any node and alternates between moving left and right.
# The length of a ZigZag path is defined as the number of edges in the path.
#
# The task is to return the length of the longest ZigZag path in the given binary tree.
#
# Example:
# Input: root = [1,null,1,1,1,null,null,1,1,null,null,null,0,0]
# Output: 3
#
# Explanation: 
# The longest ZigZag path starts at the root's right child, continues left, then right, then left, resulting in 3 edges.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Finds the length of the longest ZigZag path in a binary tree.
    
    :param root: Optional[TreeNode], the root of the binary tree.
    :return: int, the length of the longest ZigZag path in the tree.
    """
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.co = 0
        
        def helper(node, direction, vals):
            if node is not None:
                # Update the maximum ZigZag path length
                self.co = max(self.co, vals)
                
                # Continue ZigZagging: alternate between left and right
                if direction == 'R':
                    helper(node.left, 'L', vals + 1)  # Go left after right
                    helper(node.right, 'R', 1)        # Reset and go right again
                elif direction == 'L':
                    helper(node.right, 'R', vals + 1) # Go right after left
                    helper(node.left, 'L', 1)         # Reset and go left again

        # Start ZigZag from the left and right child of the root
        helper(root.left, 'L', 1)
        helper(root.right, 'R', 1)
        
        return self.co

# Time Complexity: O(n), where n is the total number of nodes in the tree. Each node is visited once.
# Space Complexity: O(h), where h is the height of the tree, due to the recursion stack.

# Example usage:
# tree = TreeNode(1, None, TreeNode(1, TreeNode(1, None, None), TreeNode(1, TreeNode(1), None)))
# solution = Solution()
# result = solution.longestZigZag(tree)
# print(result)  # Output: 3
