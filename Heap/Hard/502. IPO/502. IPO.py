# Problem: Find Maximized Capital
# Description:
# Suppose you have `k` projects to complete and an initial capital `w`. Each project has a profit and a minimum required capital to start it. 
# The goal is to maximize your capital by selecting up to `k` projects that can be completed based on the current available capital.
# You are allowed to complete a project only if your available capital is greater than or equal to the minimum required capital of that project.
# Once a project is completed, your capital is increased by the profit earned from that project.
# 
# You are given two lists: `profits` and `capital`, where `profits[i]` is the profit of the `i`th project, and `capital[i]` is the minimum capital required to start the `i`th project.
# 
# The task is to maximize your capital by completing up to `k` projects.
#
# Example:
# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
#
# Explanation:
# - Start with an initial capital of 0.
# - Pick the project with a capital requirement of 0 and profit of 1.
# - After completing the first project, the capital is 1. Now pick the project with profit 3.
# - The final capital is 4.

from typing import List
import heapq

class Solution:
    """
    Finds the maximum capital after completing up to k projects.
    
    :param k: int, the number of projects that can be completed.
    :param w: int, the initial capital available.
    :param profits: List[int], the list of profits for each project.
    :param capital: List[int], the list of minimum capital required to start each project.
    :return: int, the maximum capital after completing up to k projects.
    """
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = []
        n = len(profits)

        # Store capital and profit pairs and sort by capital
        for i in range(n):
            projects.append([capital[i], profits[i]])
        projects.sort(key=lambda x: (x[0], x[1]))

        max_heap = []
        idx = 0

        while k > 0:
            # Add all projects whose capital requirement is <= current available capital
            while idx < n and projects[idx][0] <= w:
                heapq.heappush(max_heap, -projects[idx][1])  # Push profit as negative to simulate max heap
                idx += 1

            # If no projects can be completed, return the current capital
            if max_heap:
                w -= heapq.heappop(max_heap)  # Increase capital by the largest profit project
            else:
                break  # No more projects can be completed

            k -= 1

        return w

# Time Complexity: O(n log n), where n is the number of projects. Sorting the projects takes O(n log n) and each insertion/extraction from the heap is log n.
# Space Complexity: O(n), where n is the number of projects. We store all the projects and use a heap.

# Example usage:
# solution = Solution()
# max_capital = solution.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1])
# print(max_capital)  # Output: 4
