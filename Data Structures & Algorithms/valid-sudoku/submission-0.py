class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset=[set() for i in range(9)]
        boxset=[set() for i in range(9)]
        colset=[set() for i in range(9)]
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c]=='.':
                    continue
                if board[r][c] in rowset[r] or board[r][c]in colset[c] or board[r][c] in boxset[((r//3)*3)+((c//3))]:
                    return False
                else:
                    rowset[r].add(board[r][c])
                    colset[c].add(board[r][c])
                    boxset[((r//3)*3)+((c//3))].add(board[r][c])                    
        return True
