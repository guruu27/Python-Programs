class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        rep = defaultdict(int)
        for i in range(len(s)-9):
            rep[s[i:i+10]]+=1
        return [j for j in rep.keys() if rep[j]>1]
