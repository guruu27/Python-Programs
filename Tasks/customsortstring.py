class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d=Counter(s)
        res=''
        for ch in order:
            if ch in d:
                res+=ch*d[ch]
                del d[ch]
        for ch in d:
            res+=ch*d[ch]
        return res

