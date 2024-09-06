# Problem: Remove Duplicates from a Sorted Singly-Linked List
# Description: Given a sorted singly-linked list, remove all duplicates such that each element appears 
# only once.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        Removes duplicates from a sorted singly-linked list.

        :param head: ListNode, the head of the sorted singly-linked list.
        :return: ListNode, the head of the list after duplicates have been removed.
        """
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we only use a constant amount of extra space.

# Example usage:
# head = ListNode(1)
# head.next = ListNode(1)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(3)
# solution = Solution()
# new_head = solution.deleteDuplicates(head)
# # Expected to return a list with nodes 1 -> 2 -> 3
