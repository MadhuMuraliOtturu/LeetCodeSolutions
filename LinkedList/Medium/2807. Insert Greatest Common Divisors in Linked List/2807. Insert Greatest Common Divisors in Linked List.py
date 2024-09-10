# Problem: Insert Greatest Common Divisors (GCD) Between Nodes
# Description: Given a singly-linked list, insert a new node between every two adjacent nodes such that 
# the value of the new node is the greatest common divisor (GCD) of the values of the adjacent nodes.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        Inserts a node with the greatest common divisor (GCD) between every two adjacent nodes.

        :param head: ListNode, the head of the singly-linked list.
        :return: ListNode, the head of the modified linked list.
        """
        def gcd(a, b):
            """
            Computes the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

            :param a: Integer, the first number.
            :param b: Integer, the second number.
            :return: Integer, the GCD of a and b.
            """
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        node1 = head
        # Traverse through the list and insert GCD nodes
        while node1 and node1.next:
            node2 = node1.next
            a = node1.val
            b = node2.val
            # Create a new node with the GCD of the values of node1 and node2
            gcd_node = ListNode(gcd(a, b))
            node1.next = gcd_node
            gcd_node.next = node2
            node1 = node2  # Move to the next pair

        return head

## Time Complexity: O(N), where N is the number of nodes in the list.
## Space Complexity: O(1), as we only use a constant amount of extra space.

# Example usage:
# head = ListNode(18)
# head.next = ListNode(24)
# head.next.next = ListNode(36)
# solution = Solution()
# result = solution.insertGreatestCommonDivisors(head)
# print(result)  # Expected output: 18 -> 6 -> 24 -> 12 -> 36
