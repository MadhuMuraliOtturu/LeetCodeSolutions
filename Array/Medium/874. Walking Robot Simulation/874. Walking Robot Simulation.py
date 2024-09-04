# Problem: LeetCode 874 - Walking Robot Simulation
# https://leetcode.com/problems/walking-robot-simulation/

import math

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        Simulates the movement of a robot based on the given commands and obstacles on a 2D grid.

        :param commands: List[int], a list of integers representing commands to move forward or turn.
                         -1 for turning right 90 degrees, -2 for turning left 90 degrees, and positive
                         integers for moving forward that many units.
        :param obstacles: List[List[int]], a list of pairs of integers representing obstacle coordinates.
        :return: int, the maximum Euclidean distance squared from the origin after executing the commands.
        """

        dir = 'N'  # Initial direction is North
        init = [0, 0]  # Starting position (0, 0)
        equ = 0  # Variable to track the maximum Euclidean distance squared
        obstacle_set = set(map(tuple, obstacles))  # Convert obstacles list to a set of tuples for O(1) lookup

        # Step 1: Process each command in the commands list
        for i in commands:
            if i == -1:  # Turn right 90 degrees
                if dir == 'N':
                    dir = "E"
                elif dir == 'E':
                    dir = 'S'
                elif dir == 'S':
                    dir = 'W'
                elif dir == 'W':
                    dir = 'N'
            elif i == -2:  # Turn left 90 degrees
                if dir == 'N':
                    dir = 'W'
                elif dir == 'W':
                    dir = 'S'
                elif dir == 'S':
                    dir = 'E'
                elif dir == 'E':
                    dir = 'N'
            else:
                # Step 2: Move forward 'i' units in the current direction
                for _ in range(i):
                    if dir == 'E':
                        next_pos = [init[0] + 1, init[1]]
                    elif dir == 'N':
                        next_pos = [init[0], init[1] + 1]
                    elif dir == 'W':
                        next_pos = [init[0] - 1, init[1]]
                    elif dir == 'S':
                        next_pos = [init[0], init[1] - 1]
                    
                    # Step 3: Check if the next position is an obstacle
                    if tuple(next_pos) in obstacle_set:
                        break  # Stop moving forward if an obstacle is encountered
                    init = next_pos  # Update the robot's position

            # Step 4: Update the maximum Euclidean distance squared
            equ = max(equ, init[0]**2 + init[1]**2)
        
        return equ  # Return the maximum distance squared from the origin

## Time Complexity: O(N + M), where N is the number of commands and M is the number of obstacles.
## Space Complexity: O(M), for storing the set of obstacles.

# Example usage:
# solution = Solution()
# print(solution.robotSim([4,-1,3], []))  # Output should be 25
# print(solution.robotSim([4,-1,4,-2,4], [[2,4]]))  # Output should be 65
