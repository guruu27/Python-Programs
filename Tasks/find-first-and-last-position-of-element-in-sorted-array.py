class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        k=0
        for i,j in enumerate(nums):
            if j==target:
                k=1
                res.append(i)
        if len(nums)==1 and target!=nums[0]:
            return [-1,-1]
        elif len(nums)==1 and target==nums[0]:
            return [0,0]
        elif len(res)==1:
            return [res[0],res[0]]
        else:
            return [res[0],res[-1]] if k else [-1,-1]
