#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Reverses a singly-linked list.
 * 
 * @param head Pointer to the head of the linked list.
 * @return Pointer to the new head of the reversed list.
 */
struct ListNode* reverse(struct ListNode* head) {
    struct ListNode *prev = NULL, *temp = head, *node;
    while (temp) {
        node = temp->next;
        temp->next = prev;
        prev = temp;
        temp = node;
    }
    return prev;
}

/**
 * Removes nodes from the linked list that have values less than the maximum value
 * of nodes that follow them. The function first reverses the list, then removes
 * nodes based on the criteria, and finally reverses the list again to restore 
 * the original order.
 * 
 * @param head Pointer to the head of the linked list.
 * @return Pointer to the head of the modified list.
 */
struct ListNode* removeNodes(struct ListNode* head) {
    struct ListNode *rev_node;
    head = reverse(head);
    if (head == NULL || head->next == NULL) {
        return head;
    }
    rev_node = head;
    int curr_max_val = head->val;
    while (rev_node->next) {
        if (rev_node->next->val < curr_max_val) {
            rev_node->next = rev_node->next->next;
        } else {
            curr_max_val = rev_node->next->val;
            rev_node = rev_node->next;
        }
    }
    return reverse(head);
}

/**
 * Example usage:
 * struct ListNode* node1 = (struct ListNode*)malloc(sizeof(struct ListNode));
 * node1->val = 1;
 * node1->next = (struct ListNode*)malloc(sizeof(struct ListNode));
 * node1->next->val = 3;
 * node1->next->next = (struct ListNode*)malloc(sizeof(struct ListNode));
 * node1->next->next->val = 2;
 * node1->next->next->next = (struct ListNode*)malloc(sizeof(struct ListNode));
 * node1->next->next->next->val = 4;
 * node1->next->next->next->next = NULL;
 * struct ListNode* new_head = removeNodes(node1); // Expected to remove nodes less than max value
 */
