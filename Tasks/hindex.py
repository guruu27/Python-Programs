class Solution:
    def hIndex(self, c: List[int]) -> int:
        n = len(c)
        c.sort()
        for i in range(n):
            if c[i]>=n-i:
                return n-i
        return 0
