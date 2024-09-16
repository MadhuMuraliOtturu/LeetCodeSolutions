# Problem: Minimum Time Difference
# Description: Given a list of 24-hour time points in "HH:MM" format, find the minimum difference between any two time points in minutes.

from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        This function calculates the minimum time difference between any two time points in a list.
        
        :param timePoints: A list of strings representing time in "HH:MM" format.
        :return: The minimum time difference in minutes between any two time points.
        """
        ans = []
        
        # Step 1: Convert each time point to minutes and store it in ans
        for time in timePoints:
            hour, mins = time.split(":")
            ans.append(int(hour) * 60 + int(mins))  # Convert time to minutes
        
        # Step 2: Sort the time points in ascending order
        ans.sort()
        
        # Step 3: Initialize the minimum difference with a large value
        min_diff = 10**4 + 1  # Larger than the possible maximum difference (1440)
        
        # Step 4: Calculate the difference between consecutive time points
        for i in range(1, len(ans)):
            min_diff = min(min_diff, ans[i] - ans[i - 1])
        
        # Step 5: Check the edge case where the difference is between the last and first time points across midnight
        return min(min_diff, 1440 - ans[-1] + ans[0])

# Time Complexity: O(n log n), where n is the number of time points. Sorting the list takes O(n log n), and comparing adjacent elements takes O(n).
# Space Complexity: O(n), where n is the number of time points. We use additional space to store the converted time points.

# Example usage:
# solution = Solution()
# timePoints = ["23:59", "00:00", "12:34"]
# print(solution.findMinDifference(timePoints))  # Expected output: 1
