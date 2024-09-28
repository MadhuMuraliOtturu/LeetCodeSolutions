# Problem: Design a Circular Deque
# Description: Implement the `MyCircularDeque` class that supports the following operations:
# - `insertFront`: Inserts an item at the front of the deque. Return True if the operation is successful.
# - `insertLast`: Inserts an item at the rear of the deque. Return True if the operation is successful.
# - `deleteFront`: Deletes an item from the front of the deque. Return True if the operation is successful.
# - `deleteLast`: Deletes an item from the rear of the deque. Return True if the operation is successful.
# - `getFront`: Gets the front item from the deque.
# - `getRear`: Gets the last item from the deque.
# - `isEmpty`: Checks whether the deque is empty.
# - `isFull`: Checks whether the deque is full.

class ListNode:
    def __init__(self, val):
        """
        Initializes a node with a given value and next pointer set to None.
        :param val: int, the value of the node.
        """
        self.val = val
        self.next = None


class MyCircularDeque:
    def __init__(self, k):
        """
        Initializes the circular deque with a maximum size of k.
        :param k: int, the maximum capacity of the deque.
        """
        self.head = None
        self.tail = None
        self.size = 0
        self.k = k

    def insertFront(self, value):
        """
        Inserts an element at the front of the deque.
        :param value: int, the value to insert.
        :return: bool, True if the insertion is successful, False otherwise.
        """
        if self.size < self.k:
            newnode = ListNode(value)
            newnode.next = self.head
            self.head = newnode
            if self.tail is None:
                self.tail = newnode
            self.size += 1
            return True
        return False

    def insertLast(self, value):
        """
        Inserts an element at the rear of the deque.
        :param value: int, the value to insert.
        :return: bool, True if the insertion is successful, False otherwise.
        """
        if self.size < self.k:
            newnode = ListNode(value)
            if self.head is None:
                return self.insertFront(value)
            self.tail.next = newnode
            self.tail = newnode
            self.size += 1
            return True
        return False

    def deleteFront(self):
        """
        Deletes an element from the front of the deque.
        :return: bool, True if the deletion is successful, False otherwise.
        """
        if self.head is None:
            return False
        temp = self.head
        self.head = self.head.next
        temp.next = None
        if self.head is None:
            self.tail = None
        self.size -= 1
        return True

    def deleteLast(self):
        """
        Deletes an element from the rear of the deque.
        :return: bool, True if the deletion is successful, False otherwise.
        """
        if self.head is None:
            return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.size -= 1
        return True

    def getFront(self):
        """
        Gets the front element of the deque.
        :return: int, the value of the front element, or -1 if the deque is empty.
        """
        if self.head:
            return self.head.val
        return -1

    def getRear(self):
        """
        Gets the rear element of the deque.
        :return: int, the value of the rear element, or -1 if the deque is empty.
        """
        if self.tail:
            return self.tail.val
        return -1

    def isEmpty(self):
        """
        Checks whether the deque is empty.
        :return: bool, True if the deque is empty, False otherwise.
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the deque is full.
        :return: bool, True if the deque is full, False otherwise.
        """
        return self.size == self.k


## Time Complexity: O(1) for all operations except for `deleteLast` which can take O(N) in the worst case.
## Space Complexity: O(N), where N is the maximum number of elements in the deque (limited by k).

# Example usage:
# obj = MyCircularDeque(3)
# print(obj.insertFront(1))  # Expected output: True
# print(obj.insertLast(2))   # Expected output: True
# print(obj.deleteFront())   # Expected output: True
# print(obj.getFront())      # Expected output: 2
# print(obj.getRear())       # Expected output: 2
# print(obj.isEmpty())       # Expected output: False
# print(obj.isFull())        # Expected output: False
