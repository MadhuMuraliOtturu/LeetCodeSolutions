/**
 * Problem: Remove Duplicates from Sorted List
 * Description: Given the head of a sorted singly-linked list, delete all duplicates such that each element 
 * appears only once. The function should return the modified linked list.
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Deletes duplicate elements from a sorted singly-linked list.
 *
 * @param head: The head of the sorted singly-linked list.
 * @return: The head of the modified list with duplicates removed.
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode *temp;
    temp = head;
    
    // Traverse the list and remove duplicates
    while (temp != NULL && temp->next != NULL) {
        if (temp->val == temp->next->val) {
            temp->next = temp->next->next; // Skip the duplicate node
        } else {
            temp = temp->next; // Move to the next distinct element
        }
    }
    
    return head;
}

## Time Complexity: O(N), where N is the number of nodes in the linked list.
## Space Complexity: O(1), as we are not using any additional space except for a few pointers.
