from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        neighbors = [(1, 2), (2, 1), (-1, -2), (-2, -1), (1, -2), (-2, 1), (-1, 2), (2, -1)]
        
        
        steps = 0
        while True:
            for _ in range(len(queue)):
                i, j = queue.pop()
                
                if (i, j) == (x, y):
                    return steps
                
                for step_x, step_y in neighbors:
                    next_x, next_y = i + step_x, j + step_y

                    if (next_x, next_y) not in visited:
                        queue.appendleft((next_x, next_y))
                        visited.add((next_x, next_y))
            
            steps += 1
            
        return -1