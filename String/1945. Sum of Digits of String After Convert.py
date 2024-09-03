# Problem: LeetCode 1945 - Sum of Digits of String After Convert
# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution(object):
    def sum_digit(self, num):
        """
        Helper function to sum the digits of a number.
        :param num: Integer, the number whose digits are to be summed.
        :return: Integer, the sum of the digits.
        """
        co = 0
        while num > 0:
            r = num % 10
            co += r
            num //= 10
        return co

    def getLucky(self, s, k):
        """
        Converts each letter in the string to its corresponding number in the alphabet,
        concatenates these numbers, and then repeatedly sums the digits 'k' times.

        :param s: String, consisting of lowercase English letters.
        :param k: Integer, the number of times to sum the digits.
        :return: Integer, the final result after 'k' transformations.
        """
        # Step 1: Convert each letter to its position in the alphabet
        co = ""
        for i in s:
            x = str(ord(i) - 96)
            co += x
        
        # Convert the concatenated string of numbers into an integer
        x = int(co)
        print(x)
        
        # Step 2: Sum the digits 'k' times
        for i in range(k):
            x = self.sum_digit(x)
            print(x)
        
        return x

## Time Complexity: O(K*log(N))
## Space Complexity: O(log(N))
# Example usage:
# solution = Solution()
# print(solution.getLucky("leetcode", 2))  # Output should match the expected result after the transformation
