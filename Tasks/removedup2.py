class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        occ = 1
        for i in range(1,len(nums)):

            if nums[i]==nums[i-1]:
                occ+=1
            else:
                occ =1

            if occ<=2:
                nums[idx]=nums[i]
                idx+=1

        return idx