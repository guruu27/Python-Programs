class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = 1
        l = max(piles)
        res = l
        while r<=l:
            k = (r+l)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours<=h:
                res = min(res,k)
                l = k-1
            else:
                r = k+1
        return res

