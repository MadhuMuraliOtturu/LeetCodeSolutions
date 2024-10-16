# Problem: Longest Diverse String
# Description:
# Given three integers x, y, and z, representing the number of letters 'a', 'b', and 'c' respectively, 
# the goal is to construct the longest possible string that can be formed using these letters, 
# where the same letter cannot appear more than two times in a row. Return the resulting string.

class Solution:
    def longestDiverseString(self, x: int, y: int, z: int) -> str:
        """
        Constructs the longest string using 'a', 'b', and 'c' given their respective counts
        such that no letter appears more than twice consecutively.

        :param x: int, count of letter 'a'
        :param y: int, count of letter 'b'
        :param z: int, count of letter 'c'
        :return: str, the longest diverse string possible
        """
        l = [('a', x), ('b', y), ('c', z)]  # List of letters with their counts
        ans = ""  # Resulting string
        
        while True:
            l.sort(key=lambda item: item[1], reverse=True)  # Sort by remaining counts
            
            if l[0][1] == 0:  # If the highest count is zero, break the loop
                break
            
            if len(ans) >= 2 and ans[-1] == l[0][0] and ans[-2] == l[0][0]:
                # If the last two letters are the same as the most available letter
                if l[1][1] > 0:  # Check if the second most available letter can be used
                    ans += l[1][0]  # Add the second letter
                    l[1] = (l[1][0], l[1][1] - 1)  # Decrement its count
                else:
                    break  # No more letters can be added
            else:
                # Add the most available letter
                if l[0][1] > 1:  # If more than one is available
                    ans += l[0][0] * 2  # Add two of the same letter
                    l[0] = (l[0][0], l[0][1] - 2)  # Decrement its count by 2
                else:
                    ans += l[0][0]  # Add one of the same letter
                    l[0] = (l[0][0], l[0][1] - 1)  # Decrement its count by 1

        return ans  # Return the resulting string

# Time Complexity: O(n log n), where n is the total number of letters. Sorting the list of letters
# in each iteration results in a logarithmic factor.
# Space Complexity: O(1), as we are using a fixed number of variables and a list of constant size.

# Example usage:
# solution = Solution()
# print(solution.longestDiverseString(1, 1, 7))  # Expected output: "ccbccacc"

