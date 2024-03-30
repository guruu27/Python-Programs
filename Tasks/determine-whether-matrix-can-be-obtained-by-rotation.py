class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        n=len(mat)
        if(mat==target):
            return True

        for i in range(3):
            for j in range(n):
                for k in range(j,n):
                    mat[j][k],mat[k][j] = mat[k][j],mat[j][k]

            for j in range(n):
                mat[j]=mat[j][::-1]

            print(mat)
            if(mat==target):
                return True

        return False
