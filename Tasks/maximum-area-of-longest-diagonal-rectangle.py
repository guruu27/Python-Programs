import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag=0
        diag= 0
        area= 0
        for i in range(len(dimensions)):
            diag= math.sqrt(dimensions[i][0]**2 + dimensions[i][1]**2)   
            if diag> max_diag or (diag==max_diag and dimensions[i][0] * dimensions[i][1]>area) :
                max_diag = diag
                A = dimensions[i][0]*math.sqrt((max_diag**2)-(dimensions[i][0]**2))
                area= A
                    
        return round(area)
    

