class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r= defaultdict(list)
        for s in strs:
            c=[0]*26
            for i in s:
                c[ord(i)-ord('a')]+=1
            r[tuple(c)].append(s)
        return r.values()


#Had used hashing DSA for the same
