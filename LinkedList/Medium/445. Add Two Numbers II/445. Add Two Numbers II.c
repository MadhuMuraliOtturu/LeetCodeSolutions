#include <stdlib.h>

/**
 * Problem: Add Two Numbers Represented by Linked Lists
 * Description: Given two non-empty singly linked lists representing two non-negative integers, 
 * add the two numbers and return the sum as a linked list. The digits are stored in reverse order, 
 * and each of their nodes contains a single digit.
 *
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Reverses the linked list.
 *
 * @param head: The head of the singly-linked list to be reversed.
 * @return: The new head of the reversed linked list.
 */
struct ListNode *reverse(struct ListNode *head) {
    struct ListNode *prev = NULL, *temp = head, *next = NULL;
    while (temp != NULL) {
        next = temp->next;
        temp->next = prev;
        prev = temp;
        temp = next;
    }
    return prev;
}

/**
 * Adds two numbers represented by linked lists and returns the result as a linked list.
 *
 * @param l1: The head of the first singly-linked list.
 * @param l2: The head of the second singly-linked list.
 * @return: The head of the resulting linked list representing the sum.
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *head1 = reverse(l1);
    struct ListNode *head2 = reverse(l2);
    struct ListNode dummy; 
    struct ListNode *current = &dummy;
    dummy.next = NULL;
    int carry = 0;
    
    // Traverse both lists and sum corresponding values
    while (head1 != NULL || head2 != NULL || carry != 0) {
        int sum = carry;
        
        if (head1 != NULL) {
            sum += head1->val;
            head1 = head1->next;
        }
        
        if (head2 != NULL) {
            sum += head2->val;
            head2 = head2->next;
        }
        
        carry = sum / 10;
        sum = sum % 10;
        
        // Create a new node for the current digit of the result
        current->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        current = current->next;
        current->val = sum;
        current->next = NULL;
    }

    // Reverse the result list to restore the original order
    struct ListNode *result = reverse(dummy.next);
    return result;
}

## Time Complexity: O(N + M), where N and M are the lengths of the two input linked lists.
## Space Complexity: O(N + M), where N and M are the lengths of the input lists, accounting for the result list.
