class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        c1 = None
        for num in nums:
            if c==0:
                c1 = num
            c += 1 if c1==num else -1
        return c1    
