/**
 * Problem: Check if a Singly-Linked List is a Palindrome
 * Description: Given a singly-linked list, determine if it reads the same forwards and backwards.
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
struct ListNode *reverse(struct ListNode *head)
{
    struct ListNode *prev = NULL, *temp = head, *next = NULL;
    while (temp != NULL)
    {
        next = temp->next;
        temp->next = prev;
        prev = temp;
        temp = next;
    }
    return prev;
}

/**
 * Checks if the singly-linked list is a palindrome.
 *
 * @param head: The head of the singly-linked list.
 * @return: Boolean, true if the list is a palindrome, false otherwise.
 */
bool isPalindrome(struct ListNode* head) {
    struct ListNode *slow, *fast, *second_half;
    
    slow = head;
    fast = head;
    
    // Step 1: Find the middle of the linked list
    while (slow != NULL && fast != NULL && fast->next != NULL && fast->next->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    // Step 2: Reverse the second half of the list
    second_half = slow->next;
    slow->next = NULL;
    second_half = reverse(second_half);
    
    // Step 3: Check if the list is a palindrome
    while (head != NULL && second_half != NULL)
    {
        if (head->val != second_half->val)
        {
            return false;
        }
        head = head->next;
        second_half = second_half->next;
    }

    return true;
}

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we only use a constant amount of extra space.
