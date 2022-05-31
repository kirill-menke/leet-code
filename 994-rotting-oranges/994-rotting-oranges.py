class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_oranges = 0
        
        for i, ls in enumerate(grid):
            for j, x in enumerate(ls):
                if x == 1: 
                    fresh_oranges += 1
                elif x == 2:
                    queue.appendleft((i, j))
                    
        queue.appendleft(-1)
                    
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        time = 0
        
        while len(queue) > 1:
            curr = queue.pop()
            
            if curr == -1:
                time += 1
                queue.appendleft(-1)
            else:
                for x, y in neighbors:
                    i, j = curr[0] + x, curr[1] + y
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                        queue.appendleft((i, j))
                        grid[i][j] = 2
                        fresh_oranges -= 1
                         
        return time if fresh_oranges == 0 else -1
                        
                        
            
        