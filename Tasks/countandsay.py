class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        
        for _ in range(n-1):
            i = 0
            t = []
            while i < len(s):
                j = i
                while j< len(s) and i==j: j+=1
                t.append(str(j-i))
                t.append(str(s[i]))
                i = j
            s = "".join(t)
        return s
