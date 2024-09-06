/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Removes all nodes with the given value from a linked list.
 *
 * @param head Pointer to the head of the linked list.
 * @param val The value to remove from the list.
 * @return The head of the modified linked list.
 *
 * Time Complexity: O(n) - where n is the number of nodes in the linked list. 
 * We traverse the list once to remove nodes.
 *
 * Space Complexity: O(1) - No extra space is used apart from the pointers.
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode *temp;
    
    // Remove nodes from the beginning of the list that match the value
    while (head != NULL && head->val == val) {
        head = head->next;
    }
    
    // If the list is empty after removal, return NULL
    if (head == NULL) {
        return NULL;
    }
    
    // Traverse the list and remove nodes with the given value
    temp = head;
    while (temp->next) {
        if (temp->next->val == val) {
            temp->next = temp->next->next;
        } else {
            temp = temp->next;
        }
    }
    
    return head;
}
