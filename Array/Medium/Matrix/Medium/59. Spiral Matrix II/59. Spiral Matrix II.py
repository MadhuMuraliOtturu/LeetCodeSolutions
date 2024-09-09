# Problem: Generate a Spiral Matrix
# Description: Given a positive integer `n`, generate an `n x n` matrix filled with elements from 1 to `n^2` in spiral order.

class Solution(object):
    def generateMatrix(self, n):
        """
        Generates an `n x n` matrix filled with elements from 1 to `n^2` in spiral order.

        :param n: Integer, the size of the matrix.
        :return: List[List[int]], the generated matrix in spiral order.
        """
        ans = [[-1 for _ in range(n)] for _ in range(n)]
        i = top = left = 0
        bottom = right = n
        size = n**2
        
        # Fill the matrix in spiral order
        while i < size:
            # Fill the top row
            for a in range(left, right):
                ans[top][a] = i + 1
                i += 1
            top += 1
            
            # Fill the right column
            for b in range(top, bottom):
                ans[b][right - 1] = i + 1
                i += 1
            right -= 1
            
            # Fill the bottom row
            for c in range(right - 1, left - 1, -1):
                ans[bottom - 1][c] = i + 1
                i += 1
            bottom -= 1
            
            # Fill the left column
            for d in range(bottom - 1, top - 1, -1):
                ans[d][left] = i + 1
                i += 1
            left += 1
        
        return ans

## Time Complexity: O(N^2), where N is the size of the matrix.
## Space Complexity: O(1), since we use a constant amount of extra space besides the matrix itself.

# Example usage:
# solution = Solution()
# print(solution.generateMatrix(3))  
# Expected output:
# [[1, 2, 3], 
#  [8, 9, 4], 
#  [7, 6, 5]]
