//One Pass Solution
#include <stdlib.h>

/**
 * Problem: Reverse a Sublist in a Linked List
 * Description: Given the head of a singly-linked list and two integers left and right, reverse the nodes 
 * of the linked list from position left to position right and return the head of the modified list. 
 * Positions are 1-based and left <= right.
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Reverses the nodes of a linked list from position left to right.
 *
 * @param head: The head of the singly-linked list.
 * @param left: The starting position of the sublist to be reversed (1-based index).
 * @param right: The ending position of the sublist to be reversed (1-based index).
 * @return: The head of the modified linked list.
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    struct ListNode *temp, *prev = NULL, *next = NULL;
    struct ListNode *dummynode = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode *leftPrev = NULL, *new_tail = NULL;
    
    dummynode->val = -1;
    dummynode->next = head;
    head = dummynode;
    temp = head;
    
    // Move temp to the node just before the left position
    for (int i = 0; i < left; i++) {
        leftPrev = temp;
        temp = temp->next;
    }
    
    new_tail = temp;
    
    // Reverse the sublist from left to right
    for (int j = 0; j < right - left + 1; j++) {
        next = temp->next;
        temp->next = prev;
        prev = temp;
        temp = next;
    }
    
    // Connect the reversed sublist back to the list
    leftPrev->next = prev;
    new_tail->next = temp;
    
    return head->next;
}

## Time Complexity: O(N), where N is the length of the linked list.
## Space Complexity: O(1), as we are using only a constant amount of extra space.
