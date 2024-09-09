#include <stdlib.h>

/**
 * Problem: Merge in Between Linked Lists
 * Description: Given two linked lists list1 and list2, and two integers a and b, merge the two linked lists 
 * by splicing list2 into list1 from position a to b. The nodes between positions a and b in list1 are removed, 
 * and list2 is inserted in their place.
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Merges list2 into list1 between positions a and b.
 *
 * @param list1: The head of the first singly-linked list.
 * @param a: The start position (1-based index) in list1 where the merge starts.
 * @param b: The end position (1-based index) in list1 where the merge ends.
 * @param list2: The head of the second singly-linked list to merge into list1.
 * @return: The head of the modified list1.
 */
struct ListNode* mergeInBetween(struct ListNode* list1, int a, int b, struct ListNode* list2) {
    struct ListNode *temp1 = list1, *temp2 = list2, *leftPrev = NULL, *prev = NULL;

    // Traverse list1 to find the node just before position 'a'
    for (int i = 0; i < b; i++) {
        if (i == a - 1) {
            leftPrev = temp1;
        }
        temp1 = temp1->next;
    }

    // Link the node before 'a' to the head of list2
    leftPrev->next = list2;

    // Traverse to the end of list2
    while (temp2 != NULL) {
        prev = temp2;
        temp2 = temp2->next;
    }

    // Connect the end of list2 to the node after position 'b' in list1
    prev->next = temp1->next;

    return list1;
}

## Time Complexity: O(N + M), where N is the number of nodes in list1, and M is the number of nodes in list2.
## Space Complexity: O(1), as we are using only a constant amount of extra space.
