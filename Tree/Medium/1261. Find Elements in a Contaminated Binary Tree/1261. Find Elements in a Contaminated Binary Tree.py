from typing import Optional

# Problem: Recover a Binary Tree Contaminated with -1 Values
# Description:
# You are given a binary tree where each node contains either -1 or an integer.
# The task is to "recover" the tree by assigning values such that the root starts
# at 0, left children are 2 * parent + 1, and right children are 2 * parent + 2.
# You should also be able to find if a specific target value exists in the recovered tree.
#
# Implement the FindElements class:
# - `__init__(self, root: Optional[TreeNode])`: Initializes the tree with recovered values.
# - `find(self, target: int) -> bool`: Returns True if target is in the recovered tree, False otherwise.
#
# Example:
# Input: root = [-1,-1,-1,-1,null,-1]
# FindElements obj = FindElements(root)
# Output: obj.find(1) -> True; obj.find(3) -> False

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    """
    Recovers a binary tree by assigning values based on specific rules and supports querying if a value exists.

    :param root: Optional[TreeNode], the root of the contaminated binary tree.
    """
    def __init__(self, root: Optional[TreeNode]):
        self.s = set()
        if root is not None:
            root.val = 0  
            self.s.add(0)
            self.recover(root)

    def recover(self, root: Optional[TreeNode], parent: Optional[TreeNode] = None, dir: str = ''):
        """
        Recursively recovers the tree values by calculating the values based on left/right child rules.
        
        :param root: Optional[TreeNode], current node in the tree.
        :param parent: Optional[TreeNode], parent of the current node.
        :param dir: str, direction from parent to current node ('L' for left, 'R' for right).
        """
        if root is not None:
            if parent is not None:
                if dir == 'L':
                    value = 2 * parent.val + 1
                elif dir == 'R':
                    value = 2 * parent.val + 2
                root.val = value
                self.s.add(value)
            self.recover(root.left, root, 'L')
            self.recover(root.right, root, 'R')

    def find(self, target: int) -> bool:
        """
        Checks if a target value is present in the recovered tree.
        
        :param target: int, value to search for in the tree.
        :return: bool, True if the target is present, otherwise False.
        """
        return target in self.s

# Time Complexity:
# - __init__: O(n), where n is the number of nodes in the tree, for traversing and assigning values.
# - find: O(1) for checking membership in a set.
# Space Complexity: O(n) for storing recovered values in a set.

# Example usage:
# root = TreeNode(-1, TreeNode(-1), TreeNode(-1))
# obj = FindElements(root)
# print(obj.find(1))  # Output: True
# print(obj.find(3))  # Output: False
