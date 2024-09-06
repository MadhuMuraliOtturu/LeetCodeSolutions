# Problem: Find the Middle Node of a Singly-Linked List
# Description: Given a linked list, find the middle node. If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        Finds the middle node of the linked list. If there are two middle nodes, returns the second one.

        :param head: ListNode, the head of the singly-linked list.
        :return: ListNode, the middle node of the linked list.
        """
        slow = fast = head
        # Step 1: Use the two-pointer technique to find the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we only use a constant amount of extra space.

# Example usage:
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# solution = Solution()
# middle_node = solution.middleNode(head)  # Expected to return the node with value 3
