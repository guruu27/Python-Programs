from collections import Counter
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        moves = 0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                inc = nums[i-1]-nums[i]+1
                nums[i]+=inc
                moves+=inc
        return moves
        
