# Problem: Find the Maximum Pair Sum in a Singly-Linked List
# Description: Given a singly-linked list, find the maximum sum of pairs where a pair is formed by 
# the first and last nodes, the second and second-last nodes, and so on.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        Finds the maximum pair sum in a singly-linked list. A pair is formed by the first and last nodes, 
        the second and second-last nodes, etc.

        :param head: ListNode, the head of the singly-linked list.
        :return: Integer, the maximum pair sum.
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
        
        # Step 3: Calculate the maximum pair sum
        first_half = head
        max_val = 0
        while second_half:
            max_val = max(max_val, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next
        
        return max_val

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we only use a constant amount of extra space.

# Example usage:
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# solution = Solution()
# print(solution.pairSum(head))  # Expected to return 5 (i.e., 1+4 or 2+3)
