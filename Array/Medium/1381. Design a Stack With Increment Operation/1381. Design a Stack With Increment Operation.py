# Problem: Design a Stack with Increment Operation
# Description: Design a stack-like data structure that supports the following operations:
# - `push(x)`: Pushes the integer `x` onto the stack. If the stack size reaches the max size, the push is ignored.
# - `pop()`: Removes and returns the top element of the stack. If the stack is empty, return `-1`.
# - `increment(k, val)`: Increment the bottom `k` elements of the stack by `val`. If there are fewer than `k` elements, all elements are incremented.

class CustomStack(object):

    def __init__(self, maxSize):
        """
        Initializes the stack with a given maxSize.
        :param maxSize: int, the maximum size of the stack.
        """
        self.stack = []
        self.maxSize = maxSize
        self.size = 0

    def push(self, x):
        """
        Pushes an integer x onto the stack if the size is less than the maxSize.
        :param x: int, the value to push onto the stack.
        :return: None
        """
        if self.size < self.maxSize:
            self.stack.append(x)
            self.size += 1

    def pop(self):
        """
        Removes and returns the top element of the stack. If the stack is empty, returns -1.
        :return: int, the top element of the stack or -1 if empty.
        """
        if self.size == 0:
            return -1
        y = self.stack.pop()
        self.size -= 1
        return y

    def increment(self, k, val):
        """
        Increments the bottom k elements of the stack by val. If there are fewer than k elements, all elements are incremented.
        :param k: int, the number of elements to increment from the bottom.
        :param val: int, the value to increment each of the bottom k elements by.
        :return: None
        """
        if self.size < k:
            for i in range(self.size):
                self.stack[i] += val
        else:
            for j in range(k):
                self.stack[j] += val


## Time Complexity:
# - `push`: O(1), since appending an element is a constant time operation.
# - `pop`: O(1), as removing the top element is also a constant time operation.
# - `increment`: O(min(k, n)), where k is the number of elements to increment and n is the size of the stack.

## Space Complexity: O(n), where n is the size of the stack.

# Example usage:
# obj = CustomStack(3)
# obj.push(1)  # Stack: [1]
# obj.push(2)  # Stack: [1, 2]
# param_2 = obj.pop()  # Expected output: 2, Stack: [1]
# obj.increment(2, 5)  # Stack: [6]
# obj.push(3)  # Stack: [6, 3]
# print(obj.pop())  # Expected output: 3
