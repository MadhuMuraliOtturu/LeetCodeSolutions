class Solution(object):
    def construct2DArray(self, original, m, n):
        # Initialize row and column indices
        i = 0
        j = 0
        
        # Initialize the result matrix and a temporary list for current row
        matrix = []
        l = []
        
        # Check if the original array can be reshaped into an m x n matrix
        if len(original) != m * n:
            return []  # Return an empty list if the reshape is not possible
        
        # Iterate through the original array to populate the matrix
        while i < len(original):
            if j < n:
                # Append the current element to the temporary row list
                l.append(original[i])
                j += 1
            if j == n:
                # If the row is complete, reset column index and append the row to the matrix
                j = 0
                matrix.append(l)
                l = []
            i += 1
        
        # Return the constructed 2D matrix
        return matrix

## Time Complexity: O(m * n)
# - Where m is the number of rows and n is the number of columns.
# - The time complexity is O(m * n) because we iterate through the original array once and append elements to the matrix.

## Space Complexity: O(m * n)
# - The space complexity is O(m * n) due to the storage needed for the 2D matrix.
