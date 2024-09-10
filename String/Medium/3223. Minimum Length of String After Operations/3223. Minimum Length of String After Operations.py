# Problem: Minimum Length of a String
# Description: Given a string s, the task is to find the length of the string after removing any number of characters
# from both ends of the string such that the remaining characters do not contain any character that appears more than twice.

class Solution(object):
    def minimumLength(self, s):
        """
        Calculates the minimum length of a string after removing characters from both ends such that no character in 
        the remaining string appears more than twice.

        :param s: String, the input string.
        :return: Integer, the length of the modified string.
        """
        d = {}
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1
            if d[i] > 2:
                d[i] -= 2
        return sum(d.values())

## Time Complexity: O(N), where N is the length of the string.
## Space Complexity: O(1), as the dictionary stores a constant number of unique characters.

# Example usage:
# solution = Solution()
# print(solution.minimumLength("abaccab"))  # Expected to return 1
