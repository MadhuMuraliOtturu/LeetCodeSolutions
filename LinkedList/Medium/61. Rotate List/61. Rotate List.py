# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        Swaps every two adjacent nodes in the singly-linked list.

        :param head: ListNode, the head of the singly-linked list.
        :return: ListNode, the head of the modified linked list after swapping pairs.
        """
        curr = head
        while curr and curr.next:
            # Swap current node's value with the next node
            curr.val, curr.next.val = curr.next.val, curr.val
            # Move to the next pair
            curr = curr.next.next
        return head

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we are using a constant amount of extra space.
