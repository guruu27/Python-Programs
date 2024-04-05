class Solution:
    def makeGood(self, s: str) -> str:
      res = []
      for ch in s:
        if res and abs(ord(res[-1])-ord(ch))==32:
            res.pop()
        else:
            res.append(ch)
      return "".join(res)  
