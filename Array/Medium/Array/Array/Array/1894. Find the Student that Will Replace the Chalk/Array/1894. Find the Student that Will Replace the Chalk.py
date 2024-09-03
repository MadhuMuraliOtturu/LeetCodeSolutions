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



---- OPTIMIZED SOLUTION USING BINARY SEARCH AND PREFIX SUM ----

class Solution(object):
    def chalkReplacer(self, chalk, k):
        # Create a prefix sum array to store cumulative sums of chalk usage
        pref_sum = [0] * len(chalk)
        pref_sum[0] = chalk[0]
        
        # Populate the prefix sum array
        for i in range(1, len(chalk)):
            pref_sum[i] = pref_sum[i-1] + chalk[i]
        
        # Reduce k by the total amount of chalk needed for one full cycle
        k = k % pref_sum[-1]
        
        # Initialize binary search bounds
        low = 0
        high = len(chalk) - 1
        
        # Perform binary search to find the index where the remaining chalk will run out
        while low < high:
            mid = (low + high) // 2
            if pref_sum[mid] > k:
                high = mid
            else:
                low = mid + 1
        
        # Return the index where the chalk will run out
        return low

## Time Complexity: O(log(n))
# - Where n is the number of students (length of the chalk array).
# - The time complexity is O(n) for computing the prefix sum array.
# - The binary search process takes O(log n) time. Since O(n) dominates O(log n), the overall time complexity is O(n).

## Space Complexity: O(n)
# - The space complexity is O(n) because of the prefix sum array which requires additional space proportional to the number of students.
