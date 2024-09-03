class Solution(object):
    def passThePillow(self, n, time):
        """
        Determines the position of the pillow after a certain amount of time
        when n people are passing a pillow around in a circular manner.

        Args:
        n (int): The number of people in the circle.
        time (int): The total time or number of passes.

        Returns:
        int: The position of the person holding the pillow after the given time.
        """

        # Step 1: Calculate the number of complete rounds the pillow makes around the circle.
        # A complete round occurs when the pillow is passed from the first person to the last and back.
        rounds = time // (n - 1)

        # Step 2: Calculate the remaining time after the last complete round.
        # This represents the number of steps or passes left after completing the full cycles.
        remaining_time = time % (n - 1)

        # Step 3: Determine the direction and return the final position.
        # If the number of rounds is even, the pillow continues in the forward direction.
        # If the number of rounds is odd, the pillow moves in the reverse direction.
        if rounds % 2 == 0:
            return 1 + remaining_time
        else:
            return n - remaining_time

## Time Complexity: O(1)
# The function performs a constant number of operations, regardless of the input size n.

## Space Complexity: O(1)
# The function uses a constant amount of space, requiring no additional memory that scales with the input size.

# Example Usage:
# solution = Solution()
# result = solution.passThePillow(5, 7)
# print(result)  # Output will be the position of the pillow after 7 passes with 5 people.
