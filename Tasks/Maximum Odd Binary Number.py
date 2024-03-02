class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s1 = sorted(s,reverse=True)
        for i in range(len(s1)-1,-1,-1):
            if s1[i]=='1':
                s1[i] , s1[-1] = s1[-1], s1[i]
                break
        return ''.join(s1)
