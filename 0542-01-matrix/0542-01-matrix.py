from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        queue = deque([])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = [[None] * len(mat[0]) for _ in range(len(mat))]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
                    visited.add((row, col))
                    result[row][col] = 0
    
        while queue:
            row, col, count = queue.pop()
            if mat[row][col] == 1:
                result[row][col] = count
            for dy, dx in directions:
                dy, dx = row + dy, col + dx
                if 0 <= dy < len(mat) and 0 <= dx < len(mat[0]) and (dy, dx) not in visited:
                    queue.appendleft((dy, dx, count + 1))
                    visited.add((dy, dx))

        return result
