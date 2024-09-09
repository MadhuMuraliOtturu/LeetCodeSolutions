# Problem: Reverse a Sublist in a Singly-Linked List
# Description: Given a singly-linked list and two integers `left` and `right`, reverse the nodes of the list 
# from position `left` to position `right` and return the modified list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        Reverses the nodes of the linked list from position `left` to position `right` and returns the modified list.

        :param head: ListNode, the head of the singly-linked list.
        :param left: Integer, the start position of the sublist to be reversed (1-indexed).
        :param right: Integer, the end position of the sublist to be reversed (1-indexed).
        :return: ListNode, the head of the modified linked list.
        """
        dummynode = ListNode(-1, head)
        head = dummynode
        leftPrev = None
        temp = head
        
        # Move `temp` to the node before the `left` position
        for i in range(left):
            leftPrev = temp
            temp = temp.next
        
        # Reverse the sublist from `left` to `right`
        prev = None
        curr = temp
        curr_dummy = curr
        for j in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Connect the reversed sublist back to the list
        leftPrev.next = prev
        curr_dummy.next = curr
        
        return head.next

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we only use a constant amount of extra space.

# Example usage:
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# solution = Solution()
# result = solution.reverseBetween(head, 2, 4)
# print(result)  # Expected output: 1 -> 4 -> 3 -> 2 -> 5
