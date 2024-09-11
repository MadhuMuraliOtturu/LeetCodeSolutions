# Problem: Find Prime Pairs
# Description: Given an integer `n`, find all pairs of prime numbers that sum up to `n`. 
# The prime pairs should be unique, and each pair should be in ascending order.

class Solution(object):
    def findPrimePairs(self, n):
        """
        Finds all unique pairs of prime numbers that sum up to `n`.

        :param n: Integer, the target sum for the prime pairs.
        :return: List of lists, each containing two prime numbers that sum up to `n`.
        """
        # Step 1: Create a boolean list to mark prime numbers using Sieve of Eratosthenes.
        l = [True] * (n + 1)
        p = 2
        while p * p < n:
            if l[p]:
                for i in range(p * p, n, p):
                    l[i] = False
            p += 1
        
        # Step 2: Find pairs of primes that sum up to `n`.
        arr = []
        for i in range(2, n // 2 + 1):
            remain = n - i
            if l[i] and l[remain] and i <= remain:
                arr.append([i, remain])
        return arr

## Time Complexity: O(N log log N), where N is the number `n`, because of the Sieve of Eratosthenes.
## Space Complexity: O(N), for storing the boolean list `l` to mark primes.

# Example usage:
# solution = Solution()
# print(solution.findPrimePairs(10))  
# Expected output: [[3, 7], [5, 5]], since 3+7 and 5+5 are the prime pairs summing to 10.
