#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Deletes the given node from the linked list.
 * Note: This function assumes that the node to be deleted is not the last node in the list.
 *
 * @param node Pointer to the node to be deleted.
 */
void deleteNode(struct ListNode* node) {
    // Step 1: Copy the value of the next node to the current node
    node->val = node->next->val;
    // Step 2: Skip the next node by pointing to the next of next node
    struct ListNode* temp = node->next;
    node->next = node->next->next;
    free(temp); // Free the memory allocated for the skipped node
}

/**
 * Example usage:
 * struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
 * node->val = 4;
 * node->next = (struct ListNode*)malloc(sizeof(struct ListNode));
 * node->next->val = 5;
 * node->next->next = (struct ListNode*)malloc(sizeof(struct ListNode));
 * node->next->next->val = 1;
 * node->next->next->next = (struct ListNode*)malloc(sizeof(struct ListNode));
 * node->next->next->next->val = 9;
 * deleteNode(node->next);  // Deletes the node with value 5
 */
