class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if i!=j and nums[i]==nums[i+1]:
                return True
            i+=1
        return False
        
