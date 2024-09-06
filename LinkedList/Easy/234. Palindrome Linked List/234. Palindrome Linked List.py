# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        Checks if the singly-linked list is a palindrome.

        :param head: ListNode, the head of the singly-linked list.
        :return: Boolean, True if the list is a palindrome, False otherwise.
        """
        def reverse(head):
            """
            Reverses the singly-linked list.

            :param head: ListNode, the head of the singly-linked list to be reversed.
            :return: ListNode, the new head of the reversed linked list.
            """
            prev = None
            temp = head
            while temp:
                next_node = temp.next
                temp.next = prev
                prev = temp
                temp = next_node
            return prev
        
        slow = fast = head
        
        # Step 1: Find the middle of the linked list
        while slow and fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        second_half = slow.next
        slow.next = None
        second_half = reverse(second_half)
        
        # Step 3: Check if the list is a palindrome
        while head and second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        
        return True

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we only use a constant amount of extra space.
