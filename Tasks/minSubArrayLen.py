class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minl = float('inf')
        l,r,n = 0,0,len(nums)
        sum_ = 0
        while r<n:
            sum_+=nums[r]
            while sum_>=target:
                minl = min(minl,r-l+1)
                sum_-=nums[l]
                l+=1
            r+=1
            
        return minl if minl!=float('inf') else 0
