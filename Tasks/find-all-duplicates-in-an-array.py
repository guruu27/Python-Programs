class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        d = Counter(nums)
        for k,v in d.items():
            if v>1:
                res.append(k)
        return res
        
