from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_cells = set()
        atlantic_cells = set()

        height = len(heights)
        width = len(heights[0])

        pacific_indices = list(zip([0] * width + [*range(height)], [*range(width)] + [0] * height))
        queue = deque([*pacific_indices])
        pacific_cells |= {*pacific_indices}
        
        while queue:
            i, j = queue.pop()
            
            for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row, col = i + y, j + x
        
                if 0 <= row < height and 0 <= col < width and (row, col) not in pacific_cells and heights[row][col] >= heights[i][j]:
                    pacific_cells.add((row, col))
                    queue.appendleft((row, col))

        atlantic_indices = list(zip([*range(height)] + [height - 1] * width, [width - 1] * (height - 1) + [*range(width)]))
        
        queue = deque([*atlantic_indices])
        atlantic_cells |= {*atlantic_indices}

        while queue:
            i, j = queue.pop()
            
            for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row, col = i + y, j + x
                if 0 <= row < height and 0 <= col < width and (row, col) not in atlantic_cells and heights[row][col] >= heights[i][j]:
                    atlantic_cells.add((row, col))
                    queue.appendleft((row, col))
        

        return pacific_cells & atlantic_cells
                    



        
