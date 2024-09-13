#include <stdlib.h>

/**
 * Problem: XOR Queries of a Subarray
 * Description: Given an array `arr` and a list of queries, where each query is represented by two integers `x` and `y`, 
 * you are to return the XOR of the elements in the subarray between indices `x` and `y` (inclusive).
 *
 * Note: The returned array must be malloced, assume the caller calls free().
 *
 * @param arr: The input array of integers.
 * @param arrSize: The size of the input array.
 * @param queries: The 2D array of queries where each query is represented by two integers.
 * @param queriesSize: The number of queries.
 * @param queriesColSize: The column sizes for the queries (2 for all queries).
 * @param returnSize: Pointer to store the size of the returned result array.
 * @return: An array of integers where each value is the result of a query.
 */
int* xorQueries(int* arr, int arrSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    // Compute the prefix XOR array in-place
    for (int i = 1; i < arrSize; i++) {
        arr[i] = arr[i - 1] ^ arr[i];
    }

    // Allocate memory for the result array
    int *ans = (int*)calloc(queriesSize, sizeof(int));

    // Process each query
    for (int j = 0; j < queriesSize; j++) {
        int x = queries[j][0];
        int y = queries[j][1];
        if (x > 0) {
            ans[j] = arr[y] ^ arr[x - 1];
        } else {
            ans[j] = arr[y];
        }
    }

    // Set the returnSize to the number of queries
    *returnSize = queriesSize;

    return ans;
}

## Time Complexity: O(N + Q), where N is the size of the array and Q is the number of queries.
## Space Complexity: O(Q), where Q is the size of the result array.
