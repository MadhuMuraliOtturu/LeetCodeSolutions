# Problem: Maximum Score from Card Points
# Description: You are given an array `cardPoints` where cardPoints[i] represents the point value of 
# the ith card. You can pick cards from either the beginning or the end of the array. You need to 
# maximize your score by picking exactly `k` cards.

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        Computes the maximum score you can achieve by picking exactly `k` cards from the array `cardPoints`.
        You can pick cards from either the beginning or the end of the array.

        :param cardPoints: List[int], the array of card points.
        :param k: Integer, the number of cards to pick.
        :return: Integer, the maximum score.
        """
        n = len(cardPoints)
        
        # Calculate prefix sum for cardPoints from the left.
        pref_sum = [0] * n
        pref_sum[0] = cardPoints[0]
        for i in range(1, n):
            pref_sum[i] = pref_sum[i-1] + cardPoints[i]
        
        # Calculate suffix sum for cardPoints from the right.
        suff_sum = [0] * n
        suff_sum[-1] = cardPoints[-1]
        for j in range(n-2, -1, -1):
            suff_sum[j] = suff_sum[j+1] + cardPoints[j]
        
        # Initialize the maximum score from the suffix sum.
        max_score = suff_sum[n - k]
        
        # Compare different ways of selecting cards: some from the beginning and some from the end.
        for i in range(1, k):
            current_score = suff_sum[n - (k - i)] + pref_sum[i - 1]
            max_score = max(max_score, current_score)
        
        # Return the maximum of possible scores: prefix only, suffix only, or combinations.
        return max(max_score, pref_sum[k-1], suff_sum[n-k])

## Intuition:
# The idea is to use two pointers or precomputed sums for the prefix and suffix arrays. The prefix sum
# stores the cumulative sum of taking cards from the beginning, while the suffix sum stores the cumulative
# sum of taking cards from the end. The goal is to check different ways to combine the prefix and suffix
# results
