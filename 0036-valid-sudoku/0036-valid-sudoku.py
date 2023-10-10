class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(len(board))]
        col_sets = [set() for _ in range(len(board[0]))]
        box_sets = [set() for _ in range(len(board))]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == '.':
                    continue
                if num in row_sets[i] or num in col_sets[j] or num in box_sets[i // 3 * 3 + j // 3]:
                    return False
                
                row_sets[i].add(num)
                col_sets[j].add(num)
                box_sets[i // 3 * 3 + j // 3].add(num)
        
        return True
