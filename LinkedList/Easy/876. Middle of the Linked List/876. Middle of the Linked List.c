/**
 * Problem: Find the Middle Node of a Singly-Linked List
 * Description: Given a linked list, find the middle node. If there are two middle nodes, return the second middle node.
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Finds the middle node of the linked list. If there are two middle nodes, returns the second one.
 *
 * @param head: The head of the singly-linked list.
 * @return: The middle node of the linked list.
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode *slow, *fast;
    slow = fast = head;
    
    // Step 1: Use the two-pointer technique to find the middle node
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    return slow;
}

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we only use a constant amount of extra space.

