class Solution(object):
    def chalkReplacer(self, chalk, k):
        # Calculate the total amount of chalk needed to complete one full cycle
        x = sum(chalk)
        
        # Find the remaining chalk after completing full cycles
        y = k % x
        
        # Iterate through the chalk array to determine the index where the chalk will run out
        for i in range(len(chalk)):
            # Check if the current student has enough chalk to cover the remaining amount
            if chalk[i] > y:
                # If yes, return the current index
                return i
            # Otherwise, reduce the remaining chalk amount by the current student's usage
            y -= chalk[i]
        
        # If no student is found to be the one running out of chalk, return 0 (shouldn't happen)
        return 0
## Time Complexity: O(n)
# - Where n is the number of students (length of the chalk array).
# - The time complexity is O(n) because we sum up all elements of the chalk array (O(n)) 
#   and then perform a single pass through the array to find the index (O(n)).

## Space Complexity: O(1)
# - The space complexity is O(1) because we use a constant amount of extra space
#   (for variables x and y), and the size of the input array does not affect the space usage.
