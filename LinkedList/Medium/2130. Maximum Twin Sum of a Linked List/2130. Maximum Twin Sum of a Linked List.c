/**
 * Problem: Find the Maximum Pair Sum in a Singly-Linked List
 * Description: Given a singly-linked list, find the maximum sum of pairs where a pair is formed by 
 * the first and last nodes, the second and second-last nodes, and so on.
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
struct ListNode* reverse(struct ListNode *head)
{
    struct ListNode *prev = NULL, *temp = head, *next = NULL;
    while (temp)
    {
        next = temp->next;
        temp->next = prev;
        prev = temp;
        temp = next;
    }
    return prev;
}

/**
 * Finds the maximum pair sum in a singly-linked list. A pair is formed by the first and last nodes, 
 * the second and second-last nodes, etc.
 *
 * @param head: The head of the singly-linked list.
 * @return: Integer, the maximum pair sum.
 */
int pairSum(struct ListNode* head) {
    struct ListNode *slow, *fast, *second_half;
    
    slow = head;
    fast = head;
    
    // Step 1: Find the middle of the linked list
    while (fast != NULL && fast->next != NULL && fast->next->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    // Step 2: Reverse the second half of the list
    second_half = slow->next;
    slow->next = NULL;
    second_half = reverse(second_half);
    
    // Step 3: Calculate the maximum pair sum
    int max = 0;
    while (head != NULL && second_half != NULL)
    {
        int sum = head->val + second_half->val;
        if (sum > max)
        {
            max = sum;
        }
        head = head->next;
        second_half = second_half->next;
    }

    return max;
}

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we only use a constant amount of extra space.
