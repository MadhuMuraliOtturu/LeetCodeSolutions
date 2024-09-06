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
        # Step 1: Create a set to store the values to be removed for O(1) lookup time
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
        
        # Step 2: Remove nodes from the head of the list if they are in the set
        while head and head.val in d:
            head = head.next
        
        # If the list becomes empty after removal of head, return None
        if not head:
            return None
        
        # Step 3: Traverse the list and remove nodes with values in the set
        temp = head
        while temp.next:
            if temp.next.val in d:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head

## Time Complexity: O(N + M), where N is the length of the linked list and M is the length of nums.
## Space Complexity: O(M), for storing the set of integers.

# Example usage:
# solution = Solution()
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# print(solution.modifiedList([1, 3], head))  # Expected result: Linked list without 1 and 3
