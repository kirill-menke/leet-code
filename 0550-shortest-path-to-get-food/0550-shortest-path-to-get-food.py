from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        steps_to_food = 0
        queue = deque([-1])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '*':
                    queue.append((i, j))
                    visited.add((i, j))
        
        while len(queue) > 1:
            cell = queue.pop()
            
            if cell == -1:
                steps_to_food += 1
                queue.appendleft(-1)
                continue
            
            i, j = cell
            if grid[i][j] == '#':
                break

            for y, x in directions:
                row, col = i + y, j + x
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) \
                    and (row, col) not in visited and grid[row][col] != 'X':
                    queue.appendleft((row, col))
                    visited.add((row, col))
        else:
            return -1

        return steps_to_food