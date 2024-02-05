class Solution:
    def minChanges(self, s: str) -> int:
        s=list(s)
        print(s)
        c=0
        r=[]
        i,j = 0, len(s)-1
        while i<j:
            r.append(s[i:i+2])
            i+=2
        for i in r:
            print(i)
            if i[1]==i[0]:
                continue
            else:
                c+=1
        return c    
