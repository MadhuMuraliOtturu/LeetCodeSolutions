# Problem: Replace Values in Binary Tree
# Description:
# You are given the root of a binary tree where each node has a value.
# Replace each node's value with the sum of its cousin nodes' values, where cousin nodes are the nodes at the same depth but have different parents.
# 
# A node is considered a cousin if it is at the same depth as the current node and has a different parent.
# The task is to replace each node's value with the sum of its cousin nodes.
# 
# Example:
# Input: [root] = [5, 4, 9, 1, 10, 3], Output: [15, 0, 0, 0, 0, 0]
# 
# The new values of the tree after replacing the values with the sum of cousin nodes.

from typing import Optional
from collections import defaultdict

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution:
    """
    Replaces each node value in a binary tree with the sum of its cousin nodes' values.

    :param root: TreeNode, the root of the binary tree.
    :return: TreeNode, the root of the binary tree with updated values.
    """
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        depth = {}

        def parent_depth(root, parent, co):
            """
            Helper function to calculate the depth sums and track parent contributions to each depth.

            :param root: The current node being processed.
            :param parent: The parent node of the current node.
            :param co: The current depth of the node in the tree.
            """
            if root is not None:
                if co not in depth:
                    depth[co] = [0, {}]
                
                depth[co][0] += root.val  # Total sum of values at depth `co`
                
                if parent not in depth[co][1]:
                    depth[co][1][parent] = 0
                depth[co][1][parent] += root.val  # Track sum contributed by the parent
                
                parent_depth(root.left, root, co + 1)
                parent_depth(root.right, root, co + 1)

        parent_depth(root, None, 0)

        def update_cousin_values(root, parent, co):
            """
            Update each node's value with the sum of cousin nodes' values at the same depth.

            :param root: The current node being processed.
            :param parent: The parent node of the current node.
            :param co: The current depth of the node in the tree.
            """
            if root is not None:
                cousin_sum = depth[co][0] - depth[co][1].get(parent, 0)  # Sum of cousins at depth `co`
                root.val = cousin_sum
                
                update_cousin_values(root.left, root, co + 1)
                update_cousin_values(root.right, root, co + 1)

        update_cousin_values(root, None, 0)
        
        return root

# Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node twice, once to calculate depth sums and once to update values.
# Space Complexity: O(n), where n is the number of nodes. We store depth sums and parent contributions for each node.

# Example usage:
# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(9)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(10)
# root.right.left = TreeNode(3)
# solution = Solution()
# updated_root = solution.replaceValueInTree(root)
# # Now the tree root and its children will have updated values based on cousin sums.
