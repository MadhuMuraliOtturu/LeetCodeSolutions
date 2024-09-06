# Problem: Rearrange a Singly-Linked List into Odd and Even Nodes
# Description: Given a singly-linked list, rearrange the nodes such that all nodes at odd indices come before 
# nodes at even indices. The relative order of the odd and even nodes should be preserved.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        Rearranges a singly-linked list so that all nodes at odd indices come before nodes at even indices.
        The relative order of nodes in each group (odd and even) should be preserved.

        :param head: ListNode, the head of the singly-linked list.
        :return: ListNode, the head of the rearranged linked list.
        """
        if head is None or head.next is None:
            return head
        
        odd = head
        even = head.next
        odd_head = odd
        even_head = even
        
        while True:
            if odd and odd.next:
                odd.next = odd.next.next
                odd = odd.next
            if even and even.next:
                even.next = even.next.next
                even = even.next
            if not odd or not odd.next and not even or not even.next:
                break
        
        if odd:
            odd.next = even_head
        else:
            odd_head.next = even_head
        
        return odd_head

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we only use a constant amount of extra space.

# Example usage:
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# solution = Solution()
# new_head = solution.oddEvenList(head)
# # Expected to return a list: 1 -> 3 -> 5 -> 2 -> 4
