# Problem: Modify a Linked List by Removing Nodes
# Description: Given a list of integers and a linked list, remove all nodes from the linked list
#              that contain values present in the given list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        """
        Removes nodes from the linked list whose values are present in the nums list.

        :param nums: List[int], the list of integers whose values should be removed from the linked list.
        :param head: ListNode, the head of the linked list.
        :return: ListNode, the head of the modified linked list.
        """
        s = set(nums)  # Convert the list of integers to a set for faster lookups

        # Step 1: Handle case where the head node needs to be removed
        if head and head.val in s:
            head = head.next  # Move the head pointer to the next node

        # If the linked list becomes empty after removing the head, return None
        if head is None:
            return None

        temp = head  # Pointer to traverse the linked list

        # Step 2: Traverse the list and remove any node whose value is in the set
        while temp.next:
            if temp.next.val in s:  # Check if the next node needs to be removed
                temp.next = temp.next.next  # Bypass the next node
            else:
                temp = temp.next  # Move to the next node if no removal is needed

        # Step 3: Re-check the head after traversal in case it needs to be updated
        if head and head.val in s:
            head = head.next  # Update head if its value is in the set

        return head  # Return the modified list

## Time Complexity: O(N + M), where N is the length of the linked list and M is the length of nums.
## Space Complexity: O(M), for storing the set of integers.

# Example usage:
# solution = Solution()
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# print(solution.modifiedList([1, 3], head))  # Expected result: Linked list without 1 and 3
