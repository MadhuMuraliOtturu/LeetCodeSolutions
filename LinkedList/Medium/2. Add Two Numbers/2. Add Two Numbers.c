// Problem: LeetCode 2 - Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *head1 = l1;  // Pointer to traverse the first linked list
    struct ListNode *head2 = l2;  // Pointer to traverse the second linked list
    struct ListNode *prev;        // Pointer to track the previous node
    int carry = 0;                // Initialize carry to handle sums greater than 9

    // Step 1: Traverse both linked lists and sum corresponding digits
    while(head1 && head2) {
        int sum = head1->val + head2->val + carry;  // Calculate sum including carry
        if(sum > 9) {
            head1->val = sum % 10;  // Update the node's value with the last digit of the sum
            carry = 1;  // Set carry for the next digit
        } else {
            head1->val = sum;  // No carry, update the node's value with the sum
            carry = 0;  // Reset carry
        }
        prev = head1;  // Keep track of the last node processed in l1
        head1 = head1->next;  // Move to the next node in l1
        head2 = head2->next;  // Move to the next node in l2
    }

    // Step 2: If l2 is longer, append the remaining nodes to l1
    if(head2 != NULL) {
        prev->next = head2;  // Connect the last node in l1 to the remaining nodes in l2
        head1 = prev->next;  // Continue traversal with the nodes from l2
    }

    // Step 3: Continue to process any remaining carry
    while(head1 != NULL) {
        int sum = head1->val + carry;  // Add carry to the current node's value
        if(sum > 9) {
            head1->val = sum % 10;  // Update the node's value with the last digit of the sum
            carry = 1;  // Carry over to the next digit
        } else {
            head1->val = sum;  // Update the node's value with the sum
            carry = 0;  // Reset carry
        }
        prev = head1;  // Keep track of the last node processed
        head1 = head1->next;  // Move to the next node
    }

    // Step 4: If there's still a carry left, add a new node with the carry value
    if (carry > 0) {
        struct ListNode *newNode = (struct ListNode *)malloc(sizeof(struct ListNode));  // Create a new node
        newNode->val = carry;  // Assign the carry value to the new node
        newNode->next = NULL;  // Set the next pointer to NULL
        prev->next = newNode;  // Link the new node to the end of the list
    }

    return l1;  // Return the head of the resulting linked list
}

/*
Time Complexity: O(max(m, n)), where m and n are the lengths of the linked lists l1 and l2.
Space Complexity: O(1), since we're modifying the linked list in place.

Example usage:
struct ListNode* l1 = createLinkedList([2, 4, 3]);  // Represents the number 342
struct ListNode* l2 = createLinkedList([5, 6, 4]);  // Represents the number 465
struct ListNode* result = addTwoNumbers(l1, l2);
// The result should represent the number 807, so the linked list would be 7 -> 0 -> 8
*/
