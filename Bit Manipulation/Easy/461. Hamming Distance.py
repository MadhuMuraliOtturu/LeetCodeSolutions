# Problem: Calculate Hamming Distance
# Description: Given two integers x and y, return the Hamming distance between them, which is the number of positions 
# at which the corresponding bits are different.

class Solution(object):
    def hammingDistance(self, x, y):
        """
        Calculates the Hamming distance between two integers x and y. The Hamming distance is defined as the number of 
        positions at which the corresponding bits are different.

        :param x: Integer, the first integer.
        :param y: Integer, the second integer.
        :return: Integer, the Hamming distance between x and y.
        """
        return bin(x ^ y).replace('0b', "").count('1')

## Time Complexity: O(1), as the bitwise XOR operation and counting bits are constant-time operations.
## Space Complexity: O(1), as we only use a constant amount of extra space.

# Example usage:
# solution = Solution()
# print(solution.hammingDistance(1, 4))  # Expected to return 2
