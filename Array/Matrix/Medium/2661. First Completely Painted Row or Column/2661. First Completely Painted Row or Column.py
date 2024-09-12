# Problem: First Complete Index in a Matrix
# Description: Given a 2D matrix `mat` and a list of integers `arr`, find the first index in `arr` 
# such that all the elements in either a row or column in `mat` are present in the subarray of `arr`
# up to and including the element at the current index. Return that index.
# If no such row or column is found, return -1.

class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        Finds the first index in arr such that either a row or a column in mat becomes completely filled
        with the elements seen in arr up to and including that index.

        :param arr: List of integers representing the sequence in which elements from mat are visited.
        :param mat: 2D List (matrix) of integers.
        :return: Integer, the first index in arr where a row or column is completely filled, or -1 if none.
        """
        m = len(mat)
        n = len(mat[0])
        
        # Initialize lists to keep track of remaining elements in each row and column
        row_remaining = [n] * m
        col_remaining = [m] * n
        
        # Create a dictionary to map each value to its position in the matrix
        position = {}
        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)
        
        # Process the elements in arr
        for index, num in enumerate(arr):
            r, c = position[num]
            row_remaining[r] -= 1
            col_remaining[c] -= 1
            
            # Check if any row or column is complete
            if row_remaining[r] == 0 or col_remaining[c] == 0:
                return index
        
        return -1  # In case no complete row or column is found

# Time Complexity: O(m * n + len(arr)), where m is the number of rows, n is the number of columns in the matrix,
# and len(arr) is the length of the input array arr. We process each element in arr and update row/column counts accordingly.
# Space Complexity: O(m * n), due to the storage required for the position mapping and row/column trackers.

# Example usage:
# solution = Solution()
# arr = [3, 1, 4, 5, 2]
# mat = [[1, 2], [3, 4]]
# print(solution.firstCompleteIndex(arr, mat))  # Expected output: 3
