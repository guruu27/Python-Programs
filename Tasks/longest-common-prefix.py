class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        strs=sorted(strs)
        r=strs[0]
        l=strs[-1]
        
        for i in range(min(len(r),len(l))):
            if r[i]!=l[i]:
                return res
            res+=r[i]
        return res
