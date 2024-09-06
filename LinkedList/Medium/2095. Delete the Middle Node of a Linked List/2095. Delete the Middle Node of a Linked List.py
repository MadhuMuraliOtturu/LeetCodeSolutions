# Problem: Delete the Middle Node of a Singly-Linked List
# Description: Given a linked list, delete the middle node. If there are two middle nodes, delete the second middle node.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        Deletes the middle node of the linked list. If there are two middle nodes, deletes the second one.

        :param head: ListNode, the head of the singly-linked list.
        :return: ListNode, the head of the modified list after removing the middle node.
        """
        slow = fast = head
        # Edge case: If the list is empty or has only one node
        if not head or not head.next:
            return None
        
        # Step 1: Use the two-pointer technique to find the middle node
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Delete the middle node
        if prev:
            prev.next = slow.next
        
        return head

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we only use a constant amount of extra space.

# Example usage:
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# solution = Solution()
# new_head = solution.deleteMiddle(head)  # Expected to delete the node with value 3
