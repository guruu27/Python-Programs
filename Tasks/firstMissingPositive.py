class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        d = Counter([i for i in nums if i>0])
        print(d)
        maxi = max(nums,default=0)
        for i in range(1,maxi):
            if d[i]==0:
                return i
        
        return maxi+1 if maxi+1>0 else 1
        
