#include <stdlib.h>

/**
 * Problem: Insert Greatest Common Divisors Between Linked List Nodes
 * Description: Given a singly-linked list, for every pair of consecutive nodes, insert a new node
 * between them that contains the greatest common divisor (GCD) of the two nodes' values.
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/**
 * Computes the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
 *
 * @param a: The first integer.
 * @param b: The second integer.
 * @return: The GCD of a and b.
 */
int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

/**
 * Inserts a new node containing the GCD of each pair of consecutive nodes in the linked list.
 *
 * @param head: The head of the singly-linked list.
 * @return: The head of the modified linked list with inserted GCD nodes.
 */
struct ListNode* insertGreatestCommonDivisors(struct ListNode* head) {
    struct ListNode *node1 = head, *node2 = NULL, *gcd_node = NULL;

    // Traverse through the list, inserting GCD nodes between every pair of consecutive nodes
    while (node1 != NULL && node1->next != NULL) {
        node2 = node1->next;
        int a = node1->val;
        int b = node2->val;

        // Create a new node to store the GCD of a and b
        gcd_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        gcd_node->val = gcd(a, b);

        // Insert the GCD node between node1 and node2
        node1->next = gcd_node;
        gcd_node->next = node2;

        // Move to the next pair of nodes
        node1 = node2;
    }

    return head;
}

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), since we only use a constant amount of extra space aside from the new nodes.
