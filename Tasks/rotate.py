class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        def transpose(m):
            for i in range(len(m)):
                for j in range(i,len(m[0])):
                    m[i][j],m[j][i] = m[j][i],m[i][j]
            
        def rev(m):
            for k in range(len(m)):
                l,r=0,len(m)-1
                while l<r:
                    m[k][l],m[k][r]= m[k][r],m[k][l]
                    r-=1
                    l+=1
        
        transpose(m)
        rev(m)

