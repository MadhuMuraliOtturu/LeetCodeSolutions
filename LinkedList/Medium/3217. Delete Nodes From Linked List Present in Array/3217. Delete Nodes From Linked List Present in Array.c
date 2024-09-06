#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

typedef struct {
    int data[1000001];  // Hashmap to store presence of values in the range [0, 1000000]
} hashmap;

/**
 * Creates a new hashmap and initializes all values to 0.
 * @return A pointer to the created hashmap.
 */
hashmap* create_hashmap() {
    hashmap *hash = (hashmap*)malloc(sizeof(hashmap));
    if (hash == NULL) {
        return NULL;  // Memory allocation failed
    }
    for (int i = 0; i < 1000001; i++) {
        hash->data[i] = 0;  // Initialize all values to 0
    }
    return hash;
}

/**
 * Frees the memory allocated for the hashmap.
 * @param hash A pointer to the hashmap to be freed.
 */
void free_hashmap(hashmap* hash) {
    if (hash != NULL) {
        free(hash);  // Free the allocated memory
    }
}

/**
 * Modifies the linked list by removing nodes with values present in the nums array.
 * @param nums Array of integers to be removed from the linked list.
 * @param numsSize Size of the nums array.
 * @param head Pointer to the head of the linked list.
 * @return Pointer to the head of the modified linked list.
 */
struct ListNode* modifiedList(int* nums, int numsSize, struct ListNode* head) {
    hashmap* s = create_hashmap();
    if (s == NULL) {
        return head;  // Memory allocation failed
    }

    // Populate the hashmap with the values from nums
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] >= 0 && nums[i] < 1000001) {
            s->data[nums[i]] = 1;  // Mark the value as present
        }
    }

    // Remove nodes from the head of the list if they are in the hashmap
    while (head != NULL && s->data[head->val] == 1) {
        struct ListNode* temp = head;
        head = head->next;
        free(temp);  // Free the memory of the removed node
    }

    // Remove nodes from the rest of the list
    struct ListNode *current = head;
    while (current != NULL && current->next != NULL) {
        if (s->data[current->next->val] == 1) {
            struct ListNode* temp = current->next;
            current->next = temp->next;
            free(temp);  // Free the memory of the removed node
        } else {
            current = current->next;  // Move to the next node
        }
    }

    free_hashmap(s);  // Free the hashmap memory
    return head;  // Return the modified linked list
}

/**
 * Example usage:
 * struct ListNode* head = /* Initialize the linked list */;
 * int nums[] = {1, 3, 5};
 * struct ListNode* result = modifiedList(nums, sizeof(nums)/sizeof(nums[0]), head);
 * // Print or use the modified list as needed
 */
