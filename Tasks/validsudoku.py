class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Validate row
        for i in range(9):
            s=set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j]!='.':
                    s.add(board[i][j])
        #Validate col
        for i in range(9):
            s=set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                elif board[j][i]!='.':
                    s.add(board[j][i])
        #Validate 3*3 box
        starts = [(0,0),(0,3),(0,6),
                  (3,0),(3,3),(3,6),
                  (6,0),(6,3),(6,6)]
        for i,j in starts:
            s = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    if board[row][col] in s:
                        return False
                    elif board[row][col]!='.':
                        s.add(board[row][col])
        return True
