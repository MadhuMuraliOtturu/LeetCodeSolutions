# Problem: Distinct Prime Factors of Array Product
# Description: Given an array `nums`, the task is to return the number of distinct prime factors 
# of the product of the elements of the array `nums`.

from math import isqrt

class Solution(object):
    def distinctPrimeFactors(self, nums):
        """
        Finds the number of distinct prime factors of the product of elements in the array `nums`.
        
        :param nums: List of integers.
        :return: Integer, the number of distinct prime factors.
        """
        n = max(nums) + 1  # Upper bound for sieve of Eratosthenes
        prime = [True] * (n + 1)  
        prime[0] = prime[1] = False  # 0 and 1 are not prime numbers
        
        # Sieve of Eratosthenes to mark all primes
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        
        # Set to store distinct prime factors
        s = set()
        
        # For each number in nums, find its prime factors
        for num in nums:
            # Check divisibility by each prime number
            for i in range(2, n // 2 + 1):
                if prime[i] and num % i == 0:
                    s.add(i)
            # If the number itself is prime
            if prime[num] and num % num == 0:
                s.add(num)
        
        return len(s)

# Time Complexity: O(n log log n + m * sqrt(n)), where n is the maximum element in `nums` for the sieve 
# and m is the number of elements in `nums`. The sieve of Eratosthenes runs in O(n log log n), 
# and finding prime factors takes O(sqrt(n)) for each element.
# Space Complexity: O(n), for storing the prime sieve and the set of distinct primes.

# Example usage:
# solution = Solution()
# nums = [12, 15, 18]
# print(solution.distinctPrimeFactors(nums))  # Expected output: 3 (distinct prime factors are 2, 3, 5)
