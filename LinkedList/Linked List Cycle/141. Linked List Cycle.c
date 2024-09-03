---- USING TWO POINTER APPROACH ----

  /**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

bool hasCycle(struct ListNode *head) {
    // Initialize two pointers: slow and fast
    struct ListNode *slow = head;
    struct ListNode *fast = head;
    
    // Traverse the linked list with two pointers
    while (slow != NULL && fast != NULL && fast->next != NULL) {
        // Move slow pointer by one step
        slow = slow->next;
        // Move fast pointer by two steps
        fast = fast->next->next;
        
        // If slow and fast pointers meet, a cycle is detected
        if (slow == fast) {
            return true;
        }
    }
    
    // If fast pointer reaches the end of the list, there is no cycle
    return false;
}

/*
 * Time Complexity: O(n)
 * - Where n is the number of nodes in the linked list.
 * - The time complexity is O(n) because the fast pointer may traverse the list at most once.

 * Space Complexity: O(1)
 * - The space complexity is O(1) because we only use a constant amount of extra space (pointers slow and fast).
 */
