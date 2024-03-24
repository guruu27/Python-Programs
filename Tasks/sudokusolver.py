from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row, col, subbox = defaultdict(set), defaultdict(set), defaultdict(set)
        to_visit = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    subbox[(i // 3, j // 3)].add(board[i][j])
                else:
                    to_visit.append((i, j))
                    
        def backtracking():
            if not to_visit:
                return True
            removed_cell = to_visit.pop()
            i, j = removed_cell
            subi, subj = i // 3, j // 3
            row_copy, col_copy, subbox_copy = row[i].copy(), col[j].copy(), subbox[(subi, subj)].copy()
            for num in range(1, 10):
                str_num = str(num)
                if str_num not in row_copy and str_num not in col_copy and str_num not in subbox_copy:
                    board[i][j] = str_num
                    row[i].add(str_num)
                    col[j].add(str_num)
                    subbox[(subi, subj)].add(str_num)
                    if backtracking():
                        return True
                    board[i][j] = '.'
                    row[i].remove(str_num)
                    col[j].remove(str_num)
                    subbox[(subi, subj)].remove(str_num)
            to_visit.append(removed_cell)
            return False
        
        backtracking()
