class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        prev_less = list(range(1, n + 1))
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                prev_less[i] = i - stack[-1]
                
            stack.append(i)
            
                
        next_less = list(range(n, 0, -1))
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                curr = stack.pop()
                next_less[curr] = i - curr
                
            stack.append(i)
        
        _sum = 0
        for i in range(n):
            _sum += arr[i] * prev_less[i] * next_less[i]
            
        return _sum % (10**9 + 7)