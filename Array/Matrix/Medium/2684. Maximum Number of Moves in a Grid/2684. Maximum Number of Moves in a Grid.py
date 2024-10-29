# Problem: Maximum Moves in Matrix
# Description:
# Given a 2D matrix of integers, the goal is to determine the maximum number of moves 
# one can make from the leftmost column to the rightmost column, where each move is to an adjacent 
# column cell that has a greater value than the current cell. Moves can go to the cell directly to 
# the right or to a cell in the diagonals (up-right or down-right).
#
# Example:
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 3
# Explanation: The longest path is to go right from (0,0) -> (0,1) -> (0,2) -> (1,2).
#
# Constraints:
# - 1 <= len(matrix), len(matrix[0]) <= 1000
# - 1 <= matrix[i][j] <= 10^6

from typing import List

class Solution:
    """
    Solution for finding the maximum number of moves in a matrix from the leftmost to the rightmost column.
    
    :param matrix: List[List[int]] - 2D list of integers representing the matrix.
    :return: int - The maximum number of moves possible from the leftmost to the rightmost column.
    """
    def maxMoves(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        queue = []
        visited = [[False] * n for _ in range(m)]
        dirs = [-1, 0, 1]
        max_moves = 0
        
        for i in range(m):
            visited[i][0] = True
            queue.append((i, 0, 0))

        while queue:
            x, y, moves = queue.pop(0)
            for j in dirs:
                nr = x + j
                nc = y + 1
                if 0 <= nr < m and nc < n and not visited[nr][nc] and matrix[nr][nc] > matrix[x][y]:
                    visited[nr][nc] = True
                    queue.append((nr, nc, moves + 1))
                    max_moves = max(max_moves, moves + 1)

        return max_moves

# Time Complexity: O(m * n) - where m is the number of rows and n is the number of columns, as each cell is visited once.
# Space Complexity: O(m * n) - for the visited matrix and queue storage.

# Example usage:
# solution = Solution()
# print(solution.maxMoves([[3,4,5],[3,2,6],[2,2,1]]))  # Output: 3
