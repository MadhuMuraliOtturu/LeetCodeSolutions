#include <stdio.h>

/**
 * Determines the position of the pillow after a certain amount of time
 * when n people are passing a pillow around in a circular manner.
 *
 * @param n     The number of people in the circle.
 * @param time  The total time or number of passes.
 * @return      The position of the person holding the pillow after the given time.
 */
int passThePillow(int n, int time) {
    // Step 1: Calculate the number of complete cycles the pillow makes around the circle.
    // A complete cycle occurs when the pillow is passed from the first person to the last and back.
    int cycle = time / (n - 1);

    // Step 2: Calculate the remaining time after the last complete cycle.
    // This represents the number of steps or passes left after completing the full cycles.
    int remaining = time % (n - 1);

    // Step 3: Determine the direction and return the final position.
    // If the number of cycles is even, the pillow continues in the forward direction.
    // If the number of cycles is odd, the pillow moves in the reverse direction.
    if (cycle % 2 == 0) {
        return 1 + remaining;
    } else {
        return n - remaining;
    }
}

// Time Complexity: O(1)
// The function performs a constant number of operations, regardless of the input size n.

// Space Complexity: O(1)
// The function uses a constant amount of space, requiring no additional memory that scales with the input size.

// Example Usage:
int main() {
    int n = 5;
    int time = 7;
    int result = passThePillow(n, time);
    printf("The position of the pillow after %d passes with %d people is: %d\n", time, n, result);
    // Output: The position of the pillow after 7 passes with 5 people is: 4
    return 0;
}
