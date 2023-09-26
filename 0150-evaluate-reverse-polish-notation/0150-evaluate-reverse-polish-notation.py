class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }

        cur_pos = 0
        while len(tokens) > 1:
            while tokens[cur_pos] not in self.operations:
                cur_pos += 1
            
            op1, op2 = int(tokens[cur_pos - 2]), int(tokens[cur_pos - 1])
            operation = self.operations[tokens[cur_pos]]
            res = operation(op1, op2)

            del tokens[cur_pos - 2: cur_pos + 1]
            tokens.insert(cur_pos - 2, res)
            cur_pos -= 1
        
        return int(tokens[0])


            

