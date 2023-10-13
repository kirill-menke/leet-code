class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height, width = len(heights), len(heights[0])
        pacific_indices = list(zip([0] * width + [*range(1, height)], [*range(width)] + [0] * (height - 1)))
        pacific_visited = set([*pacific_indices])

        queue = collections.deque([*pacific_indices])
        while queue:
            i, j = queue.pop()
            for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row, col = i + y, j + x
                if 0 <= row < height and 0 <= col < width \
                    and heights[row][col] >= heights[i][j] and (row, col) not in pacific_visited:
                    queue.appendleft((row, col))
                    pacific_visited.add((row, col))
        

        atlantic_indices = list(zip([*range(height - 1)] + [height - 1] * width, [width - 1] * (height - 1) + [*range(width)]))
        atlantic_visited = set([*atlantic_indices])
        queue = collections.deque([*atlantic_indices])

        while queue:
            i, j = queue.pop()
            for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row, col = i + y, j + x
                if 0 <= row < height and 0 <= col < width \
                    and heights[row][col] >= heights[i][j] and (row, col) not in atlantic_visited:
                    queue.appendleft((row, col))
                    atlantic_visited.add((row, col))
        
        return pacific_visited & atlantic_visited


        
