/**
 * Problem: Compute Hamming Distance
 * Description: Given two integers x and y, calculate the Hamming distance between them. 
 * The Hamming distance is the number of positions at which the corresponding bits are different.
 * 
 * @param x: The first integer.
 * @param y: The second integer.
 * @return: The Hamming distance between x and y.
 */
int hammingDistance(int x, int y) {
    int c = x ^ y; // XOR operation gives the bits that are different between x and y
    int count = 0;

    // Count the number of set bits (1s) in the result of XOR operation
    while (c > 0) {
        if (c % 2 == 1) {
            count++;
        }
        c = c / 2; // Move to the next bit
    }

    return count;
}

## Time Complexity: O(1), as the number of bits in the integers is constant.
## Space Complexity: O(1), as we use only a constant amount of extra space.
