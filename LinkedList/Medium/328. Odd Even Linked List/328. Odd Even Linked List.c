/**
 * Problem: Odd-Even Linked List
 * Description: Given a singly-linked list, group all the nodes with odd indices together followed by 
 * the nodes with even indices, and return the reordered list. The relative order inside the odd and even 
 * groups should remain as it was in the input.
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Reorders the linked list such that all nodes at odd positions are grouped together, followed by 
 * the nodes at even positions.
 *
 * @param head: The head of the singly-linked list.
 * @return: The head of the reordered list.
 */
struct ListNode* oddEvenList(struct ListNode* head) {
    // Return early if the list has less than 2 nodes
    if (!head || !head->next) {
        return head;
    }
    
    // Initialize pointers for odd and even lists
    struct ListNode *odd = head;
    struct ListNode *even = head->next;
    struct ListNode *even_head = even;  // Keep track of the start of even nodes

    // Traverse and rearrange the list
    while (even && even->next) {
        odd->next = even->next;
        odd = odd->next;
        even->next = odd->next;
        even = even->next;
    }
    
    // Connect the end of the odd list to the start of the even list
    odd->next = even_head;

    return head;
}

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we are not using any extra space except for a few pointers.
