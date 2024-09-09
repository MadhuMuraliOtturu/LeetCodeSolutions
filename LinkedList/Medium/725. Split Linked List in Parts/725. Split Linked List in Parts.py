# Problem: Split a Linked List into Parts
# Description: Given a singly linked list and an integer `k`, split the list into `k` consecutive parts 
# where the length of each part is as equal as possible.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        """
        Splits a linked list into `k` parts with nearly equal lengths. If the list cannot be divided equally, 
        the first parts will have an extra node.

        :param head: ListNode, the head of the singly-linked list.
        :param k: Integer, the number of parts to split the list into.
        :return: List[ListNode], a list of `k` parts, each being a list node or None if the part is empty.
        """
        temp = head
        ans = [None] * k
        count_ = 0
        
        # Count the total number of nodes in the linked list
        while temp:
            count_ += 1
            temp = temp.next

        size = count_ // k  # Minimum size of each part
        extra = count_ % k   # The first 'extra' parts get an extra node

        curr = head
        ind = 0
        
        # Split the linked list into parts
        while curr and ind < k:
            length = size + 1 if extra > 0 else size  # Extra node for the first 'extra' parts
            if extra > 0:
                extra -= 1

            temp = curr
            dummy = temp
            i = 0
            
            # Split the list into the current part
            while temp and i < length:
                prev = temp
                i += 1
                temp = temp.next

            if temp:
                curr = prev.next
                prev.next = None
            else:
                curr = None

            ans[ind] = dummy
            ind += 1

        return ans

## Time Complexity: O(N), where N is the total number of nodes in the linked list.
## Space Complexity: O(k), as we use an array of size `k` to store the results.

# Example usage:
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# solution = Solution()
# result = solution.splitListToParts(head, 5)
# print(result)  # Expected output: [1->None, 2->None, 3->None, None, None]
