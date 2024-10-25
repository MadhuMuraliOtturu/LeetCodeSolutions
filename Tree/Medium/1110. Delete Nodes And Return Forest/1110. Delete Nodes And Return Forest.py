from typing import Optional, List

# Problem: Delete Nodes and Return Forest
# Description:
# Given the root of a binary tree and a list of integers `to_delete`, delete the nodes with values in `to_delete`
# from the tree. After deleting a node, its children become new roots of separate trees in the resulting forest.
# Return a list of the roots of the trees in the forest.
#
# Example:
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4], [6], [7]]
#
# Constraints:
# - The number of nodes in the tree is at most 1000.
# - Each node has a unique value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Solution to delete specified nodes from a binary tree and return the forest of remaining trees.

    :param root: Optional[TreeNode], the root of the binary tree.
    :param to_delete: List[int], list of node values to delete.
    :return: List[TreeNode], list of roots of the trees in the forest after deletion.
    """
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.l = []
        to_delete_set = set(to_delete)

        def delete(root: Optional[TreeNode], parent: Optional[TreeNode], dir: str):
            """
            Recursive helper to traverse and delete nodes. If a node's value is in `to_delete`, it will be removed.
            Otherwise, it is added as a new root if it has no parent.
            
            :param root: Optional[TreeNode], the current node in traversal.
            :param parent: Optional[TreeNode], parent of the current node.
            :param dir: str, direction from parent ('L' for left, 'R' for right).
            """
            if root is not None:
                if root.val in to_delete_set:
                    if dir == 'L':
                        parent.left = None
                    elif dir == 'R':
                        parent.right = None

                    delete(root.left, None, 'L')
                    delete(root.right, None, 'R')
                else:
                    if parent is None:
                        self.l.append(root)

                    delete(root.left, root, 'L')
                    delete(root.right, root, 'R')

        delete(root, None, '')
        return self.l

# Time Complexity: O(n), where n is the number of nodes in the tree, since each node is visited once.
# Space Complexity: O(n) for storing the resulting list of root nodes in the forest.

# Example usage:
# root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
# to_delete = [3, 5]
# solution = Solution()
# print(solution.delNodes(root, to_delete))  # Output: [TreeNode objects representing [1, 2, null, 4], [6], [7]]
