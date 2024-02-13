class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        r = [0]*len(temp)
        s = []
        for i, t in enumerate(temp):
            while s and t>s[-1][0]:
                st , si = s.pop()
                r[si] = i-si
            s.append([t,i])
        return r
