# Problem: Merge Two Linked Lists with an Insertion Point
# Description: Given two singly-linked lists `list1` and `list2`, and two integers `a` and `b`, 
# merge `list2` into `list1` starting at position `a` and ending at position `b`. 
# The nodes between positions `a` and `b` in `list1` should be replaced by `list2`.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        Merges list2 into list1 starting at position `a` and ending at position `b`.

        :param list1: ListNode, the head of the first singly-linked list.
        :param a: Integer, the start position (0-indexed) for merging list2 into list1.
        :param b: Integer, the end position (0-indexed) for merging list2 into list1.
        :param list2: ListNode, the head of the second singly-linked list to be merged into list1.
        :return: ListNode, the head of the modified linked list.
        """
        # Create a dummy node to simplify edge cases
        list1 = ListNode(-1, list1)
        temp = list1
        
        # Traverse to the node just before position `a`
        for i in range(a):
            temp = temp.next
        leftNode = temp
        
        # Traverse to the node just after position `b`
        for j in range(b - a + 1):
            temp = temp.next
        
        # Find the last node of list2
        temp_2 = list2
        prev = None
        while temp_2:
            prev = temp_2
            temp_2 = temp_2.next
        
        # Merge list2 into list1
        prev.next = temp.next
        leftNode.next = list2
        
        return list1.next

## Time Complexity: O(N + M), where N is the number of nodes in list1 and M is the number of nodes in list2.
## Space Complexity: O(1), as we only use a constant amount of extra space.

# Example usage:
# list1 = ListNode(0)
# list1.next = ListNode(1)
# list1.next.next = ListNode(2)
# list1.next.next.next = ListNode(3)
# list1.next.next.next.next = ListNode(4)
# list2 = ListNode(1000000)
# list2.next = ListNode(1000001)
# solution = Solution()
# result = solution.mergeInBetween(list1, 2, 4, list2)
# print(result)  # Expected output: 0 -> 1 -> 1000000 -> 1000001
