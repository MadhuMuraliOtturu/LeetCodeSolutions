/**
 * Problem: Rotate a Singly-Linked List to the Right
 * Description: Given the head of a singly-linked list, rotate the list to the right by k places.
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Rotates the given linked list to the right by k positions.
 *
 * @param head: The head of the singly-linked list.
 * @param k: The number of positions to rotate the list.
 * @return: The new head of the rotated linked list.
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    struct ListNode *temp, *prev, *curr, *new_head;
    temp = head;
    int count = 0;

    // Step 1: Count the number of nodes in the list
    while (temp != NULL) {
        prev = temp;
        count++;
        temp = temp->next;
    }

    // Step 2: Check if no rotation is needed
    if (k == 0 || head == NULL) {
        return head;
    }

    // Step 3: Adjust k for cases where k is larger than the list size
    k = k % count;
    k = count - k;

    // Step 4: Connect the last node to the head to form a circular list
    prev->next = head;
    curr = head;
    
    // Step 5: Traverse to the new tail of the list (k-1 positions)
    for (int i = 0; i < k - 1; i++) {
        curr = curr->next;
    }

    // Step 6: Set the new head and break the circular connection
    new_head = curr->next;
    curr->next = NULL;

    return new_head;
}

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we only use a constant amount of extra space.
