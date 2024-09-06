# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        Removes all nodes with the given value from a linked list.

        :param head: ListNode, the head of the linked list.
        :param val: Integer, the value to be removed from the list.
        :return: ListNode, the head of the modified linked list.
        """
        # Remove nodes from the beginning of the list that match the value
        while head and head.val == val:
            head = head.next
        
        # If the list is empty after removal, return None
        if head is None:
            return head
        
        # If the list has only one node
        if head.next is None:
            if head.val != val:
                return head
            return None
        
        # Traverse the list and remove nodes with the given value
        temp = head
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head

# Example usage:
# head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
# solution = Solution()
# new_head = solution.removeElements(head, 6)
# The new_head should not contain any nodes with value 6
