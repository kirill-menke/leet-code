class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row_content = [0 for _ in range(n)]
        col_content = [0 for _ in range(n)]
        box_content = [0 for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j]) - 1
                box_cell = i // 3 * 3 + j // 3
                if row_content[i] & (1 << num) or col_content[j] & (1 << num) or box_content[box_cell] & (1 << num):
                    return False
                
                row_content[i] |= (1 << num)
                col_content[j] |= (1 << num)
                box_content[box_cell] |= (1 << num)
        
        return True
                