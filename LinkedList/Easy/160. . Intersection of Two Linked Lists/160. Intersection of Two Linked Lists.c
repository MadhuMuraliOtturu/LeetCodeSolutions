/**
 * Problem: Find the Intersection Node of Two Linked Lists
 * Description: Given the heads of two singly-linked lists, find the node where the two lists intersect. 
 * If they do not intersect, return NULL. The lists may intersect at more than one node.
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Finds the intersection node of two singly-linked lists.
 *
 * @param headA: The head of the first singly-linked list.
 * @param headB: The head of the second singly-linked list.
 * @return: The intersection node, or NULL if there is no intersection.
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {

    struct ListNode *list1, *list2, *temp1, *temp2;
    temp1 = headA;
    temp2 = headB;
    int lenA = 0, lenB = 0, extra_len;
    
    // Calculate the length of list A
    while (temp1 != NULL) {
        lenA++;
        temp1 = temp1->next;
    }
    
    // Calculate the length of list B
    while (temp2 != NULL) {
        lenB++;
        temp2 = temp2->next;
    }
    
    // Determine the longer list and calculate the difference in length
    if (lenA > lenB) {
        extra_len = lenA - lenB;
        list1 = headA;
        list2 = headB;
    } else {
        extra_len = lenB - lenA;
        list1 = headB;
        list2 = headA;
    }

    // Advance the pointer of the longer list by the difference in length
    for (int i = 0; i < extra_len; i++) {
        list1 = list1->next;
    }
    
    // Traverse both lists together to find the intersection
    while (list1 != NULL && list2 != NULL) {
        if (list1 == list2) {
            return list2;
        }
        list1 = list1->next;
        list2 = list2->next;
    }
    
    return NULL;
}

## Time Complexity: O(N + M), where N and M are the lengths of the two lists.
## Space Complexity: O(1), as we are not using any additional space except for a few pointers.
