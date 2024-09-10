# Problem: Find Occurrences of Element in Array
# Description: Given an array of integers `nums`, a list of queries, and an integer `x`, 
# find the positions of the element `x` in the array. For each query, return the position of the `x`th occurrence
# or -1 if the occurrence does not exist.

class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        Finds the positions of the `x`th occurrence of an element in an array for each query.

        :param nums: List[int], the array of integers.
        :param queries: List[int], the list of queries for occurrences.
        :param x: Integer, the element to find occurrences of.
        :return: List[int], a list of positions for each query.
        """
        ans = []
        arr = []
        # Step 1: Collect the indices of occurrences of `x`
        for i in range(len(nums)):
            if nums[i] == x:
                ans.append(i)
        
        # Step 2: For each query, find the index of the `x`th occurrence or return -1 if not found
        for query in queries:
            if query > len(ans):
                arr.append(-1)
            else:
                arr.append(ans[query - 1])
        return arr

## Time Complexity: O(N + Q), where N is the length of the array and Q is the number of queries.
## Space Complexity: O(K), where K is the number of occurrences of the element `x`.

# Example usage:
# solution = Solution()
# print(solution.occurrencesOfElement([1, 2, 3, 2, 2, 5], [1, 2, 3], 2))  
# Expected output: [1, 3, 4], because 2 occurs at indices 1, 3, and 4.
