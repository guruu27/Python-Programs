class Solution:    
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        l=0
        while i<j:
            l = max(l, min(height[i],height[j])*abs(i-j))
            if height[i]<height[j]:
                i+=1
            elif height[i]>=height[j]:
                j-=1
        return l
