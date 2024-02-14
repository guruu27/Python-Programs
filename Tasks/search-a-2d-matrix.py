class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top,bot = 0, m-1
        while top<=bot:
            row = (bot+top)//2
            if target> matrix[row][-1]:
                top = row+1
            elif target< matrix[row][0]:
                bot = row-1
            else:
                break
        
        
        if not (top<=bot):
            return False
          
        row = (top+bot)//2
        i = 0
        j = n-1
        while i<=j:
            mid = (j+i)//2
            if target> matrix[row][mid]:
                i = mid+1
            elif target<matrix[row][mid]:
                j = mid-1
            else:
                return True
        return False
