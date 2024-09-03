# Problem: LeetCode 2 - Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Adds two numbers represented by linked lists, where each node contains a single digit.
        The digits are stored in reverse order, and each of their non-empty linked lists 
        does not contain any leading zero, except the number 0 itself.

        :param l1: ListNode, the head of the first linked list.
        :param l2: ListNode, the head of the second linked list.
        :return: ListNode, the head of the linked list representing the sum.
        """
        carry = 0  # Initialize carry to handle sums greater than 9
        temp1 = l1  # Pointer to traverse the first linked list
        temp2 = l2  # Pointer to traverse the second linked list
        
        # Step 1: Traverse both linked lists and sum corresponding digits
        while temp1 and temp2:
            sum_ = temp1.val + temp2.val + carry  # Calculate sum including carry
            if sum_ > 9:
                temp1.val = sum_ % 10  # Update the node's value with the last digit of the sum
                carry = 1  # Set carry for the next digit
            else:
                temp1.val = sum_  # No carry, update the node's value with the sum
                carry = 0  # Reset carry
            
            prev = temp1  # Keep track of the last node processed in l1
            temp1 = temp1.next  # Move to the next node in l1
            temp2 = temp2.next  # Move to the next node in l2
        
        # Step 2: If l2 is longer, append the remaining nodes to l1
        if temp2:
            prev.next = temp2  # Connect the last node in l1 to the remaining nodes in l2
            temp1 = prev.next  # Continue traversal with the nodes from l2

        # Step 3: Continue to process any remaining carry
        while temp1:
            sum_ = carry + temp1.val  # Add carry to the current node's value
            if sum_ > 9:
                temp1.val = sum_ % 10  # Update the node's value with the last digit of the sum
                carry = 1  # Carry over to the next digit
            else:
                temp1.val = sum_  # Update the node's value with the sum
                carry = 0  # Reset carry
            
            prev = temp1  # Keep track of the last node processed
            temp1 = temp1.next  # Move to the next node

        # Step 4: If there's still a carry left, add a new node with the carry value
        if carry > 0:
            prev.next = ListNode(carry)  # Add a new node at the end with the carry value
        
        return l1  # The head of the resulting linked list

## Time Complexity: O(max(m, n)), where m and n are the lengths of the linked lists l1 and l2.
## Space Complexity: O(1), since we're modifying the linked list in place.

# Example usage:
# solution = Solution()
# l1 = ListNode(2, ListNode(4, ListNode(3)))  # Represents the number 342
# l2 = ListNode(5, ListNode(6, ListNode(4)))  # Represents the number 465
# result = solution.addTwoNumbers(l1, l2)
# The result should represent the number 807, so the linked list would be 7 -> 0 -> 8
