class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        c=0
        seen = s[0]
        for i in range(len(s)-1):
            if seen==s[i+1]:
                pass
            else:
                seen = s[i+1]
                c+=1
        return c
