# Problem: Remove Nodes in a Linked List
# Description: Given a linked list, remove nodes that are less than the maximum value of nodes that follow them.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNodes(self, head):
        """
        Removes nodes from the linked list that have values less than the maximum value
        of nodes that follow them.

        :param head: ListNode, the head of the singly-linked list.
        :return: ListNode, the head of the modified list after removing nodes.
        """
        def reverse(head):
            """
            Reverses the given linked list.

            :param head: ListNode, the head of the singly-linked list.
            :return: ListNode, the head of the reversed list.
            """
            prev = None
            temp = head
            while temp:
                next_node = temp.next
                temp.next = prev
                prev = temp
                temp = next_node
            return prev
        
        # Step 1: Reverse the linked list
        head = reverse(head)
        rev_head = head
        
        # If the list is empty or has only one node, return it as is
        if head is None or head.next is None:
            return head
        
        # Step 2: Traverse the reversed list and remove nodes with values less than the maximum value seen
        curr_max_val = rev_head.val
        while rev_head.next:
            if rev_head.next.val < curr_max_val:
                rev_head.next = rev_head.next.next
            else:
                curr_max_val = rev_head.next.val
                rev_head = rev_head.next
        
        # Step 3: Reverse the list again to restore original order
        return reverse(head)

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we do not use extra space for storing nodes.

# Example usage:
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# solution = Solution()
# new_head = solution.removeNodes(head)  # Expected to remove nodes less than max value
