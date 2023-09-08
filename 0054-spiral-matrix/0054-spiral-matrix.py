class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        direction = 1
        i, j = 0, -1
        result = []

        while m * n > 0:
            for _ in range(n):
                j += direction
                result.append(matrix[i][j])
            m -= 1

            for _ in range(m):
                i += direction
                result.append(matrix[i][j])
            n -= 1
        
            direction = -direction
        
        return result