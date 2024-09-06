/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Deletes the middle node of a singly-linked list.
 *
 * @param head Pointer to the head of the linked list.
 * @return The head of the modified linked list after deleting the middle node.
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    struct ListNode *slow, *fast, *prev;
    slow = head;
    fast = head;
    
    // Edge case: if the list is empty or contains only one node
    if (head == NULL || head->next == NULL) {
        return NULL;
    }

    // Traverse the list with two pointers to find the middle node
    while (fast && fast->next) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }
    
    // Delete the middle node
    prev->next = prev->next->next;
    return head;
}

/*
 * Time Complexity: O(n) - where n is the number of nodes in the linked list.
 * We traverse the list to find the middle node using two pointers.
 *
 * Space Complexity: O(1) - No extra space is used apart from a few pointers.
 */
