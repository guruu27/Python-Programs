class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lo,mi,hi = 0,0,len(nums)-1
        while mi<=hi:
            if nums[mi]==0:
                nums[mi],nums[lo] = nums[lo],nums[mi]
                mi +=1
                lo += 1
            elif nums[mi]==1:
                mi +=1
            else:
                nums[mi],nums[hi] = nums[hi],nums[mi]
                hi -=1
            
        return nums
            
