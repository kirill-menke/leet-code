class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        self.operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

        stack = []

        for token in tokens:
            if token not in self.operations:
                stack.append(token)
            else:
                operation = self.operations[token]
                op2, op1 = int(stack.pop()), int(stack.pop())
                stack.append(operation(op1, op2))
        
        return int(stack.pop())