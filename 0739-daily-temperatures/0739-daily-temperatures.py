class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(float("inf"), -1)]
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while temp > stack[-1][0]:
                s_temp, idx = stack.pop()
                output[idx] = i - idx
            
            stack.append((temp, i))

        return output
