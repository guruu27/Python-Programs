class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        s=0
        for num in nums:
            r = num*num
            if r>s:
                res.append(r)
                s = r
            else:
                res.append(r)
        return sorted(res)
