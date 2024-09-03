---- USING HASHMAP ----

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize a dictionary to keep track of visited nodes
        hash_map = {}
        
        # Start with the head of the linked list
        temp = head
        
        # Traverse the linked list
        while temp:
            # If the current node is already in the hash_map, a cycle is detected
            if temp in hash_map:
                return True
            
            # Mark the current node as visited by adding it to the hash_map
            hash_map[temp] = True
            
            # Move to the next node
            temp = temp.next
        
        # If we reach the end of the list without finding a cycle, return False
        return False

## Time Complexity: O(n)
# - Where n is the number of nodes in the linked list.
# - The time complexity is O(n) because we traverse each node in the linked list once.

## Space Complexity: O(n)
# - The space complexity is O(n) due to the hash_map which stores each node to track cycles.




---- OPTIMAL APPROACH USING TWO POINTERS ----

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers: slow and fast
        slow = head
        fast = head
        
        # Traverse the linked list with two pointers
        while fast and fast.next:
            # Move slow pointer by one step
            slow = slow.next
            # Move fast pointer by two steps
            fast = fast.next.next
            
            # If slow and fast pointers meet, a cycle is detected
            if slow == fast:
                return True
        
        # If fast pointer reaches the end of the list, there is no cycle
        return False

## Time Complexity: O(n)
# - Where n is the number of nodes in the linked list.
# - The time complexity is O(n) because we traverse the list at most once with the fast pointer.

## Space Complexity: O(1)
# - The space complexity is O(1) because we only use a constant amount of extra space (pointers slow and fast).
