# Problem: Add Two Numbers Represented by Linked Lists
# Description: Given two singly-linked lists representing non-negative integers, 
# where each node contains a single digit. The digits are stored in reverse order, and each of 
# their non-empty linked lists does not contain any leading zero, add the two numbers and return the result as a linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Adds two numbers represented by linked lists in reverse order.

        :param l1: ListNode, the head of the first linked list.
        :param l2: ListNode, the head of the second linked list.
        :return: ListNode, the head of the new linked list representing the sum.
        """
        
        def reverse(head):
            """
            Reverses the linked list.

            :param head: ListNode, the head of the singly-linked list to be reversed.
            :return: ListNode, the new head of the reversed linked list.
            """
            prev = None
            temp = head
            while temp:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            return prev

        # Step 1: Reverse both linked lists
        l1 = reverse(l1)
        l2 = reverse(l2)

        carry = 0
        temp1 = l1
        temp2 = l2

        # Step 2: Add corresponding nodes from both lists
        while temp1 and temp2:
            sum_ = temp1.val + temp2.val + carry
            if sum_ > 9:
                temp1.val = sum_ % 10
                carry = 1
            else:
                temp1.val = sum_
                carry = 0
            prev = temp1
            temp1 = temp1.next
            temp2 = temp2.next

        # Step 3: Handle remaining nodes in l2 if it has more digits
        if temp2:
            prev.next = temp2
            temp1 = prev.next

        # Step 4: Handle carry
        while temp1:
            sum_ = carry + temp1.val
            if sum_ > 9:
                temp1.val = sum_ % 10
                carry = 1
            else:
                temp1.val = sum_
                carry = 0
            prev = temp1
            temp1 = temp1.next

        # Step 5: If carry remains after the last digit, add a new node
        if carry > 0:
            prev.next = ListNode(carry)

        # Step 6: Reverse the result list back and return
        return reverse(l1)

## Time Complexity: O(N), where N is the number of nodes in the longer linked list.
## Space Complexity: O(1), since no extra space is used apart from the input list and output list.

# Example usage:
# l1 = ListNode(7)
# l1.next = ListNode(2)
# l1.next.next = ListNode(4)
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
# solution = Solution()
# result = solution.addTwoNumbers(l1, l2)
# # Expected output: The list representing the number 780 (i.e., 7 -> 8 -> 0)
