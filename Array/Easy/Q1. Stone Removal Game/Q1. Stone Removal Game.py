# Problem: Can Alice Win?
# Description:
# Alice and Bob play a game where they start with `n` stones. Alice removes the first 10 stones,
# then 9, 8, and so on, alternating turns with Bob. The player unable to make a valid move loses.
# Determine if Alice can win if both players play optimally.
#
# Example:
# Input: n = 20
# Output: False
# Explanation: Bob will win since the last move leaves Alice with no valid stones to remove.
#
# Constraints:
# - 1 <= n <= 10^9

class Solution:
    """
    Determines if Alice can win the game based on the number of stones `n`.

    :param n: int - Initial number of stones.
    :return: bool - True if Alice can win, False otherwise.
    """
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
            
        stones = n
        stones_to_remove = 10
        is_alice_turn = True  # True means it's Alice's turn, False means Bob's turn.
        
        while stones >= stones_to_remove and stones_to_remove > 0:
            stones -= stones_to_remove
            stones_to_remove -= 1
            is_alice_turn = not is_alice_turn
            
        # If no stones remain, check whose turn it was before the game ended.
        if stones == 0:
            return not is_alice_turn  # If it's Bob's turn, Alice wins.
            
        return not is_alice_turn

# Time Complexity: O(√n) - Stones are reduced in a decreasing sequence.
# Space Complexity: O(1) - Constant space usage.

# Example usage:
# solution = Solution()
# print(solution.canAliceWin(20))  # Output: False
# print(solution.canAliceWin(15))  # Output: True
