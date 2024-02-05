class Solution:
    def reverse(self, x: int) -> int:
        l=list(str(x))
        h=['']
        r=0
        for i in l[::-1]:
            if i=='-':
                r=1
                continue
            h[0]+=i
        y=int(h[0]) if r==0 else int('-'+h[0])
        if int(h[0]) >= 2** 31 -1 or int(h[0]) <= -2** 31:
            return 0 
        return y
