# Problem: Delete Node in a Linked List
# Description: Given a node in a singly-linked list, delete that node from the list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        Deletes the given node from the linked list.

        :param node: ListNode, the node to be deleted. This node is guaranteed to not be the last node in the list.
        """
        # Step 1: Copy the value of the next node to the current node
        node.val = node.next.val
        # Step 2: Skip the next node by pointing to the next of next node
        node.next = node.next.next

## Time Complexity: O(1), as we only perform a constant number of operations.
## Space Complexity: O(1), as we do not use any extra space.

# Example usage:
# node = ListNode(4)
# node.next = ListNode(5)
# node.next.next = ListNode(1)
# node.next.next.next = ListNode(9)
# solution = Solution()
# solution.deleteNode(node)  # Deletes the node with value 5
