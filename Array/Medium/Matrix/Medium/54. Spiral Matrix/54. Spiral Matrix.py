# Problem: Spiral Matrix
# Description: Given a matrix of m x n elements, return all elements of the matrix in spiral order.

class Solution(object):
    def spiralOrder(self, matrix):
        """
        Returns the elements of a matrix in spiral order.

        :param matrix: List[List[int]], a 2D matrix of integers.
        :return: List[int], the elements of the matrix in spiral order.
        """
        
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        ans = []
        
        # Traverse the matrix in a spiral order
        while top < bottom and left < right:
            # Get every element in the top row
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1
            
            # Get every element in the right column
            for j in range(top, bottom):
                ans.append(matrix[j][right - 1])
            right -= 1
            
            # Check if the spiral is complete
            if not (left < right and top < bottom):
                break
            
            # Get every element in the bottom row
            for k in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][k])
            bottom -= 1
            
            # Get every element in the left column
            for l in range(bottom - 1, top - 1, -1):
                ans.append(matrix[l][left])
            left += 1
        
        return ans

## Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the matrix.
## Space Complexity: O(1), as we are not using any extra space except for the output list.

# Example usage:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# solution = Solution()
# print(solution.spiralOrder(matrix))  
# Expected output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
