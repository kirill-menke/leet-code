class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

        stack = []

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and len(token) > 1):
                stack.append(int(token))
            else:
                op2, op1 = stack.pop(), stack.pop()
                operator = operators[token]
                stack.append(operator(op1, op2))
        
        return stack[0]