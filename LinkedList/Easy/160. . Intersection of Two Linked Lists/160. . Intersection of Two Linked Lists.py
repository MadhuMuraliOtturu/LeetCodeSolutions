# Problem: Find the Intersection Node of Two Singly-Linked Lists
# Description: Given the heads of two singly-linked lists, find the node where the two lists intersect. 
# If the two lists do not intersect, return None.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        Finds the intersection node of two singly-linked lists.

        :param headA: ListNode, the head of the first singly-linked list.
        :param headB: ListNode, the head of the second singly-linked list.
        :return: ListNode, the intersection node of the two lists, or None if they do not intersect.
        """
        lenA = 0
        lenB = 0
        temp1 = headA
        temp2 = headB
        
        # Calculate the length of both lists
        while temp1:
            lenA += 1
            temp1 = temp1.next
        while temp2:
            lenB += 1
            temp2 = temp2.next
        
        # Determine the longer and shorter list
        if lenA > lenB:
            list1 = headA
            list2 = headB
        else:
            list1 = headB
            list2 = headA
        
        # Move the pointer of the longer list by the difference in lengths
        extra_len = abs(lenA - lenB)
        for _ in range(extra_len):
            list1 = list1.next
        
        # Traverse both lists to find the intersection node
        while list1 and list2:
            if list1 == list2:
                return list1
            list1 = list1.next
            list2 = list2.next
        
        return None

## Time Complexity: O(N + M), where N and M are the lengths of the two linked lists.
## Space Complexity: O(1), as we only use a constant amount of extra space.

# Example usage:
# headA = ListNode(1)
# headB = ListNode(2)
# headA.next = ListNode(3)
# headB.next = ListNode(4)
# intersect = ListNode(5)
# headA.next.next = intersect
# headB.next.next = intersect
# intersect.next = ListNode(6)
# solution = Solution()
# result = solution.getIntersectionNode(headA, headB)
# # Expected to return the node with value 5
