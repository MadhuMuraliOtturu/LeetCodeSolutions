# Problem: Parsing Boolean Expression
# Description:
# We are given a boolean expression as a string exp, consisting of:
# - 't' for True
# - 'f' for False
# - '!' for NOT operation
# - '&' for AND operation
# - '|' for OR operation
# The expression can also include parentheses to denote operator precedence.
# The task is to evaluate the given boolean expression and return the result as a boolean value.

class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        """
        Parses and evaluates the given boolean expression exp.

        :param exp: str, the boolean expression to parse and evaluate.
        :return: bool, the result of the boolean expression evaluation.
        """
        i = 0
        n = len(exp)
        symbol = []  # Stack to hold operators like &, |, !
        stack = []   # Stack to evaluate the boolean values

        while i < n:
            if exp[i] != ",":  # Ignore commas in the expression
                if exp[i] in "&|!":  # Push operators onto the symbol stack
                    symbol.append(exp[i])
                elif exp[i] == ')':  # Evaluate the expression when encountering a closing parenthesis
                    curr_op = symbol.pop()
                    curr_sy = []
                    
                    # Collect all values within the parentheses
                    while stack and stack[-1] != '(':
                        curr_sy.append(stack.pop())
                    stack.pop()  # Remove the opening parenthesis

                    # Evaluate based on the current operator
                    if curr_op == '&':
                        result = True
                        for val in reversed(curr_sy):
                            result = result and val
                        stack.append(result)
                    elif curr_op == '|':
                        result = False
                        for val in reversed(curr_sy):
                            result = result or val
                        stack.append(result)
                    elif curr_op == '!':
                        stack.append(not curr_sy[-1])
                elif exp[i] in "tf":  # Convert 't' to True and 'f' to False
                    stack.append(exp[i] == 't')
                else:
                    stack.append(exp[i])
                
            i += 1

        return stack[0] if stack else False

# Time Complexity: O(n), where n is the length of the boolean expression. We iterate through the expression once.
# Space Complexity: O(n), as we use two stacks (one for symbols and one for values) that can grow up to the size of the expression.

# Example usage:
# solution = Solution()
# print(solution.parseBoolExpr("|(f,t)"))  # Expected output: True
# print(solution.parseBoolExpr("&(t,f)"))  # Expected output: False
# print(solution.parseBoolExpr("!(t)"))    # Expected output: False
