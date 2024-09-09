# Problem: Spiral Matrix from Linked List
# Description: Given the head of a singly-linked list and dimensions `m` and `n` for a matrix, 
# fill the matrix in spiral order using the values from the linked list. If the linked list 
# has fewer values than the matrix size, fill remaining cells with `-1`.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        Fills an m x n matrix with values from a singly-linked list in spiral order. If the list 
        has fewer nodes than matrix elements, the remaining cells are filled with `-1`.

        :param m: Integer, the number of rows in the matrix.
        :param n: Integer, the number of columns in the matrix.
        :param head: ListNode, the head of the singly-linked list.
        :return: List[List[int]], the filled matrix in spiral order.
        """
        # Initialize matrix with -1 values
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        temp = head
        top = 0
        bottom = m
        left = 0
        right = n
        
        # Fill the matrix in spiral order using values from the linked list
        while temp:
            # Fill the top row
            for i in range(left, right):
                if not temp:
                    return matrix
                matrix[top][i] = temp.val
                temp = temp.next
            top += 1
            
            # Fill the right column
            for j in range(top, bottom):
                if not temp:
                    return matrix
                matrix[j][right - 1] = temp.val
                temp = temp.next
            right -= 1
            
            # Fill the bottom row
            for k in range(right - 1, left - 1, -1):
                if not temp:
                    return matrix
                matrix[bottom - 1][k] = temp.val
                temp = temp.next
            bottom -= 1
            
            # Fill the left column
            for l in range(bottom - 1, top - 1, -1):
                if not temp:
                    return matrix
                matrix[l][left] = temp.val
                temp = temp.next
            left += 1
        
        return matrix

## Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the matrix.
## Space Complexity: O(1), as we use constant space besides the matrix itself.

# Example usage:
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# solution = Solution()
# print(solution.spiralMatrix(2, 2, head))  
# Expected output: [[1, 2], [3, -1]]
