# Problem: K-th Nearest Obstacle Queries
# Description: Given a list of queries where each query is a coordinate (x, y) representing an obstacle's position,
#              and an integer k, return an array where each element is the k-th nearest obstacle's Manhattan distance
#              to the origin (0, 0). If there are fewer than k obstacles seen so far, return -1 for that query.

import heapq

class Solution(object):
    def resultsArray(self, queries, k):
        """
        Finds the k-th nearest obstacle's Manhattan distance to the origin for each query.

        :param queries: List of lists, where each inner list is [x, y] representing an obstacle's coordinates.
        :param k: Integer, the k-th nearest obstacle to track.
        :return: List of integers, where each element is the k-th nearest obstacle's distance or -1 if fewer than k obstacles.
        """
        distance = []  # Max-heap to store distances, but with negative values for Python's min-heap implementation
        answer = []    # List to store the results

        # Step 1: Process each query to calculate the Manhattan distance and track the k-th nearest
        for query in queries:
            dis = abs(query[0]) + abs(query[1])  # Calculate Manhattan distance from the origin
            heapq.heappush(distance, -dis)  # Push the negative distance to maintain a max-heap

            # If the heap exceeds size k, remove the largest (i.e., smallest negative) element
            if len(distance) > k:
                heapq.heappop(distance)

            # If the heap has exactly k elements, the k-th nearest obstacle is at the root
            if len(distance) == k:
                answer.append(-distance[0])  # Convert back to positive
            else:
                answer.append(-1)  # If fewer than k obstacles, return -1
        
        return answer

## Time Complexity: O(N * log(k)), where N is the number of queries and k is the specified nearest obstacle.
## Space Complexity: O(k), for storing the distances in the heap.

# Example usage:
# solution = Solution()
# print(solution.resultsArray([[1,2], [2,3], [3,4]], 2))  # Example output might be [-1, 5, 7]
