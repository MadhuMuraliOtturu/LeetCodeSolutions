from typing import Optional

# Problem: Minimum Number of Operations to Sort Each Level of a Binary Tree
# Description:
# Given a binary tree root, the goal is to perform a minimum number of swaps on each level of the tree
# so that all values at each level are sorted in non-decreasing order. Each swap can be used to
# exchange any two nodes within the same level.
#
# The task is to return the minimum number of swaps required to sort each level.
#
# Example:
# Input: root = [1,4,3,7,6,8,5,null,null,null,null,null,null,9,null]
# Output: 3
#
# Explanation:
# Sorting the first level (1 swap), second level (1 swap), and third level (1 swap) gives a total of 3 swaps.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Calculates the minimum number of swaps required to sort each level of a binary tree.
    
    :param root: Optional[TreeNode], the root of the binary tree.
    :return: int, the minimum number of swaps needed.
    """
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def minSwap(arr):
            """
            Helper function to find the minimum number of swaps to sort an array.

            :param arr: List[int], the array to sort.
            :return: int, the minimum number of swaps.
            """
            n = len(arr)
            if n <= 1:
                return 0

            ans = 0
            temp = arr.copy()
            h = {}

            # Sort a copy of arr to determine final positions
            temp.sort()

            # Create a hash map to remember original indices
            for i in range(n):
                h[arr[i]] = i

            for i in range(n):
                if arr[i] != temp[i]:
                    ans += 1
                    init = arr[i]

                    # Swap current element with its correct position
                    arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]

                    # Update the hash map
                    h[init] = h[temp[i]]
                    h[temp[i]] = i

            return ans
        
        # Initialize total swap count
        self.co = 0
        queue = [root]
        
        # Traverse each level of the binary tree
        while queue:
            level_arr = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_arr.append(node.val)
            
            # Add the swaps needed for the current level
            self.co += minSwap(level_arr)
        
        return self.co

# Time Complexity: O(n log n), where n is the number of nodes in the tree, due to sorting operations per level.
# Space Complexity: O(h + m), where h is the height of the tree and m is the number of nodes at the largest level, due to level-wise traversal.

# Example usage:
# tree = TreeNode(1, TreeNode(4, TreeNode(7), TreeNode(6)), TreeNode(3, TreeNode(8), TreeNode(5, TreeNode(9))))
# solution = Solution()
# result = solution.minimumOperations(tree)
# print(result)  # Output: 3
