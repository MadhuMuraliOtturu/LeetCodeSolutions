# Problem: Kth Largest Level Sum in a Binary Tree
# Description:
# Given the root of a binary tree and an integer k, return the kth largest sum among all the levels of the tree.
# If there are fewer than k levels in the tree, return -1.
# 
# Each level in the tree consists of the sum of the values of the nodes at that level.
# The root is at level 1, the children of the root are at level 2, and so on.
# 
# The task is to return the sum of the kth largest level in the binary tree.
# 
# Example:
# Input: [root] = [5, 2, 9, 1, 3, null, 7], k = 2
# Output: 15  (The sums are: 5, 5, 15, and the 2nd largest is 15.)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        """
        Calculates the kth largest level sum in a binary tree.

        :param root: TreeNode, the root of the binary tree.
        :param k: int, the kth largest level sum to find.
        :return: int, the kth largest sum, or -1 if the number of levels is less than k.
        """
        if not root:
            return -1
        
        level = 0
        queue = [root]
        level_sums = []

        # Perform level-order traversal to calculate sums at each level
        while queue:
            current_sum = 0
            for i in range(len(queue)):
                node = queue.pop(0)
                current_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sums.append(current_sum)
            level += 1

        # Sort the level sums in descending order and find the kth largest sum
        level_sums_sorted = sorted(level_sums, reverse=True)
        return level_sums_sorted[k-1] if level >= k else -1

# Time Complexity: O(n log n), where n is the number of levels in the tree. Sorting the level sums takes O(n log n).
# Space Complexity: O(n), where n is the number of levels, as we store the level sums.

# Example usage:
# solution = Solution()
# root = TreeNode(5)
# root.left = TreeNode(2)
# root.right = TreeNode(9)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.right = TreeNode(7)
# print(solution.kthLargestLevelSum(root, 2))  # Expected output: 15
